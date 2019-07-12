def reverse_string(x):
    
    # return x[::-1]
    c = ''
    for i in x:
        c = i + c
    return c

# print(reverse_string('abc'))


def reverse_recursion(x):

    if len(x) == 0:
        return x
    else:
        return reverse_recursion(x[1:]) + x[0]


# print(reverse_recursion('abghy'))


