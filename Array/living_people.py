class People:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

def count_living_people(people_list):
    living_count = {}

    for people in people_list:
        # increment count for bith year and death year
        year = people.birth
        if year not in living_count:
            living_count[year] = 0

        living_count[year] += 1

        year = people.death
        if year not in living_count:
            living_count[year] = 0

        living_count[year] += 1

        # decrement count for year following death
        if year + 1 not in living_count:
            living_count[year + 1] = 0

        living_count[year + 1] -= 1

def sort_years(living_years):


def find_max_year_count():
    pass
