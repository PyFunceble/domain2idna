#!/usr/bin/env python3

"""
domain2idna - A tool to convert a domain or a file with a list
of domain to the famous IDNA format.

This submodule will test domain2idna.core

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to domains2idna!!

Project link:
    https://github.com/funilrys/domain2idna

Project documentation:
    http://domain2idna.readthedocs.ios

License:
    MIT License

    Copyright (c) 2018 Nissar Chababy

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

from domain2idna.core import Core


class TestCore(TestCase):
    """
    This class test Core.to_idna.
    """

    def test_to_idna_single(self):
        """
        This method run and test Core.idna.
        """

        domain_to_test = "ṁỵetherwallet.com"

        expected = "xn--etherwallet-tv8eq7f.com"
        actual = Core(domain_to_test).to_idna()

        self.assertEqual(expected, actual)

    def test_to_idna_multiple(self):
        """
        This method run and test Core.idna.
        """

        domains_to_test = [
            "bịllogram.com",
            "bittréẋ.com",
            "cryptopiạ.com",
            "coinbȧse.com",
            "cṙyptopia.com",
            "0.0.0.0 ṁỵetherwallet.com",
        ]

        expected = [
            "xn--bllogram-g80d.com",
            "xn--bittr-fsa6124c.com",
            "xn--cryptopi-ux0d.com",
            "xn--coinbse-30c.com",
            "xn--cyptopia-4e0d.com",
            "0.0.0.0 xn--etherwallet-tv8eq7f.com",
        ]
        actual = Core(domains_to_test).to_idna()

        self.assertEqual(expected, actual)

    def test_commented_line(self):
        """
        This method test that the comments are returned normally.
        """

        comments = [
            "# Hello, World!",
            "# This is another commented line",
            "cryptopiạ.com",
            "# This is a commented line with bittréẋ.com",
            "# cryptopiạ.com",
        ]

        expected = [
            "# Hello, World!",
            "# This is another commented line",
            "xn--cryptopi-ux0d.com",
            "# This is a commented line with bittréẋ.com",
            "# cryptopiạ.com",
        ]

        actual = Core(comments).to_idna()

        self.assertEqual(expected, actual)

    def test_hosts_file_format(self):
        """
        This method test that the hosts file format is always respected.
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

        actual = Core(given).to_idna()

        self.assertEqual(expected, actual)

        given = "0.0.0.0 bịllogram.com"

        expected = "0.0.0.0 xn--bllogram-g80d.com"

        actual = Core(given).to_idna()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()
