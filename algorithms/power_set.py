from functools import reduce


def get_powerset(A):

    if len(A) == 0:
        return [[]]

    result = [[]]
    for i in A:
        temp = A[:]
        temp.remove(i)
        res = [[i] + x for x in get_powerset(temp)]
        if len(res) > 1 and res[0] < res[1]:
            result.extend(res)
        elif len(res) <= 1:
            result.extend(res)

    # result.append([A])

    return result

result_hash = {}

testdata = get_powerset([4,5,6])
# print([list(x) for x in set(tuple(x) for x in testdata)])


# def powerset(s):
#     x = len(s)

#     # gets multiples of 2^n
#     masks = [1 << i for i in range(x)]
#     # print(masks)

#     # loop till 2^n
#     for i in range(1 << x):
#         yield [ss for mask, ss in zip(masks, s) if i & mask]

# # print(list(powerset([4,2,3])))
# print(list(powerset(['a','b','c'])))

def powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])

print(powerset([2,3,4]))








