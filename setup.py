"""
domain2idna - The tool to convert a domain or a file with a list of domain to
the famous IDNA format.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to domain2idna!!

Repository:
    https://github.com/PyFunceble/domain2idna

License:
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

import os
from re import compile as comp
import re
from unittest import TestLoader

from setuptools import setup


def test_suite():
    """
    This method will discover and run all the test
    """

    test_loader = TestLoader()
    tests = test_loader.discover("tests", pattern="test_*.py")
    return tests


def get_requirements(*, mode="standard"):
    """
    This function extract all requirements from requirements.txt.
    """

    mode2files = {
        "standard": ["requirements.txt"],
        "dev": ["requirements.dev.txt"],
        "test": ["requirements.test.txt"],
    }

    mode2files["full"] = [y for x in mode2files.values() for y in x]

    result = set()

    for file in mode2files[mode]:
        with open(file, "r", encoding="utf-8") as file_stream:
            for line in file_stream:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "#" in line:
                    line = line[: line.find("#")].strip()

                if not line:
                    continue

                result.add(line)

    return list(result)


def get_version():
    """
    This function will extract the version from domain2idna/__about__.py
    """

    to_match = re.compile(r'__version__.*=\s+"(.*)"')

    if os.path.exists("domain2idna/__about__.py"):
        about_path = "domain2idna/__about__.py"
    elif os.path.exists("../domain2idna/__about__.py"):
        about_path = "../domain2idna/__about__.py"
    else:
        raise FileNotFoundError("No __about__.py found.")

    with open(about_path, encoding="utf-8") as file_stream:
        extracted = to_match.findall(file_stream.read())[0]

    return extracted

def get_long_description():  # pragma: no cover
    """
    This function return the long description.
    """

    return open("README.md", encoding="utf-8").read()


if __name__ == "__main__":
    setup(
        name="domain2idna",
        version=get_version(),
        python_requires=">=3.6.2, <4",
        description="The tool to convert a domain or a file with a list of domain to the "
        "famous IDNA format.",
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        install_requires=get_requirements(mode="standard"),
        extras_require={
            "test": get_requirements(mode="test"),
            "dev": get_requirements(mode="dev"),
            "full": get_requirements(mode="full"),
        },
        author="funilrys",
        author_email="contact@funilrys.com",
        license="MIT https://raw.githubusercontent.com/PyFunceble/domain2idna/master/LICENSE",
        url="https://github.com/PyFunceble/domain2idna",
        platforms=["any"],
        packages=["domain2idna"],
        keywords=["Python", "domain", "idna"],
        classifiers=[
            "Environment :: Console",
            "Topic :: Internet",
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
        ],
        entry_points={"console_scripts": ["domain2idna=domain2idna.cli:tool"]},
    )
