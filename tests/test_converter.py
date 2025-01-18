#!/usr/bin/env python3

"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

Tests the converter itself.

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

    Copyright (c) 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 Nissar Chababy
    Copyright (c) 2019, 2020, 2021, 2022, 2023, 2024, 2025 PyFunceble Contributors

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

from unittest import TestCase
from unittest import main as launch_tests

from domain2idna.converter import Converter


class TestConverter(TestCase):
    """
    Tests Converter.
    """

    def test_to_idna_single(self):
        """
        Runs and tests Converter
        """

        domain_to_test = "ṁỵetherwallet.com"

        expected = "xn--etherwallet-tv8eq7f.com"
        actual = Converter(domain_to_test).get_converted()

        self.assertEqual(expected, actual)

    def test_single_very_long_fqdn(self):
        """
        Tests the conversion of a very long FQDN.
        """

        domain_to_test = "ạ" + "a" * 955 + ".com"

        expected = "ạ" + "a" * 955 + ".com"
        actual = Converter(domain_to_test).get_converted()

        self.assertEqual(expected, actual)

    def test_to_idna_multiple(self):
        """
        Runs and tests Converter.
        """

        domains_to_test = [
            "bịllogram.com",
            "bittréẋ.com",
            "cryptopiạ.com",
            "coinbȧse.com",
            "cṙyptopia.com",
            "0.0.0.0 ṁỵetherwallet.com",
            "0.0.0.0/8",
        ]

        expected = [
            "xn--bllogram-g80d.com",
            "xn--bittr-fsa6124c.com",
            "xn--cryptopi-ux0d.com",
            "xn--coinbse-30c.com",
            "xn--cyptopia-4e0d.com",
            "0.0.0.0 xn--etherwallet-tv8eq7f.com",
            "0.0.0.0/8",
        ]
        actual = Converter(domains_to_test).get_converted()

        self.assertEqual(expected, actual)

    def test_to_idna_multiple_urls(self):
        """
        Runs and tests Converter.
        """

        domains_to_test = [
            "http://bịllogram.com",
            "https://bittréẋ.com/path;parameters?query#fragment",
            "ftp://cryptopiạ.com",
            "git://coinbȧse.com",
            "://coinbȧse.com/hello_world",
        ]

        expected = [
            "http://xn--bllogram-g80d.com",
            "https://xn--bittr-fsa6124c.com/path;parameters?query#fragment",
            "ftp://xn--cryptopi-ux0d.com",
            "git://xn--coinbse-30c.com",
            "://xn--coinbse-30c.com/hello_world",
        ]
        actual = Converter(domains_to_test).get_converted()

        self.assertEqual(expected, actual)

    def test_commented_line(self):
        """
        Tests that the comments are returned normally.
        """

        comments = [
            "# Hello, World!",
            "# This is another commented line",
            "cryptopiạ.com  # This is a comment at the end of a line.",
            "# This is a commented line with bittréẋ.com",
            "# cryptopiạ.com",
        ]

        expected = [
            "# Hello, World!",
            "# This is another commented line",
            "xn--cryptopi-ux0d.com # This is a comment at the end of a line.",
            "# This is a commented line with bittréẋ.com",
            "# cryptopiạ.com",
        ]

        actual = Converter(comments).get_converted()

        self.assertEqual(expected, actual)

    def test_hosts_file_format(self):
        """
        Tests that the hosts file format is always respected.
        """

        given = [
            "0.0.0.0 bịllogram.com",
            "127.0.0.1 bittréẋ.com",
            "0.0.0.0 cryptopiạ.com",
            "127.0.0.1 coinbȧse.com",
            "0.0.0.0 cṙyptopia.com",
        ]

        expected = [
            "0.0.0.0 xn--bllogram-g80d.com",
            "127.0.0.1 xn--bittr-fsa6124c.com",
            "0.0.0.0 xn--cryptopi-ux0d.com",
            "127.0.0.1 xn--coinbse-30c.com",
            "0.0.0.0 xn--cyptopia-4e0d.com",
        ]

        actual = Converter(given).get_converted()

        self.assertEqual(expected, actual)

        given = "0.0.0.0 bịllogram.com"

        expected = "0.0.0.0 xn--bllogram-g80d.com"

        actual = Converter(given).get_converted()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()
