"""
DSC 20 Fall 2023, Discussion 01
Name: TODO
PID: TODO
Source: TODO

****************************** Example ******************************
DSC 20 Fall 2023, Discussion 01
Name: Marina Langlois
PID: A12345678
Source: Lecture 1 Slides, https://www.w3schools.com/python/ref_string_join.asp
"""

# Question 1
def add_connection(num_range):
    """
    Inserts "-" between each number in the range of 0 to num_range (inclusive).
    If a number <= 0 is passed, return '0'.

    Args:
        num_range: an integer that determines the range of the result.

    Returns:
        '0' if num_range <= 0. 
        range from 0-num_range with "-" inserted between each number otherwise.
        

    >>> add_connection(0)
    '0'
    >>> add_connection(-1)
    '0'
    >>> add_connection(4)
    '0-1-2-3-4'
    """
    if num_range <= 0:
        return '0'
    output = list(range(num_range+1))
    for i in output:
        output[i] = str(i)
    return '-'.join(output)
