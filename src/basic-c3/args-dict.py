def print_args(**args):
    """
    引数に指定した値を辞書型に変換

    parametars
    ----------
    args : int()
    # args : object()

    #       キー:値の組み合わせ
    returns
    -------
    なし
    """
    print(args)

print_args(a=30, b=50, c=40)
print_args(aa="hoge", bb="fuga")
