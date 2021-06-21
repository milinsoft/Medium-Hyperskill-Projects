# University Admission Application
def selection(department_accepted, department):

    if len(department_accepted) < max_students_per_department:
        vacant_spots = int(max_students_per_department) - int(len(department_accepted))  # difference between max number of spots and occupied
        # if the number of vacant spots is greater than applicants, we will set num of available spots equal to num of applicants
        if vacant_spots > len(department):
            vacant_spots = len(department)
        department_accepted.extend(department[0:vacant_spots])
        del department[0:vacant_spots]
    else:
        pass
    return department_accepted


def print_results():
    global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted
    biotech_accepted = sorted(biotech_accepted, key=lambda x: (-(x[3] + x[2]) / 2, x[0], x[1]))  # -x[3] for biology -x[2] for physics | (x[3] + x[2]) / 2 - for print
    engineering_accepted = sorted(engineering_accepted, key=lambda x: (-(x[5]+x[4]) / 2, x[0], x[1]))  # DONE -x[5] for computer science, -x[4] for math | (x[5]+x[4]) / 2 - for print
    chemistry_accepted = sorted(chemistry_accepted, key=lambda x: (-x[3], x[0], x[1]))  # DONE -x[3] for chemistry; NO CHANGES REQUIRED (STAGE 6)
    physics_accepted = sorted(physics_accepted, key=lambda x: (-(x[2] + x[4]) / 2, x[0], x[1]))  # DONE -x[2] for physics -x[4] for math | x[2] + x[4] / 2 - for print
    mathematics_accepted = sorted(mathematics_accepted, key=lambda x: (-x[4], x[0], x[1]))  # DONE -x[4] for math; NO CHANGES REQUIRED (STAGE 6)

    # write results into individual files

    with open('biotech.txt', 'w') as biotech_file:
        for applicant in biotech_accepted:
            f1 = [applicant[0], applicant[1], str((applicant[2] + applicant[3]) / 2)]
            f1 = " ".join(f1)
            print(f1)
            biotech_file.write(f1 + '\n')

    with open('chemistry.txt', 'w') as chemistry_file:
        for applicant in chemistry_accepted:
            f2 = [applicant[0], applicant[1], str(applicant[3])]
            f2 = " ".join(f2)
            chemistry_file.write(f2 + '\n')

    with open('engineering.txt', 'w') as engineering_file:
        for applicant in engineering_accepted:
            f3 = [applicant[0], applicant[1], str((applicant[5] + applicant[4]) / 2)]
            f3 = " ".join(f3)
            engineering_file.write(f3 + '\n')

    with open('mathematics.txt', 'w') as mathematics_file:
        for applicant in mathematics_accepted:
            f4 = [applicant[0], applicant[1], str(applicant[4])]
            f4 = " ".join(f4)
            mathematics_file.write(f4 + '\n')

    with open('physics.txt', 'w') as physics_file:
        for applicant in physics_accepted:
            f5 = [applicant[0], applicant[1], str((applicant[2] + applicant[4]) / 2)]
            f5 = " ".join(f5)
            physics_file.write(f5 + '\n')

    if len(biotech_accepted) > 0:
        print("Biotech")
        for applicant in biotech_accepted:
            print(*applicant[0:2], (applicant[3] + applicant[2]) / 2)  # updated index for chemistry exam
        print()

    if len(chemistry_accepted) > 0:
        print("Chemistry")
        for applicant in chemistry_accepted:
            print(*applicant[0:2], applicant[3])  # updated index for chemistry exam
        print()

    if len(engineering_accepted) > 0:
        print("Engineering")
        for applicant in engineering_accepted:
            print(*applicant[0:2], (applicant[5] + applicant[4]) / 2)
        print()

    if len(mathematics_accepted) > 0:
        print("Mathematics")
        for applicant in mathematics_accepted:
            print(*applicant[0:2], applicant[4])  # updated index for math exam
        print()

    if len(physics_accepted) > 0:
        print("Physics")
        for applicant in physics_accepted:
            print(*applicant[0:2], (applicant[2] + applicant[4]) / 2)  # updated index for physics exam
        print()


