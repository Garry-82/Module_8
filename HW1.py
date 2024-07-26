def add_everything_up(a, b):
    try:
        a + b
        return a + b
    except TypeError as TE:
        return  str(a) + str(b)



print(add_everything_up(44,'dfgdfg'))



