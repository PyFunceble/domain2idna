"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

Provides the base to all other sublogic(s).

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to domains2idna!!

Project link:
    https://github.com/PyFunceble/domain2idna

Project documentation:
    http://domain2idna.readthedocs.io

License:
    MIT License

    Copyright (c) 2018-2019 Nissar Chababy
    Copyright (c) 2019 PyFunceble

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from urllib.parse import urlparse


class Converter:
    """
    Provides a base for every core logic we add.

    :param subject: The subject to convert.
    :type subject: str, list

    :param str original_encoding:
        The encoding to provide as output.
    """

    to_ignore = [
        "0.0.0.0",
        "localhost",
        "127.0.0.1",
        "localdomain",
        "local",
        "broadcasthost",
        "allhosts",
        "allnodes",
        "allrouters",
        "localnet",
        "loopback",
        "mcastprefix",
    ]

    def __init__(self, subject, original_encoding="utf-8"):
        self.subject = subject
        self.encoding = original_encoding

    def convert_to_idna(self, subject, original_encoding="utf-8"):
        """
        Converts the given subject to IDNA.

        :param str subject: The subject to convert.
        :rtype: str
        """

        if subject in self.to_ignore:
            return subject

        if "://" not in subject:
            try:
                return subject.encode("idna").decode(original_encoding)
            except UnicodeError:  # pragma: no cover
                return subject

        parsed_url = urlparse(subject)
        result = f"{parsed_url.scheme}://{self.convert_to_idna(parsed_url.netloc)}{parsed_url.path}"

        if parsed_url.params:
            result += f";{parsed_url.params}"
        if parsed_url.query:
            result += f"?{parsed_url.query}"
        if parsed_url.fragment:
            result += f"#{parsed_url.fragment}"

        return result

    def __get_converted(self, subject):
        """
        Process the actual conversion.

        :param str subject: The subject to convert.

        :rtype: str
        """

        if (
            not subject
            or not subject.strip()
            or subject in self.to_ignore
            or subject.startswith("#")
        ):
            return subject

        if "#" in subject and "://" not in subject:
            comment = " " + subject[subject.find("#") :]
            subject = subject[: subject.find("#")].strip()
        else:
            comment = ""

        return (
            " ".join(
                [
                    self.convert_to_idna(x, original_encoding=self.encoding)
                    for x in subject.split()
                ]
            )
            + comment
        ).strip()

    def get_converted(self):
        """
        Provides the converted data.
        """

        if isinstance(self.subject, list):
            return [self.__get_converted(x) for x in self.subject]
        return self.__get_converted(self.subject)
