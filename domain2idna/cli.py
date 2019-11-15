"""
domain2idna - The tool to convert a domain or a file with a list
of domain to the famous IDNA format.

This submodule provides everything related to the CLI.

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

import argparse

from colorama import Fore, Style
from colorama import init as initiate_colorama

from . import VERSION, domain, file


def tool():  # pragma: no cover
    """
    Provides the CLI.
    """

    if __name__ == "domain2idna.cli":
        initiate_colorama(autoreset=True)

        parser = argparse.ArgumentParser(
            description="domain2idna - The tool to convert a domain or a file with \
            a list of domain to the famous IDNA format.",
            epilog="Crafted with %s by %s"
            % (
                Fore.RED + "♥" + Fore.RESET,
                Style.BRIGHT
                + Fore.CYAN
                + "Nissar Chababy (Funilrys)"
                + Style.RESET_ALL,
            ),
        )

        parser.add_argument(
            "-d", "--domain", type=str, help="Sets the domain to convert."
        )

        parser.add_argument(
            "-e", "--encoding", type=str, help="Sets the encoding to use.", default="utf-8"
        )

        parser.add_argument(
            "-f",
            "--file",
            type=str,
            help="Sets the file to read to get the domain(s) to convert.",
        )

        parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="Sets the file where we write the converted domain(s).",
        )

        parser.add_argument(
            "-v", "--version", action="version", version="%(prog)s " + VERSION
        )

        args = parser.parse_args()

        if args.domain:
            domain(args.domain, args.output, encoding=args.encoding)
        elif args.file:
            file(args.file, args.output, encoding=args.encoding)
