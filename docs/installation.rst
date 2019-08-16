Requirements
============

Here is the list of requirements:

-   Python >= 3.6.2  && Python < 4
-   :code:`colorama`

Python >= 3.6.2  && Python < 4
------------------------------

As we want to give a priority to Python 3, Python 3 is required. The specification `>= 3.6.2` is because
this project is tested which all version `>=3.6.2`

colorama
--------

As we want to add some coloration, we choose :code:`colorama` for the job as it offers a portable awesome solution.

Get and install domain2idna
===========================

Using :code:`pip`
-----------------

Choose your repository, install and enjoy domain2idna!

From PyPi
^^^^^^^^^

::

   $ pip3 install --user domain2idna

.. note::
   We recommend the :code:`--user` flag which installs the required dependencies at the user level. More information about it can be found on `pip documentation`_.
.. warning::
   We do not recommend the :code:`--user` flag when using :code:`domain2idna` into containers like - for example - Travis CI.

From GitHub
^^^^^^^^^^^

::

   $ pip3 install --user git+https://github.com/funilrys/domain2idna.git@master#egg=domain2idna

.. note::
   We recommend the :code:`--user` flag which installs the required dependencies at the user level. More information about it can be found on `pip documentation`_.
.. warning::
   We do not recommend the :code:`--user` flag when using :code:`domain2idna` into containers like - for example - Travis CI.

.. _pip documentation: https://pip.pypa.io/en/stable/reference/pip_install/?highlight=--user#cmdoption-user


Pure Python method
------------------

Execute the following and enjoy domain2idna!

We clone the repository.
::

   $ git clone https://github.com/funilrys/domain2idna.git


We move to the cloned directory.

::

   $ cd domain2idna

We test the package before installating.

::

   $ python3 setup.py test

We install domain2idna.

::

   $ python3 setup.py install --user

.. note::
   We recommend the :code:`--user` flag which installs the required dependencies at the user level. More information about it can be found on `pip documentation`_.

.. warning::
   We do not recommend the :code:`--user` flag when using :code:`domain2idna` into containers like - for example - Travis CI.

First steps
===========


Make sure that you can run the following without any issue and enjoy domain2idna!!

::

   $ domain2idna --version
