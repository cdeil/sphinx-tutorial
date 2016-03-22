"""
Python in Astronomy 2016 is the second iteration of the Python in Astronomy
conference series.

This is the docstring for the pyastro module, this gets included as the
description for the module.
"""

import numpy as np


def times(a, b):
    """
    Multiply a by b.

    Parameters
    ----------

    a : `numpy.ndarray`
        Array one.

    b : `numpy.ndarray`
        Array two

    Returns
    -------

    result : `numpy.ndarray`
        ``a`` multiplied by ``b``
    """

    return np.multipy(a, b)


class PyAstro(object):
    """
    This is a class docstring, here you must describe the parameters for the
    creation of the class, which is normally the signature of the ``__init__``
    method.

    Parameters
    ----------
    awesomeness_level : `int`
        How awesome is pyastro16??!

    day : `int`
        Day of the conference. Defaults to 1.

    Attributes
    ----------

    awesomeness_level: `int`
        How awesome is this class attributes?! You can document attributes that
        are not properties here.
    """

    def __init__(self, awesomeness_level, day=1):
        """
        This docstring is not used, because it is for a hidden method.
        """
        self.awesomeness_level = awesomeness_level
        self._day = day

    @property
    def day(self):
        """
        Day of the conference.

        Properties are automatically documented as attributes
        """
        return self._day


class PyAstro16(PyAstro):
    """
    The 2016 edition of the python in astronomy conference.

    """
    __doc__ += PyAstro.__doc__
