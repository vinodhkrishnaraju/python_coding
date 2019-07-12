def get_permutations(string):

    # Generate all permutations of the input string
    if len(string) == 0:
        return []


    if len(string) == 1:
        print([string])
        return [string]

    
    result = []
    for i in range(len(string)):
        m = string[i]
        
        temp = string[:i] + string[i+1:]
        
        # result += [ [m] + [p for p in get_permutations(temp) ] ]
        result.extend([ [m] + p for p in get_permutations(temp) ])
      
    # print(result)      
    return result


print(get_permutations([1,2,3]))