# University Admission Application

def sorting_applicants(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[3], -x[2]))
    return sorted_results

def sorting_second_priority(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[4], -x[2]))
    return sorted_results

def sorting_third_priority(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[5], -x[2]))
    return sorted_results

def selection_1st_round():
    #global biotech, engineering, chemistry, physics, mathematics
    #global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted
    if len(biotech) <= max_students_per_department:
        biotech_accepted = [candidate for candidate in biotech[0:max_students_per_department]]
        del biotech[0:max_students_per_department]

    if len(engineering) <= max_students_per_department:
        engineering_accepted = [candidate for candidate in engineering[0:max_students_per_department]]
        del engineering[0:max_students_per_department]

    if len(chemistry) <= max_students_per_department:
        chemistry_accepted = [candidate for candidate in chemistry[0:max_students_per_department]]
        del chemistry[0:max_students_per_department]

    if len(physics) <= max_students_per_department:
        physics_accepted = [candidate for candidate in physics[0:max_students_per_department]]
        del physics[0:max_students_per_department]

    if len(mathematics) <= max_students_per_department:
        mathematics_accepted = [candidate for candidate in mathematics[0:max_students_per_department]]
        del mathematics[0:max_students_per_department]

def selection(department_accepted, department):
    global biotech, engineering, chemistry, physics, mathematics
    global max_students_per_department, biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted

    if len(department_accepted) < max_students_per_department:
        vacant_spots = int(max_students_per_department) - int(len(department_accepted)) # difference between max number of spots and occupied
        # if the number of vacant spots is greater than applicants, we will set num of available spots equal to num of applicants
        if vacant_spots > len(department):
            vacant_spots = len(department)
        for counter in range(vacant_spots):
            department_accepted.append(department[counter])
            del department[counter]
    else:
        pass
    return department_accepted

def print_results():
    global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted
    if len(biotech_accepted) > 0:
        print("Biotech")
        for applicant in biotech_accepted:
            print(*applicant[0:3])
        print()

    if len(chemistry_accepted) > 0:
        print("Chemistry")
        for applicant in chemistry_accepted:
            print(*applicant[0:3])
        print()

    if len(engineering_accepted) > 0:
        print("Engineering")
        for applicant in engineering_accepted:
            print(*applicant[0:3])
        print()

    if len(mathematics_accepted) > 0:
        print("Mathematics")
        for applicant in mathematics_accepted:
            print(*applicant[0:3])
        print()

    if len(physics_accepted) > 0:
        print("Physics")
        for applicant in physics_accepted:
            print(*applicant[0:3])
        print()

def split_and_invoke_selection(sorted_selection_list, index):  # + clear as the 1st word in fun name
    global biotech, engineering, chemistry, physics, mathematics
    biotech.clear()
    engineering.clear()
    chemistry.clear()
    physics.clear()
    mathematics.clear()

    # 3 for the 1st priority, 4 for the 2nd and 5 for the 3rd (last) priority
    # SPLIT
    biotech = [person for person in sorted_selection_list if person[index] == "Biotech"]  # index person[4] for the second preference department
    engineering = [person for person in sorted_selection_list if person[index] == "Engineering"]
    chemistry = [person for person in sorted_selection_list if person[index] == "Chemistry"]
    physics = [person for person in sorted_selection_list if person[index] == "Physics"]
    mathematics = [person for person in sorted_selection_list if person[index] == "Mathematics"]

    # select
    selection(biotech_accepted, biotech)
    selection(engineering_accepted, engineering)
    selection(chemistry_accepted, chemistry)
    selection(physics_accepted, physics)
    selection(mathematics_accepted, mathematics)


# step #1 read the file and create the list of applicants as a list of lists
max_students_per_department = int(input())

# initial data import
with open('applicants.txt') as file:
    applicants = [applicant.split() for applicant in file.readlines()]
# step #2 convering GPA str values to float
for value in applicants:
    value[2] = float(value[2])


#PRE SELECTION

biotech = []
chemistry = []
engineering = []
mathematics = []
physics = []

biotech_accepted = []
chemistry_accepted = []
engineering_accepted = []
mathematics_accepted = []
physics_accepted = []

first_round_list = sorting_applicants(applicants)
split_and_invoke_selection(first_round_list, 3)  # index 3 for the 1st priority


if all([len(biotech_accepted) == max_students_per_department, len(engineering_accepted) == max_students_per_department, len(chemistry_accepted) == max_students_per_department, len(physics_accepted) == max_students_per_department, len(mathematics_accepted) == max_students_per_department]):
        print_results()
        exit()  # potentialy useless block as repeating the lines below
else:
    pass




round = 2  # vaid value

#round = 5 # blocking balue

while round <= 3:

    if round == 2:
        second_round_list = [*biotech, *engineering, *chemistry, *physics, *mathematics]
        second_round_list = sorting_second_priority(second_round_list)
        split_and_invoke_selection(second_round_list, 4)  # index 4 for the 2nd priority
        round += 1
        if all([len(biotech_accepted) == max_students_per_department, len(engineering_accepted) == max_students_per_department, len(chemistry_accepted) == max_students_per_department, len(physics_accepted) == max_students_per_department, len(mathematics_accepted) == max_students_per_department]):
            print_results()
            exit()
        else:
            continue

    if round == 3:
        # step #8 obtaining the list for the last tour:
        last_round_list = [*biotech, *engineering, *chemistry, *physics, *mathematics]  # unpacking lists with * asterisk sign
        last_round_list = sorting_third_priority(last_round_list)
        split_and_invoke_selection(second_round_list, 5)  # index 5 for the 3rd (last) priority
        round += 1
        print_results()
        exit()

        #print(len(biotech_accepted) + len(engineering_accepted) + len(chemistry_accepted) + len(physics_accepted) + len(mathematics_accepted))
