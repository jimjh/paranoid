# ~*~ encoding: utf-8 ~*~
"""inspect - py2/3-compatible inspection"""
# import built-in
from __future__ import absolute_import, print_function
from collections import namedtuple

# import 3rd-party
import six
from six.moves import zip

try:
    # try to use getfullargspec from python3
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec

    def getfullargspec(f):
        result = list(getargspec(f))
        result.extend([[], {}, {}])
        return tuple(result)

__missing = object()  #: unique object to denote missing value


def zip_params(fn, args, kwargs):
    """Takes a function call and label each argument with its name in the argspec.

        >>> def foo(arg0, arg1, k1=u'🛥', *args):
        ...     pass
        >>> zip_params(foo, ('val0', 1, 'leftover'), {'k1': u'boat'})
        Parameters(arg0='val0', arg1=1, k1=u'boat', args=())

    :param fn: function/method
    :param args: list of positional arguments
    :param kwargs: dict of keyword arguments
    """
    # TODO make this work with python3

    defn_args, defn_vargs, defn_kwargs, defaults, _, _, _ = getfullargspec(fn)

    # create a parameter dict with default values
    parameters = {arg_name: __missing for arg_name in defn_args}
    parameters.update(zip(reversed(defn_args), reversed(defaults)))

    # set given positional args, vargs, kwargs
    parameters.update(zip(defn_args, args))
    if defn_vargs is not None:
        parameters[defn_vargs] = tuple(args[len(defn_args):])
    if defn_kwargs is not None:
        parameters[defn_kwargs] = {k: v for k, v in six.iteritems(kwargs) if k not in defn_args}
    parameters.update(kwargs)

    # ensure that we are not missing any positional arguments
    missing = set(k for k, v in six.iteritems(parameters) if v is __missing)
    if len(missing) > 0:
        missing_names = ', '.join(missing)
        error = '{}() requires positional argument(s): {}'.format(fn.__name__, missing_names)
        raise TypeError(error)

    return namedtuple('Parameters', parameters.keys())(**parameters)


__all__ = [zip_params]
