# ~*~ encoding: utf-8 ~*~
"""Contracts for functions."""
# import built-in
from __future__ import absolute_import, print_function

# import 3rd-party
import wrapt

# import package local
from .invocation import zip_params

# TODO more docs, mypy
# TODO automatically check types from annotations


class Contract(object):
    """
    Assertions are disabled by default, and are also disabled when python is started
    with optimization flags _e.g._ ``python -O``.
    """

    def __init__(self):
        self.__enabled = False

    def enable(self):
        """Enables contract assertions.

        Note that this does not enable assertions if python is started with ``-O``.
        """
        self.__enabled = True

    def disable(self):
        """Disables contract assertions."""
        self.__enabled = False

    def enabled(self):
        return self.__enabled and __debug__

    def precondition(self, conditions):
        @wrapt.decorator(enabled=self.enabled)
        def decorator(fn, inst, args, kwargs):
            params = zip_params(fn, args, kwargs)
            for description, predicate in conditions:
                assert predicate(params), description
            return fn(*args, **kwargs)
        return decorator

    def postcondition(self, conditions):
        @wrapt.decorator(enabled=self.enabled)
        def decorator(fn, inst, args, kwargs):
            params = zip_params(fn, args, kwargs)
            ret = fn(*args, **kwargs)
            for description, predicate in conditions:
                assert predicate(params, ret), description
            return ret
        return decorator


contract = Contract()
