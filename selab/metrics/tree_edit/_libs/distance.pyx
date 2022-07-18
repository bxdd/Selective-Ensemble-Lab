# cython: cdivision=True
# cython: boundscheck=False
# cython: wraparound=False
# cython: nonecheck=False
# cython: language_level=3
# distutils: language=c++

cimport cython
import numpy as np
cimport numpy as np
np.import_array()

from cpython cimport array
import array

from numpy import uint8 as DTYPE
from numpy import float64 as DOUBLE

from libcpp.queue cimport queue
from libcpp.stack cimport stack

from ....ensemble.forest.tree._libs._tree cimport (
    DTYPE_t,
    DOUBLE_t,
    SIZE_t,
    Tree
)

cdef SIZE_t _TREE_LEAF = -1
cdef SIZE_t _TREE_UNDEFINED = -1

cdef np.ndarray preprocess_tree(
    const SIZE_t node_count,
    const SIZE_t [:] feature, 
    const SIZE_t [:] children_left, 
    const SIZE_t [:] children_right, 
    ):

    cdef SIZE_t[3] gogo = array.array('i', [1, 2, 3])

    cdef SIZE_t root_id = 0
    #cdef array.array nodes_fa = array.array() 
    cdef np.ndarray[SIZE_t, ndim=1] nodes_fa = np.empty((node_count, ), dtype=np.intp)

    #with nogil:

    return nodes_fa

cpdef np.ndarray test_queue(
    const SIZE_t node_count,
    const SIZE_t [:] feature, 
    const SIZE_t [:] children_left, 
    const SIZE_t [:] children_right
    ):
    cdef queue [SIZE_t] que = queue [SIZE_t] ()
    que.push(1233)
    cdef array.array gogo = array.array('i', [1, 2, 3])
    print(1)
    return preprocess_tree(node_count, feature, children_left, children_right)

cdef class DisTree:
    cdef Tree decision_tree
    cdef lmds
    cdef keyroots
    def __cinit__(self, Tree decision_tree):
        self.decision_tree = decision_tree
        cdef SIZE_t [:] x = self.preprocess_tree(
            node_count=decision_tree.node_count,
            feature=decision_tree.feature,
            children_left=decision_tree.children_left,
            children_right=decision_tree.children_right
        )
        print(len(x), decision_tree.node_count)

    cdef SIZE_t [:] preprocess_tree(
        self,
        const SIZE_t node_count,
        const SIZE_t [:] feature, 
        const SIZE_t [:] children_left, 
        const SIZE_t [:] children_right, 
    ):
        cdef SIZE_t root_id = 0
        #cdef array.array nodes_fa = array.array() 
        cdef SIZE_t[node_count] tree_nodes = np.empty((node_count, ), dtype=np.intp)
        cdef SIZE_t[node_count] nodes_fa = np.empty((node_count, ), dtype=np.intp)
        

        cdef stack [SIZE_t] now_stack = stack [SIZE_t] ()
        cdef stack [SIZE_t] fa_stack = stack [SIZE_t] ()
        now_stack.push(root_id)
        fa_stack.push(-1)

        cdef SIZE_t internal_count = 0
        cdef SIZE_t new_node, new_fa
        cdef SIZE_t left_node, right_node
        while now_stack.empty() == False:
            new_node, new_fa = now_stack.top(), fa_stack.top()
            now_stack.pop()
            fa_stack.pop()
            if feature[new_node] == _TREE_UNDEFINED:
                continue
            tree_nodes[internal_count] = new_node
            nodes_fa[internal_count] = new_fa
            
            left_node = children_left[new_node]
            right_node = children_right[new_node]
            if left_node != _TREE_LEAF:
                now_stack.push(left_node)
                fa_stack.push(internal_count)
            if right_node != _TREE_LEAF:
                now_stack.push(right_node)
                fa_stack.push(internal_count)
            internal_count = internal_count + 1
        
        for idx in range(len(tree_nodes)):
            #while nodes_fa
            print(idx)
        return nodes_fa