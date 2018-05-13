========
paranoid
========

Pragmatic Contracts for Python.

.. code-block:: python

    from paranoid import contract
    import six

    contract.enable()
    # Use ``contract.disable()`` or ``python -O`` to disable

    @contract.precondition([
        ("`x` must be an integer", lambda params: isinstance(params.x, int)),
        ("`y` must be an float", lambda params: isinstance(params.y, float))
    ])
    @contract.postcondition([
        ("return value must be a unicode string", lambda s: isinstance(s, six.text_type))
    ])
    def my_function(x, y, z='a', *args, **kwargs):
        """docs."""
        return u'x'

Inspired by `deadpixi/contracts`_ and `Hillel Wayne`_.

.. _`deadpixi/contracts`: https://github.com/deadpixi/contracts
.. _`Hillel Wayne`: https://us.pycon.org/2018/schedule/presentation/130/
