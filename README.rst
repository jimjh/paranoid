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
...     ("`x` must be a positive integer", lambda p: isinstance(p.x, int) and p.x > 0),
...     ("`y` must be a positive float", lambda p: isinstance(p.y, float) and p.y > 0)
... ])
... @contract.postcondition([
...     ("product must greater than either operand", lambda p, r: r > p.x and r > p.y)
... ])
... def multiply(x, y):
...     return x * int(y)

The preconditions and postconditions will be applied when the function is invoked.

>>> multiply(10, 6.4)
60

To disable contract assertions in production, use ``contract.disable()`` or ``python -O``.

Developing
----------

- Use `six`_ for Py2/3 compatibility.
- Add docs and use doctests. Run them with

  .. code-block:: console

      $ py.test --doctest-glob='*.rst' --doctest-mod

Testing
-------

Run ``tox`` outside any virtualenv.

Inspired by `deadpixi/contracts`_ and `Hillel Wayne`_.

.. _`deadpixi/contracts`: https://github.com/deadpixi/contracts
.. _`Hillel Wayne`: https://us.pycon.org/2018/schedule/presentation/130/
.. _`six`: https://pythonhosted.org/six/
