def hello_world():
    return ("Hello, World!")

def ss():
    """
    Sum of squares.

    Parameters
    ----------

    Returns
    -------

    Notes
    -----

    References
    ----------

    """
    print("Sum of squares function")
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
    ssb = (np.sum(
    sum_y_sqrd = 
    ssw = 
    sst = 

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
