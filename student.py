#student data management
num = int(input('how many. ')) 
database = []

def addstudent(name, dep, mark):
    database.append({'student_name': name, 'department': dep, 'marks':mark})

def printstudents():
   for j in range(num):
      print(database[j]['student_name'] + " from " + database[j]['department'] + " department " , database[j]['marks'] , " grade: " + database[j]['grade']) 
def calculate_result():
    for student_data in database:
        if student_data['marks'] >= 90:
            grade ='a'
        elif student_data['marks'] >= 80:
            grade = 'b'
        else:
            grade = 'f'
        student_data['grade'] = grade
#3 keys
for i in range(num):
    name = input('ENTER YOUR NAME: ')
    dep = input('what department? ')
    mark = int(input('what is your mark? '))
    addstudent(name, dep, mark)    

calculate_result()
printstudents()


    