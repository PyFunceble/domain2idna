As a Python module
==================

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
        https://github.com/funilrys/domain2idna
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