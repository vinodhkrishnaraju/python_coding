

def change_possibilities(amount, denominations, partial_list, result, s):

    # # Calculate the number of ways to make change
    # if amount == 0:
    #   result.append(partial_list)
    #   return

    # if amount < 0:
    #   return
    
    # if len(denominations) == 0:
    #     return

    
    # last_coin = list(denominations)[-1]
    # without_last_coin = set(list(denominations)[:-1])
    
    # # including coin possible ways
    # # excluding coin how many possible ways
    # change_possibilities(amount-last_coin, denominations, partial_list + [last_coin], result) 
    # change_possibilities(amount, without_last_coin, partial_list, result)


    ## solution 2
    # print_all_sum_rec(target, current_sum, start, output, result):
    if amount == 0:
      result.append(copy.copy(partial_list))

    if amount < 0:
      return

    n = len(denominations)
    for i in range(s, n):
      value = denominations[i]
      change_possibilities(amount - value, denominations, partial_list + [value], result, i)
      

partial_list = []
result = []
denominations = [2,3,6,7]
amount = 7
start = 0
change_possibilities(amount, denominations, partial_list, result, start)
print(4)
print(result)