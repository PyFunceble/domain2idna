#!/usr/bin/env python3

"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to domains2idna!!

Project link:
    https://github.com/PyFunceble/domain2idna

Project documentation:
    http://domain2idna.readthedocs.io

License:
::

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

# pylint: disable=bad-continuation

import warnings

from .converter import Converter
from .helpers import File

VERSION = "1.10.0"


def get(domain_to_convert):
    """
    This function is a passerelle between the front
    and the backend of this module.


    :param str domain_to_convert:
        The domain to convert.

    :return:
        str:
            if a string is given.
        list:
            if a list is given.
    :rtype: str, list
    """

    warnings.warn(
        "`domain2idna.get` will be deprecated in future version. "
        "Please use `domain2idna.process_conversion` instead.",
        DeprecationWarning,
    )

    if domain_to_convert:
        return Converter(domain_to_convert).get_converted()

    return domain_to_convert


def get_converted(subject, encoding="utf-8"):
    """
    Process the conversion of the given subject.

    :param subject: The subject to convert.
    :type subject: str, list
    :param str encoding: The encoding to provide.

    :rtype: list, str
    """

    return Converter(subject, original_encoding=encoding).get_converted()


def domain(domain_to_convert, output=None, encoding="utf-8"):
    """
    This function convert the given domain to IDNA format.


    :param str domain_to_convert:
        The domain to convert.
    :param str output:
        The output of the conversion. If not set, we output to stdout.
     :param str encoding:
        The encoding to provide.

    :raise ValueError:
        If the given :code:`domain_to_convert` is empty.
    """

    if domain_to_convert and domain_to_convert.strip():
        converted = Converter(
            domain_to_convert, original_encoding=encoding
        ).get_converted()

        if output:
            File(output).write(converted)
        else:
            print(converted)
    else:
        raise ValueError("<domain_to_convert> is not understable.")


def file(file_to_convert, output=None, encoding="utf-8"):
    """
    This function read a file and convert each line of the file to IDNA.

    :param str file_to_convert:
        The file to convert
    :param str output:
        The output of the conversion. If not set, we output to stdout.
    :param str encoding:
        The encoding to provide.
    """

    if file_to_convert:
        converted = []

        try:
            to_convert = File(file_to_convert).read(encoding=encoding).split("\n")
        except (UnicodeEncodeError, UnicodeDecodeError):  # pragma: no cover
            to_convert = File(file_to_convert).read(encoding="ISO-8859-1").split("\n")

        converted = Converter(to_convert).get_converted()

        if output:
            File(output).write("\n".join(converted))
        else:
            print("\n".join(converted))
