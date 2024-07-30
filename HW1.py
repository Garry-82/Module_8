def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as TE:
        return  str(a) + str(b)



print(add_everything_up(44,66))
print(add_everything_up(44,"jgjhgjh"))



