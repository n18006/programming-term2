def sumargs(*args):
    """
    引数に指定された値をすべて合計する

    parametars
    ----------
    args : int()
        合計したい数値(複数指定可能)
    returns
    -------
    int
        合計された値
    """

    v = 0
    for n in args:
        v += n
    return v

print(sumargs(1, 2, 3))
print(sumargs(1, 2, 3, 4, 5))
print(sumargs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

