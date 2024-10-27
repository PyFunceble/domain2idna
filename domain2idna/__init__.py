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

    Copyright (c) 2018, 2019, 2020, 2021, 2022, 2023, 2024 Nissar Chababy
    Copyright (c) 2019, 2020, 2021, 2022, 2023, 2024 PyFunceble Contributors

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

import warnings

from .converter import Converter

VERSION = "1.12.1"


def domain2idna(subject, encoding="utf-8"):
    """
    Process the conversion of the given subject.

    :param subject: The subject to convert.
    :type subject: str, list
    :param str encoding: The encoding to provide.

    :rtype: list, str
    """

    return Converter(subject, original_encoding=encoding).get_converted()


def get(domain_to_convert):  # pragma: no cover
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

    .. deprecated:: 1.10.0
        Use :func:`~domain2idna.domain2idna` instead.
    """

    warnings.warn(
        "`domain2idna.get` will be removed in future version. "
        "Please use `domain2idna.domain2idna` instead.",
        DeprecationWarning,
    )

    return domain2idna(domain_to_convert)
