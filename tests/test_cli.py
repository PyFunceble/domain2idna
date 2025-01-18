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

# pylint: disable=duplicate-code

import sys
from io import StringIO
from os import path
from unittest import TestCase
from unittest import main as launch_tests

from domain2idna.cli import file, subjects
from domain2idna.helpers import File


class BaseStdout(TestCase):
    """
    This class is the one we use when we want to catch stdout.
    """

    def setUp(self):
        """
        Setup stdout.
        """

        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = sys.__stdout__


class TestCLI(BaseStdout):
    """
    This class will test domain2idna.__init__.
    """

    def setUp(self):
        """
        Setup all cross tests variables.
        """

        super().setUp()
        self.domain_to_test = ["ṁỵetherwallet.com", "xn--etherwallet-tv8eq7f.com\n"]

        self.domains_to_test = [
            "bịllogram.com",
            "0.0.0.0 ṁỵetherwallet.com",
            "coinbȧse.com",
            "cryptopiạ.com",
            "bittréẋ.com",
            "cṙyptopia.com",
        ]

        self.converted = [
            "xn--bllogram-g80d.com",
            "0.0.0.0 xn--etherwallet-tv8eq7f.com",
            "xn--coinbse-30c.com",
            "xn--cryptopi-ux0d.com",
            "xn--bittr-fsa6124c.com",
            "xn--cyptopia-4e0d.com",
        ]

        self.empty_inputs = ["", None, False]

    def test_domain(self):
        """
        This method will test domain2idna.domain()
        """


        expected = self.domain_to_test[-1]

        subjects(self.domain_to_test[0], None)
        actual = sys.stdout.getvalue()

        self.assertEqual(expected, actual)

    def test_domain_output(self):
        """
        This method will test domain2idna.domain() for the case
        that we want the output into a file.
        """

        output_file = "this_file_is_a_ghost"

        expected = False
        actual = path.isfile(output_file)

        self.assertEqual(expected, actual)

        expected = self.domain_to_test[-1][:-1]
        subjects(self.domain_to_test[0], output_file)
        actual = File(output_file).read()

        self.assertEqual(expected, actual)

        File(output_file).delete()
        expected = False
        actual = path.isfile(output_file)

        self.assertEqual(expected, actual)

    def test_empty_domain(self):
        """
        This method will test domain2idna.domain() for the case
        that an empty string is given.
        """

        for empty_domain in self.empty_inputs:
            self.assertRaises(
                ValueError,
                lambda: subjects(empty_domain),  # pylint: disable=cell-var-from-loop
            )

    def test_file(self):
        """
        This method will test domain2idna.file().
        """

        file_to_pass = "this_file_is_a_ghost"

        expected = False
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

        File(file_to_pass).write("\n".join(self.domains_to_test))

        expected = True
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

        expected = "\n".join(self.domains_to_test)
        actual = File(file_to_pass).read()

        self.assertEqual(expected, actual)

        expected = "\n".join(self.converted) + "\n"
        file(file_to_pass, None)
        actual = sys.stdout.getvalue()

        self.assertEqual(expected, actual)

        File(file_to_pass).delete()

        expected = False
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

    def test_file_output(self):
        """
        This method will test domain2idna.file() for the case we want
        the results in a file.
        """

        file_to_pass = "this_file_is_a_ghost"
        output_file = "this_file_is_a_converted_ghost"

        expected = False
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

        File(file_to_pass).write("\n".join(self.domains_to_test))

        expected = True
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

        expected = "\n".join(self.domains_to_test)
        actual = File(file_to_pass).read()

        self.assertEqual(expected, actual)

        expected = "\n".join(self.converted)
        file(file_to_pass, output_file)
        actual = File(output_file).read()

        self.assertEqual(expected, actual)

        File(file_to_pass).delete()
        File(output_file).delete()

        expected = False
        actual = path.isfile(file_to_pass)

        self.assertEqual(expected, actual)

        expected = False
        actual = path.isfile(output_file)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()
