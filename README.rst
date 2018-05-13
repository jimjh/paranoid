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
...     ("`x` must be an integer", lambda p: isinstance(p.x, int)),
...     ("`y` must be a float", lambda p: isinstance(p.y, float))
... ])
... @contract.postcondition([
...     ("product must greater than either operand", lambda p, r: r > p.x and r > p.y)
... ])
... def multiply(x, y):
...     return x * int(y)

The preconditions and postconditions will be applied when the function is invoked.

>>> multiply(10, 6)
Traceback (most recent call last):
    ...
AssertionError: `y` must be a float

To disable contract assertions in production, use ``contract.disable()`` or ``python -O``.

Developing
----------

- Use `six`_ for Py2/3 compatibility.
- Add docs and use doctests. Run them with

  .. code-block:: console

      $ pytest --doctest-glob='*.rst' --doctest-mod

Testing
-------

Run ``tox`` outside any virtualenv.

Appendix
--------

Inspired by `deadpixi/contracts`_ and `Hillel Wayne`_.

Differences:

- Provides a shorter stack trace on failure, since each decorator takes multiple conditions, instead of wrapping the target function once per condition.
- Uses `wrapt`_ instead of functools for decorators.
- Provides enable/disable methods, in addition to using ``__debug__``, so you don't have to disable assertions across the entire virtualenv.
- Allows you to instantiate isolated contracts that can be enabled/disabled independently.

I need the latter 2 behaviors because I work with a monolith.

.. _`deadpixi/contracts`: https://github.com/deadpixi/contracts
.. _`Hillel Wayne`: https://us.pycon.org/2018/schedule/presentation/130/
.. _`six`: https://pythonhosted.org/six/
.. _`wrapt`: https://wrapt.readthedocs.io/
