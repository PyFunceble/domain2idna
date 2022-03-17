#!/usr/bin/env python3

"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

Tests the API endpoints.

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

    Copyright (c) 2019, 2020, 2021, 2022 PyFunceble
    Copyright (c) 2018, 2019, 2020, 2021, 2022 Nissar Chababy

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

# pylint: disable=duplicate-code

from unittest import TestCase
from unittest import main as launch_tests

from domain2idna import domain2idna


class TestInit(TestCase):
    """
    This class will test domain2idna.__init__.
    """

    def setUp(self):
        """
        Setup all cross tests variables.
        """

        self.domain_to_test = ["ṁỵetherwallet.com", "xn--etherwallet-tv8eq7f.com\n"]

        self.domains_to_test = [
            "bittréẋ.com",
            "bịllogram.com",
            "coinbȧse.com",
            "cryptopiạ.com",
            "cṙyptopia.com",
            "0.0.0.0 ṁỵetherwallet.com",
        ]

        self.converted = [
            "xn--bittr-fsa6124c.com",
            "xn--bllogram-g80d.com",
            "xn--coinbse-30c.com",
            "xn--cryptopi-ux0d.com",
            "xn--cyptopia-4e0d.com",
            "0.0.0.0 xn--etherwallet-tv8eq7f.com",
        ]

        self.empty_inputs = ["", " ", "  ", None, False]

    def test_get(self):
        """
        This method will test domain2idna.get
        """

        expected = self.converted
        actual = domain2idna(self.domains_to_test)
        self.assertEqual(expected, actual)

        expected = self.empty_inputs
        actual = domain2idna(self.empty_inputs)
        self.assertEqual(expected, actual)

        expected = None
        actual = domain2idna(None)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()
