def two_sum(num_list, k):

    num_list = list(set(num_list))
    agg = []
    for num in num_list:

        complement = k - num

        if complement in num_list:

            agg += [[num, complement]]


    vagg = []
    for item in agg:
        if sorted(item) not in vagg:
            vagg += [sorted(item)]
    
    return vagg

print(two_sum([1,3,2,4,5,0], 5))
