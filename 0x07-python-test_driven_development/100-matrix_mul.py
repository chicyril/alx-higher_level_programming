#!/usr/bin/python3
"""100-matrix_mul Module."""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices.

    Args:
        m_a(list): first matrix.
        m_b(list): second matrix.

    Return:
        list: the resulting matrix.
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    if any(type(row) is not list for row in m_a):
        raise TypeError('m_a must be a list of lists')

    if any(type(row) is not list for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError('m_a can\'t be empty')

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError('m_b can\'t be empty')

    for row in m_a:
        if any(type(el) not in [int, float] for el in row):
            raise TypeError('m_a should contain only integers or floats')

        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')

    for row in m_b:
        if any(type(el) not in [int, float] for el in row):
            raise TypeError('m_b should contain only integers or floats')

        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_bT = [[row[i] for row in m_b] for i in range(len(m_b[0]))]

    result = ([[sum(x * y for x, y in zip(m_a[row], m_bT[col]))
                for col in range(len(m_bT))]
               for row in range(len(m_a))])

    return result
