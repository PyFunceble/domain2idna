#!/usr/bin/env python3

"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

Tests the helpers.

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

from os import path
from unittest import TestCase
from unittest import main as launch_tests

from domain2idna.helpers import File


class TestFile(TestCase):
    """
    Tests helpers.File.
    """

    def test_write_delete(self):
        """
        Tests helpers.File.write along with helpers.File.delete.
        """

        expected = "Hello, World! I'm PyFunceble"
        File("hi").write(expected)

        with open("hi") as file:
            actual = file.read()

        self.assertEqual(expected, actual)

        expected = False
        File("hi").delete()
        actual = path.isfile("hi")

        self.assertEqual(expected, actual)

    def test_write_overwrite_delete(self):
        """
        Tests helpers.File.write along with helpers.File.delete.
        """

        expected = "Hello, World! I'm PyFunceble"
        File("hi").write(expected)

        with open("hi") as file:
            actual = file.read()

        self.assertEqual(expected, actual)

        expected = "Hello, World! Python is great, you should consider learning it!"
        File("hi").write(expected)

        with open("hi") as file:
            actual = file.read()

        self.assertEqual(expected, actual)

        expected = False
        File("hi").delete()
        actual = path.isfile("hi")

        self.assertEqual(expected, actual)

    def test_read_delete(self):
        """
        Tests helpers.File.read along with helpers.File.delete.
        """

        expected = "Hello, World! This has been written by Fun Ilrys."
        File("hi").write(expected)
        actual = File("hi").read()

        self.assertEqual(expected, actual)

        expected = False
        File("hi").delete()
        actual = path.isfile("hi")

        self.assertEqual(expected, actual)

    def test_delete_not_exist(self):
        """
        Tests helpers.File.delete for the case that the file does
        not exists.
        """

        filename = "this_file_is_a_ghost"

        expected = False
        actual = path.isfile(filename)

        self.assertEqual(expected, actual)

        File(filename).delete()

        expected = False
        actual = path.isfile(filename)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    launch_tests()
