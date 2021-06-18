# University Admission Application
#total_number_of_applicants = int(input())
#spots_availiable = int(input())
#applicants_list = [input().split() for aplicant in range(total_number_of_applicants)]

#for value in applicants_list:
#    value[2] = float(value[2])

def sorting_applicants(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[3], -x[2]))
    return sorted_results

def sorting_second_priority(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[4], -x[2]))
    return sorted_results


def selection_1st_round():
    global biotech, engineering, chemistry, physics, mathematics
    global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted
    if len(biotech) <= max_students_per_department:
        biotech_accepted = biotech
        biotech.clear()
    else:
        biotech_accepted = [candidate for candidate in biotech[0:max_students_per_department]]
        del biotech[0:max_students_per_department]

    if len(engineering) <= max_students_per_department:
        engineering_accepted = engineering
        engineering.clear()
    else:
        engineering_accepted = [candidate for candidate in engineering[0:max_students_per_department]]
        del engineering[0:max_students_per_department]

    if len(chemistry) <= max_students_per_department:
        chemistry_accepted = chemistry
        chemistry.clear()
    else:
        chemistry_accepted = [candidate for candidate in chemistry[0:max_students_per_department]]
        del chemistry[0:max_students_per_department]

    if len(physics) <= max_students_per_department:
        physics_accepted = physics
        physics.clear()
    else:
        physics_accepted = [candidate for candidate in physics[0:max_students_per_department]]
        del physics[0:max_students_per_department]

    if len(mathematics) <= max_students_per_department:
        mathematics_accepted = mathematics
        mathematics.clear()
    else:
        mathematics_accepted = [candidate for candidate in mathematics[0:max_students_per_department]]
        del mathematics[0:max_students_per_department]

def selection_2st_round():
    global biotech, engineering, chemistry, physics, mathematics
    global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted

    # comment out (our move to a separate backup file all blocks after one and make this function called 5 times instead)
    # in can also be a function for the 3rd round check after proper sorting

    if len(biotech_accepted) < max_students_per_department:
        #checking number of vacant spots
        vacant_spots = max_students_per_department - len(biotech_accepted)
        # if the number of vacant spots is bigger than candidates, we will set num of available spots equal to num of candidates
        if vacant_spots > len(biotech):
            vacant_spots = len(biotech)
        for candidate_form_2nd_tour in range(vacant_spots):
            biotech_accepted.append(biotech[candidate_form_2nd_tour])
            del biotech[0:vacant_spots]
    else:
        pass

    if len(engineering_accepted) < max_students_per_department:
        vacant_spots = max_students_per_department - len(engineering_accepted)
        # if the number of vacant spots is bigger than candidates, we will set num of available spots equal to num of candidates
        if vacant_spots > len(engineering):
            vacant_spots = len(engineering)
        for candidate_form_2nd_tour in range(vacant_spots):
            engineering_accepted.append(engineering[candidate_form_2nd_tour])
            del engineering[0:vacant_spots]
    else:
        pass

    if len(chemistry_accepted) < max_students_per_department:
        vacant_spots = max_students_per_department - len(chemistry_accepted)
        # if the number of vacant spots is bigger than candidates, we will set num of available spots equal to num of candidates
        if vacant_spots > len(chemistry):
            vacant_spots = len(chemistry)
        for candidate_form_2nd_tour in range(vacant_spots):
            chemistry_accepted.append(chemistry[candidate_form_2nd_tour])
            del chemistry[0:vacant_spots]
    else:
        pass

    if len(physics_accepted) < max_students_per_department:
        vacant_spots = max_students_per_department - len(physics_accepted)
        # if the number of vacant spots is bigger than candidates, we will set num of available spots equal to num of candidates
        if vacant_spots > len(physics):
            vacant_spots = len(physics)
        for candidate_form_2nd_tour in range(vacant_spots):
            physics_accepted.append(engineering[physics_form_2nd_tour])
            del physics[0:vacant_spots]
    else:
        pass

    if len(mathematics_accepted) < max_students_per_department:
        # if the number of vacant spots is bigger than candidates, we will set num of available spots equal to num of candidates
        if vacant_spots > len(mathematics):
            vacant_spots = len(mathematics)
        vacant_spots = max_students_per_department - len(mathematics_accepted)
        for candidate_form_2nd_tour in range(vacant_spots):
            mathematics_accepted.append(mathematics[candidate_form_2nd_tour])
            del mathematics[0:vacant_spots]
    else:
        pass

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


#admitted = admission_process(applicants_list)

#print("Successful applicants: ")
#for applicant in range(spots_availiable):
#   print(*admitted[applicant][0:2])


# step #1 read the file and create the list of applicants as a list of lists
max_students_per_department = int(input())
best_candidates = max_students_per_department
with open('applicants.txt') as file:
    applicants = [applicant.split() for applicant in file.readlines()]
# step #2 convering GPA str values to float
for value in applicants:
    value[2] = float(value[2])

# step #3 sort out applicants using sorting algorithm
sorted_applicants1 = sorting_applicants(applicants)

#print("len of the sorted_applicants1 list now", len(sorted_applicants1))
#print(sorted_applicants)

# step #4 creating empty lists of candidates for each of departments and splitting into 5 lists:

biotech = [person for person in sorted_applicants1 if person[3] == "Biotech"]
engineering = [person for person in sorted_applicants1 if person[3] == "Engineering"]
chemistry = [person for person in sorted_applicants1 if person[3] == "Chemistry"]
physics = [person for person in sorted_applicants1 if person[3] == "Physics"]
mathematics = [person for person in sorted_applicants1 if person[3] == "Mathematics"]

# step #5 clearing out original list after splitting values into individual lists
sorted_applicants1.clear()  # clearing out original list after splitting.

# step #6 the first round of selection
# correct order of input is below
biotech_accepted = []
chemistry_accepted = []
engineering_accepted = []
mathematics_accepted = []
physics_accepted = []


#step #7 executing 1st round of selection, if all spots fulfilled - stop, else - other rounds

selection_1st_round()


# print results, declare function
if all([len(biotech_accepted) == max_students_per_department, len(engineering_accepted) == max_students_per_department, len(chemistry_accepted) == max_students_per_department, len(physics_accepted) == max_students_per_department, len(mathematics_accepted) == max_students_per_department]):
    print_results()
    exit()
else:
    print("not all spots fulfilled TEST string")
    print("LEN of lists after 1st round", len(biotech_accepted), len(engineering_accepted), len(chemistry_accepted), len(physics_accepted), len(mathematics_accepted))
    pass

# step #8 obtaining the list for the second tour:
applicants_2nd_tour = [*biotech, *engineering, *chemistry, *physics, *mathematics]  # unpacking lists with * asterisk sign
applicants_2nd_tour = sorting_second_priority(applicants_2nd_tour)

# clearing individual lists:
biotech.clear()
engineering.clear()
chemistry.clear()
physics.clear()
mathematics.clear()

# segregating into individual lists based on the second priority for the second time:
biotech = [person for person in sorted_applicants1 if person[4] == "Biotech"]  # index person[4] for the second preference department
engineering = [person for person in sorted_applicants1 if person[4] == "Engineering"]
chemistry = [person for person in sorted_applicants1 if person[4] == "Chemistry"]
physics = [person for person in sorted_applicants1 if person[4] == "Physics"]
mathematics = [person for person in sorted_applicants1 if person[4] == "Mathematics"]



# step #9 the Second Round of Selection:
selection_2st_round()

print("LEN of lists after 2st round", len(biotech_accepted), len(engineering_accepted), len(chemistry_accepted), len(physics_accepted), len(mathematics_accepted))
