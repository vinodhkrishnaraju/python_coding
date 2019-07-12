def find_xor_sum(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num
    return xor_sum


def find_missing(full_set, partial_set):

    # return list(set(full_set) - set(partial_set))

    partial_dict = {}
    agg = []
    for i in partial_set:
        partial_dict[i] = 1

    for i in full_set:
        if i not in partial_dict.keys():
            agg += [i]
    return agg

# print(find_xor_sum([10,12,2,3],[10,3]))
print(find_missing([10,12,2,3],[10,3]))