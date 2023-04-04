#!/usr/bin/python3
"""Defines a function that does multiplies two matrices using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the result of multilication of two matrices

    Args:
        m_a(list, int/float): first matrice
        m_b(list, int/float): second matrice
    """
    return (np.matmul(m_a, m_b))
