#!/usr/bin/python3
"""101-lazy_matrix_mul Module."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply the elements of 2 matrices.

    Args:
        m_a: matrix a
        m_b: matrix b

    Return:
        result of the multiplication
    """
    return (np.matmul(m_a, m_b))
