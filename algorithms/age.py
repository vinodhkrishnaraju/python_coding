def getpopulation(persons):
    first_birth = getminbirth(persons)
    last_birth = getmaxbirth(persons)
    deltas = get_deltas(persons, first_birth, last_birth)
    max_age = getmaxpop(deltas)


def get_deltas(persons, first_birth, last_birth):
    
    n = last_birth - first_birth
    deltas = [0] * n
    for person in persons:
        birth_index = persons.birth - first_birth
        death_index = last_birth - persons.death
        deltas[birth_index] += 1
        deltas[death_index] -= 1
    return deltas

def getmaxpop(deltas):

    max_population = 0
    running_population = 0
    output_year = 0

    for i in range(deltas):
        running_population += deltas[i]
        if running_population>max_population:
            max_population = running_population
            output_year = deltas[i]



    return output_year


def getminbirth(persons):
    pass

def getmaxbirth(persons):
    pass