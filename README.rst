========
paranoid
========

.. image:: https://travis-ci.org/jimjh/paranoid.svg?branch=master
    :target: https://travis-ci.org/jimjh/paranoid

Pragmatic Contracts for Python.

Basic Usage
-----------

Import and enable ``paranoid.contract``:

    >>> from paranoid import contract
    >>> contract.enable()

Then, add preconditions and postconditions by defining predicates on each argument and on
the return value.

    >>> @contract.precondition([
    ...     ("`x` must be an integer", lambda params: isinstance(params.x, int)),
    ...     ("`y` must be an float", lambda params: isinstance(params.y, float))
    ... ])
    ... @contract.postcondition([
    ...     ("return value must be a binary string", lambda ret: isinstance(ret, bytes))
    ... ])
    ... def my_function(x, y, z='a', *args, **kwargs):
    ...     return b'\xf0\x9f\x9a\x80'

The preconditions and postconditions will be applied when the function is invoked.

    >>> my_function(10, 6.4)
    '\xf0\x9f\x9a\x80'

To disable contract assertions in production, use ``contract.disable()`` or ``python -O``.

Developing
----------

Testing
-------

Run ``tox`` outside any virtualenv.

Inspired by `deadpixi/contracts`_ and `Hillel Wayne`_.

.. _`deadpixi/contracts`: https://github.com/deadpixi/contracts
.. _`Hillel Wayne`: https://us.pycon.org/2018/schedule/presentation/130/
