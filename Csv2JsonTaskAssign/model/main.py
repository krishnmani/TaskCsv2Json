import json
import csv
import os
from collections import OrderedDict
from datetime import datetime, date
from babel.numbers import format_currency
import locale
from Student import Student
from Teacher import Teacher


def calculate_age(born):
    born = datetime.strptime(str(born), '%m/%d/%Y').date()
    today = date.today()
    year = today.year - born.year - 1
    month = 12 + today.month - 1 - born.month if today.month < born.month else today.month - born.month
    return f'{year} Years {month} months'


def calculate_grade(marks):
    percentage = int(marks)/1000 * 100
    if percentage > 90:
        return 'A+'
    elif percentage > 80 and percentage < 89:
        return 'A'
    elif percentage > 70 and percentage < 79:
        return 'B+'
    elif percentage > 60 and percentage < 69:
        return 'B'
    elif percentage > 50 and percentage < 59:
        return 'C'
    else:
        return 'D'


def calculate_fullname(fname, lname):
    return f'{fname} {lname}'


def service_period(doj):
    return calculate_age(doj)


def format_salary(salary):
    b =  format_currency(salary, 'INR', locale='en_IN')[1:]
    c = b[0:len(b)-3]
    return c
    
    

    
def save_json_files(data, category, path):
    os.makedirs(path, exist_ok=True)
    filename = str(datetime.today()).split()[0].replace('-', '')

    if category == 'student':
        student_data = open(f'{path}/student_record_{filename}.json', 'a')
        student_data.write(f'{json.dumps(data, indent = 4)}')
    
    if category == 'teacher':
        teacher_data = open(f'{path}/teacher_record_{filename}.json', 'a')
        teacher_data.write(f'{json.dumps(data, indent = 4)}')
    
    

    
def read_csv(filepath):
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dic = OrderedDict()
        data = {}
        line_count = -1
        for l, row in enumerate(csv_reader):
            line_count += 1
            if line_count == 0:
                keys = row
                continue
            else:
                for ind in range(len(row)):
                    dic[keys[ind]] = row[ind]
            data[l] = dic
            dic = {}

        # json_object = json.dumps(data, indent = 4)
        return data


def update_data(data):
    updated_data = {}
    for k, val in data.items():
        # Change 'm/f' to 'Male/Female' 
        if val['gender'] == 'm':
            val['gender'] = 'Male'
        else:
            val['gender'] = 'Female'

        val['fullName'] = calculate_fullname(val['firstname'], val['lastname'])

        val.pop('firstname')
        val.pop('lastname')

        val['age'] = calculate_age(val['dob'])

        if val['category'] == 'student':
            val["grade"] = calculate_grade(val['total_marks'])
            
        else:
            val['servicePeriod'] = service_period(val['doj'])
            val['salary'] = val['salary']
        updated_data[k] = val
    return updated_data


if __name__ == '__main__':
    csv_file = 'C:\\Users\\manik\\OneDrive\\Desktop\\Task\\master-data2.csv'

    data = read_csv(csv_file)
    data = update_data(data)

    students = []
    teachers = []
    
    
    def get_Student_record(obj):
        
        st_record = {
            "id" : obj.id,
            "fullName" : obj.fullName,
            "gender" : obj.gender,
            "dob" : obj.dob,
            "age" : calculate_age(obj.dob),
            "aadhar" : obj.aadhar,
            "city" : obj.city,
            "contactNumber" : obj.contact,
            "rollNumber" : obj.rollNumber,
            "className" : obj.className,
            "totalMarks" : obj.totalMarks,
            "grade" : calculate_grade(obj.totalMarks),
            "secPercent" : obj.secPercentage,
            "hsStream" : obj.hsStream
        }
        return st_record


    def get_Teacher_record(obj):
        
        tea_record = {
            "id" : obj.id,
            "fullName" : obj.fullName,
            "gender" : obj.gender,
            "dob" : obj.dob,
            "age" : calculate_age(obj.dob),
            "aadhar" : obj.aadhar,
            "city" : obj.city,
            "contactNumber" : obj.contact,
            "empNo" : obj.empNo,
            "classTeacher" : obj.classTeacher,
            "doj" : obj.doj,
            "servicePeriod" : service_period(obj.doj),
            "previousSchool" : obj.previousSchool,
            "post" : obj.post,
            "salary" : format_salary(obj.salary),
        }
        return tea_record

        


    for val in data.values():
        #  Separating Student and Teachers
        if val['category'] == 'student':
            
            st = Student(
                id = val['id'],
                fullName = val['fullName'],
                gender = val['gender'],
                dob = val['dob'],
                age = calculate_age(val['dob']),
                aadhar = val['aadhar_number'],
                city = val['city'],
                contact = val['contact_number'],
                rollNumber = val['roll_no'],
                className = val['class'],
                totalMarks = val['total_marks'],
                grade = calculate_grade(val['total_marks']),
                secPercentage = val['sec_percent'],
                hsStream = val['hs_stream']
                )
            st_record = get_Student_record(st)
            students.append(st_record)
            st_record = None
            
        else:
            
            tea = Teacher(
                id = val['id'],
                fullName = val['fullName'],
                gender = val['gender'],
                dob = val['dob'],
                age = calculate_age(val['dob']),
                aadhar = val['aadhar_number'],
                city = val['city'],
                contact = val['contact_number'],
                empNo = val['emp_no'],
                classTeacher = val['class_teacher_of'],
                previousSchool = val['previous_school'],
                post = val['post'],
                doj = val['doj'],
                salary = val['salary'],
                servicePeriod = service_period(val['doj']),
                subjectTeaches = val['subject_teaches']
                )
            tea_record = get_Teacher_record(tea)
            teachers.append(tea_record)
            tea = None


    studentRecordCount = len(students) 
    teacherRecordCount = len(teachers)


    final_student_record = {
        'studentRecordCount' : studentRecordCount,
        'data' : students
    }

    final_teacher_record = {
        'teacherRecordCount' : teacherRecordCount,
        'data' : teachers
    }

    # Enter Path
    print('Enter path to store JSON files: ')
    path = input()

    # Save teacher and student data to JSON files
    try:
        save_json_files(final_student_record, 'student', path)
        save_json_files(final_teacher_record, 'teacher', path)
    except Exception as e:
        print(e)

    print('2 JSON files created successfully')
    
    
