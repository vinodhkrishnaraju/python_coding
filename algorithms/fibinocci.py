def fibinocci(nterms):

    # 0 1 1 2 3 5 8 13
    start = 2
    fibi = []
    if nterms < 1:
        fibi.append(0)
    elif nterms > 1:
        fibi.append(0)
        fibi.append(1)

    while start < nterms:
        fibi.append(fibi[start-1] + fibi[start-2])
        start += 1


    return fibi



# print(fibinocci(10))


def recursive_fibinocci(nterms):

    result = []
    memo = {}
    def recurse(nterms):
        if nterms == 0 or nterms == 1:
            return nterms

        # print(recurse(nterms - 2) + recurse(nterms - 1))
        if nterms in memo.get(nterms) 
        return (recurse(nterms - 2) + recurse(nterms - 1))
    for i in range(nterms):
        result.append(recurse(i))
    # print(recurse(nterms))
    return result

print(recursive_fibinocci(10))