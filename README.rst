Website rank
=============

sitesiteranklib is a Python library that gets ranks of a website.

Based on [siteranklib](https://pypi.org/project/seolib/)


Example how to use
------------------

.. sourcecode:: python

    >>> import siteranklib
    >>> alexa_rank = siteranklib.get_alexa('http://google.com')
    >>> print alexa_rank
    1

Metrics available
-----------------

- Alexa Ranks (global and USA)

Installation
------------

To install siteranklib open terminal and type:

.. sourcecode:: bash

    $ pip install siteranklib
