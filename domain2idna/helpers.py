#!/usr/bin/env python3

"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

This submodule contains all helpers that are used by other submodules.

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

from os import remove


class File:
    """
    File treatment/manipulations.

    :param str filename:
        A path to the file to manipulate.
    """

    def __init__(self, filename):
        self.file = filename

    def write(self, data_to_write):
        """
        Writes or appends data into the given file path.

        :param str data_to_write:
            The data to write.
        """

        if data_to_write and isinstance(data_to_write, str):
            with open(self.file, "w", encoding="utf-8") as file:
                file.write(data_to_write)

    def read(self, encoding=None):
        """
        Reads a given file path and return its content.

        :param str encoding:
            The encoding to use when opening the file.

        :rtype: str
        """

        if not encoding:
            encoding = "utf-8"

        with open(self.file, "r", encoding=encoding) as file:
            funilrys = file.read()

        return funilrys

    def delete(self):
        """
        Deletes a given file path.

        .. warning::

            We handle the case that the file does not exist.
        """

        try:
            remove(self.file)
        except OSError:
            pass
