# University Admission Application
#total_number_of_applicants = int(input())
#spots_availiable = int(input())
#applicants_list = [input().split() for aplicant in range(total_number_of_applicants)]

#for value in applicants_list:
#    value[2] = float(value[2])

def admission_process(applicants_data):
    sorted_results = sorted(applicants_data)
    sorted_results = sorted(sorted_results, key = lambda x: (x[3], -x[2]))
    return sorted_results

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
sorted_applicants1 = admission_process(applicants)
print("len of the sorted_applicants1 list now", len(sorted_applicants1))
#print(sorted_applicants)

# step #4 creating empty lists of candidates for each of departments
biotech = [person for person in sorted_applicants1 if person[3] == "Biotech"]
engineering = [person for person in sorted_applicants1 if person[3] == "Engineering"]
chemistry = [person for person in sorted_applicants1 if person[3] == "Chemistry"]
physics = [person for person in sorted_applicants1 if person[3] == "Physics"]
mathematics = [person for person in sorted_applicants1 if person[3] == "Mathematics"]

# step #5 splitting into 5 lists:
#for applicant in sorted_applicants:
#    if applicant[3] == "Biotech":  # index 3 for the first choice in their application
#        biotech.append(applicant)
#        sorted_applicants.remove(applicant)
#    elif applicant[3] == "Engineering":  # index 3 for the first choice in their application
#        engineering.append(applicant)
#        sorted_applicants.remove(applicant)
#    elif applicant[3] == "Chemistry":  # index 3 for the first choice in their application
#        chemistry.append(applicant)
#        sorted_applicants.remove(applicant)
#    elif applicant[3] == "Physics":  # index 3 for the first choice in their application
#        physics.append(applicant)
#        sorted_applicants.remove(applicant)
#    elif applicant[3] == "Mathematics":  # index 3 for the first choice in their application
#        mathematics.append(applicant)
#        sorted_applicants.remove(applicant)


print(len(biotech))
print(len(engineering))
print(len(chemistry))
print(len(physics))
print(len(mathematics))

sorted_applicants1.clear()
print("the sorted_applicants1 list now", sorted_applicants1)
print("len of the sorted_applicants1 list now", len(sorted_applicants1))

# step 5 the frist round of selection
biotech_accepted = []
engineering_accepted = []
chemistry_accepted = []
physics_accepted = []
mathematics_accepted = []


if len(biotech) <= max_students_per_department:
    biotech_accepted = biotech
    biotech.clear()
else:
    ...

if len(engineering) <= max_students_per_department:
    engineering_accepted = engineering
    engineering.clear()
else:
    ...
if len(chemistry) <= max_students_per_department:
    chemistry_accepted = chemistry
    chemistry.clear()
else:
    ...
if len(physics) <= max_students_per_department:
    physics_accepted = physics
    physics.clear()
else:
    ...
if len(mathematics) <= max_students_per_department:
    mathematics_accepted = mathematics
    mathematics.clear()
else:
    ...
