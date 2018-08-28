def hello_world():
    return ("Hello, World!")

def sst(a):
    """
    Total sum of squares

    Parameters
    ----------
    a : array_like
        N-dimensional matrix for N-way ANOVA

    Returns
    -------
    out : array_like
        Total sum of squares

    Notes
    -----

    SS_total = sum((Y - mean(Y))**2)

    References
    ----------
    https://en.wikipedia.org/wiki/Total_sum_of_squares
    http://statweb.stanford.edu/~susan/courses/s141/exanova.pdf
    http://www.real-statistics.com/two-way-anova/anova-more-than-two-factors/

    """

    out = np.sum((a - np.mean(a))**2)
    return out

def ssb(a):
    return

def ssw(a):
    return

def ss(a, method='total'):
    """
    Sum of squares.

    Parameters
    ----------

    Returns
    -------
    out : float
        The sum of squares

    Notes
    -----
    Sum of squares is the summation of the square of the differences between
    a vector and the mean value.

    SS = sum((Y - mean(Y))**2)

    The objective in a least squares regression is minimizing the sum of
    squares.
    
    There are different types of SS and different naming conventions, such as
    the total SS (shown above), the SS within a group, the SS between groups,
    the SS from interactions of groups, the explained SS, and the residual SS.

    SS_total = sum((Y - mean(Y))**2)

    SS_between = n * sum((mean(Y, axis=1) - mean(Y))**2)

    References
    ----------

    """
    print("Sum of squares function")

    if method.lower() == 'total':
        return sst()
    elif method.lower() == 'between':
        return ssb()
    elif method.lower() == 'within':
        return ssw()
    else:
        raise LookupError('Method "{}" not found'.format(method))
    return

def anova_one():
    """
    One-way ANOVA test.

    Parameters
    ----------

    Returns
    -------

    Notes
    -----

    References
    ----------

    """

    print("One-way anova")
    a = np.asarray(a)
    n = a.shape[0]
    k = a.shape[1]
    N = n*k

    # Degrees of freedom between
    dfb = k - 1

    # Degrees of freedom within
    dfw = N - k

    # Degrees of freedom total
    dft = N - 1

    # Sum of squares is n*variance
    # Sum of squares between
    #ssb = (np.sum(
    #sum_y_sqrd = 
    #ssw = 
    #sst = 

    return

def anova_two():
    """
    Two-way ANOVA test.

    Parameters
    ----------

    Returns
    -------

    Notes
    -----

    References
    ----------

    """

    print("Two-way anova")
    return

def anova_n():
    """
    N-way ANOVA test.

    Parameters
    ----------

    Returns
    -------

    Notes
    -----

    References
    ----------

    """

    print("N-way anova")
    return

def anova(a, method='n', **kwargs):
    """
    Wrapper function for ANOVA tests. The input is re-directed to a one-way,
    two-way, or n-way ANOVA based on the provided method. By default, a n-way
    ANOVA is performed (since it is the general case).

    Parameters
    ----------

    Returns
    -------

    Notes
    -----

    References
    ----------

    """

    if method.lower() == 'one':
        out = anova_one(a)
        return out
    elif method.lower() == 'two':
        out = anova_two()
        return out
    elif method.lower() == 'n':
        out = anova_n()
        return out
    else:
        raise LookupError('Method "{}" not found'.format(method))
    return
