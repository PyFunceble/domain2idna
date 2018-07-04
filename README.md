# domains2idna

## The tool to convert domains to the famous IDNA format.

* * *

# Tests

```shell
# The following run the tests.
$ python setup.py test
```

# Installation

You can install domain2idna with two ways.

```shell
# This install domain2idna without having to manually clone the repository
$ pip install git+https://github.com/funilrys/domain2idna.git#egg=domain2idna
```

```shell
# This install all dependencies along with domain2idna after you cloned the repository.
# Usage: developement only.
$ python setup.py test
```

# Usage

## Import

```python
#!/usr/bin/env python3

"""
This module uses domains2idna to convert a given domain.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Contributors:
    Let's contribute to this example!!

Repository:
    https://github.com/funilrys/domain2idna
"""
from domain2idna import domain as domain2idna

DOMAINS = [
    "bittréẋ.com", "bịllogram.com", "coinbȧse.com", "cryptopiạ.com", "cṙyptopia.com"
]

# The following return the result of the whole loop.
print("List of converted domains: %s" % domain2idna(DOMAINS, True))

# The following return the result of only one element.
print( "String representing a converted domain: %s"% domain2idna(DOMAINS[-1], True))
```

## Command-Line

    usage: domain2idna [-h] [-d DOMAIN] [-f FILE] [-o OUTPUT]

    domain2idna - A tool to convert a domain or a file with a list of domain to
    the famous IDNA format.

    optional arguments:
    -h, --help            show this help message and exit
    -d DOMAIN, --domain DOMAIN
                        Set the domain to convert.
    -f FILE, --file FILE  Set the domain to convert.
    -o OUTPUT, --output OUTPUT
                        Set the file where we write the converted domain(s).

    Crafted with ♥ by Nissar Chababy (Funilrys)
