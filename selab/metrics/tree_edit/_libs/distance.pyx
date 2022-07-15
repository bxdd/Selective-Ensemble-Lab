# cython: cdivision=True
# cython: boundscheck=False
# cython: wraparound=False
# cython: nonecheck=False
# cython: language_level=3


cimport cython
import numpy as np
cimport numpy as np
np.import_array()

from numpy import uint8 as DTYPE
from numpy import float64 as DOUBLE

from ....ensemble.forest.tree._libs._tree cimport DTYPE_t, DOUBLE_t, SIZE_t

cpdef np.ndarray preprocess_tree(
    const SIZE_t [:] feature, 
    const SIZE_t [:] children_left, 
    const SIZE_t [:] children_right, 
    np.ndarray[DOUBLE_t, ndim=2] value
    ):
    
    