
def equal_string(s1, s2, tolerance):

    edit_distance = 0
    for i in range(0, len(s1)):

        if s1[i].upper() != s2[i].upper() and edit_distance >= tolerance:
            return False 

        elif s1[i].upper() != s2[i].upper() and edit_distance < tolerance:
            edit_distance += 1

    return True



def compare_two_string(s1, s2, tolerance):

    # Compare two strings for addition and deletion
    # upto k digits

    if len(s1) == len(s2):
        return equal_string(s1, s2, tolerance)

    # Set s2 is larger
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    s1_iter = iter(s1)
    s2_iter = iter(s2)
    edit_distance = 0
    for _ in range(len(s1)):
        s1_val = next(s1_iter)
        s2_val = next(s2_iter)

        if s1_val.upper() != s2_val.upper() and edit_distance >= tolerance:
            return False  

        elif s1_val.upper() != s2_val.upper() and edit_distance < tolerance:
            while s1_val.upper() != s2_val.upper():
                if edit_distance >= tolerance:
                    return False
                s2_val = next(s2_iter)
                edit_distance += 1


    return True



def test_run():
    print(compare_two_string('abc', 'AC', tolerance = 2))
    print(compare_two_string('abc', 'ADC', tolerance = 2))
    print(compare_two_string('abc', 'A', tolerance = 2))
    print(compare_two_string('abdc', 'AD', tolerance = 2))
    print(compare_two_string('aDbc', 'Ab', tolerance = 2))
    print(compare_two_string('aDbcx', 'Ax', tolerance = 3))


test_run()