def split_and_invoke_selection(sorted_selection_list, index):  # + clear as the 1st word in fun name
    global biotech, engineering, chemistry, physics, mathematics
    global biotech_accepted, engineering_accepted, chemistry_accepted, physics_accepted, mathematics_accepted
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

    # sorting:
    biotech = sorted(biotech, key=lambda x: (-(x[3] + x[2]) / 2, x[0], x[1]))  # -x[3] for biology -x[2] for physics | (x[3] + x[2]) / 2 - for print
    engineering = sorted(engineering, key=lambda x: (-(x[5]+x[4]) / 2, x[0], x[1]))  # DONE -x[5] for computer science, -x[4] for math | (x[5]+x[4]) / 2 - for print
    chemistry = sorted(chemistry, key=lambda x: (-x[3], x[0], x[1]))  # DONE -x[3] for chemistry; NO CHANGES REQUIRED (STAGE 6)
    physics = sorted(physics, key=lambda x: (-(x[2] + x[4]) / 2, x[0], x[1]))  # DONE -x[2] for physics -x[4] for math | x[2] + x[4] / 2 - for print
    mathematics = sorted(mathematics, key=lambda x: (-x[4], x[0], x[1]))  # DONE -x[4] for math; NO CHANGES REQUIRED (STAGE 6)

    # select
    selection(biotech_accepted, biotech)
    selection(engineering_accepted, engineering)
    selection(chemistry_accepted, chemistry)
    selection(physics_accepted, physics)
    selection(mathematics_accepted, mathematics)


# step #1 read the file and create the list of applicants as a list of lists
max_students_per_department = int(input())

# initial data import
with open('applicants.txt', 'r') as file:
    applicants = [applicant.split() for applicant in file.readlines()]
# step #2 converting GPA str values to float
for value in applicants:
    for i in range(2, 6):
        value[i] = float(value[i])


# PRE SELECTION

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


selection_round = 1  # default value


while selection_round <= 3:
    if selection_round == 1:
        first_round_list = [applicant for applicant in applicants]
        split_and_invoke_selection(first_round_list, 6)  # index 3 for the 1st priority
        selection_round += 1
        del first_round_list  # deleting from memory
        if all([len(biotech_accepted) == max_students_per_department, len(engineering_accepted) == max_students_per_department, len(chemistry_accepted) == max_students_per_department, len(physics_accepted) == max_students_per_department, len(mathematics_accepted) == max_students_per_department]):
            print_results()
            exit()  # potentially useless block as repeating the lines below
        else:
            pass

    if selection_round == 2:
        second_round_list = [*biotech, *engineering, *chemistry, *physics, *mathematics]
        # second_round_list = sorting_second_priority(second_round_list)
        split_and_invoke_selection(second_round_list, 7)  # index 4 for the 2nd priority
        selection_round += 1
        del second_round_list  # deleting from memory
        if all([len(biotech_accepted) == max_students_per_department, len(engineering_accepted) == max_students_per_department, len(chemistry_accepted) == max_students_per_department, len(physics_accepted) == max_students_per_department, len(mathematics_accepted) == max_students_per_department]):
            print_results()
            exit()
        else:
            continue

    if selection_round == 3:
        # step #8 obtaining the list for the last tour:
        last_round_list = [*biotech, *engineering, *chemistry, *physics, *mathematics]  # unpacking lists with * asterisk sign
        split_and_invoke_selection(last_round_list, 8)  # index 5 for the 3rd (last) priority
        del last_round_list  # deleting from memory
        print_results()
        exit()

#  exams: physics and math for the Physics department, DONE
#  chemistry for the Chemistry department, DONE
#  math for the Mathematics department, DONE
#  computer science and math for the Engineering Department, DONE
#  chemistry and physics for the Biotech department.

#
# create files with results.
