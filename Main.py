#Age and Student Status Checker

age = int(input('what is your age: '))
st_ver = input('Are you a student: ')
if st_ver == 'yes':
    is_student = True
elif st_ver == 'no':
    is_student = False
else:
    print('Enter valid response')

print(age <= 18 or is_student)
