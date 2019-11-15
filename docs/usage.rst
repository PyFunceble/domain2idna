Usage
=====

As a Python module
------------------

Here's an example which show us how domain2idna can be used a python module.

::

    #!/usr/bin/env python3

    """
    This module uses domains2idna to convert a given domain.

    Author:
        Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

    Contributors:
        Let's contribute to this example!!

    Repository:
        https://github.com/PyFunceble/domain2idna
    """
    from domain2idna import get as domain2idna

    DOMAINS = [
        "bittréẋ.com", "bịllogram.com", "coinbȧse.com", "cryptopiạ.com", "cṙyptopia.com"
    ]

    # The following return the result of the whole list.
    print("UTF-8 domains: %s" % DOMAINS)
    print("Converted domains: %s" % domain2idna(DOMAINS))

    # The following return the result of only one element.
    print("UTF-8 domain: %s" % DOMAINS[0])
    print( "Converted domain: %s" % domain2idna(DOMAINS[0]))

From a terminal
---------------

Here is the list of available command when calling :code:`domain2idna` from a terminal.

::

    usage: domain2idna [-h] [-d DOMAIN] [-e ENCODING] [-f FILE] [-o OUTPUT] [-v]

    domain2idna - The tool to convert a domain or a file with a list of domain to
    the famous IDNA format.

    optional arguments:
        -h, --help            show this help message and exit
        -d DOMAIN, --domain DOMAIN
                                Set the domain to convert.
        -e ENCODING, --encoding ENCODING
                                Set the encoding to use.
        -f FILE, --file FILE  Sets the file to read to get the domain(s) to convert.
        -o OUTPUT, --output OUTPUT
                                Sets the file where we write the converted domain(s).
        -v, --version         show program's version number and exit

    Crafted with ♥ by Nissar Chababy (Funilrys)