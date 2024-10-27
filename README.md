![image](https://raw.githubusercontent.com/PyFunceble/logo/dev/Green/HD/RM.png)

<div align="center">
    <a href="https://coveralls.io/github/PyFunceble/domain2idna?branch=master">
        <img src="https://coveralls.io/repos/github/PyFunceble/domain2idna/badge.svg?branch=master" />
    </a>
    <a href="https://github.com/PyFunceble/domain2idna/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/PyFunceble/domain2idna.svg" />
    </a>
    <a href="https://github.com/PyFunceble/domain2idna/releases/latest">
        <img src="https://img.shields.io/github/release/PyFunceble/domain2idna.svg" />
    </a>
    <a href="https://github.com/ambv/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" />
    </a>
</div>

# domains2idna

**The tool to convert domains to the famous IDNA format.**


This project provides a tool for list or hosts file maintainer that can
converts domain to the Punycode/IDNA format.

## Documentation as the place to be!

Want to know more about **domain2idna**? We invite you to read the
documentation at <https://domain2idna.readthedocs.io>!

Want a local copy!? We get you covered!

Simply run the following and enjoy the documentation!

    $ # We move to the docs directory
    $ cd docs/
    $ # We build the documentation
    $ make html
    $ # We run the documentation with our favorite browser.
    $ chromium _builld/html/index.html

## What can domain2idna do ?

- Read a given domain and convert it to the Punycode/IDNA format.
- Read a given URL and convert its base to Punycode/IDNA format.
- Read a file and convert all non-commented line to the Punycode/IDNA
    format.
- Print the converted data on the screen.
- Save into a file the converted data.
- Return the converted data (when used as a module).
- Ignore commented inputs (starts with `#`)

## License

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