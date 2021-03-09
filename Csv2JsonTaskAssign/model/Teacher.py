from Personnel import Personnel

class Teacher(Personnel):
    def __init__(self, id, fullName, gender, dob, age, aadhar, city, contact, empNo, classTeacher, previousSchool, post, 
    doj, salary, servicePeriod, subjectTeaches):

        Personnel.__init__(self, id, fullName, gender, dob, age, aadhar, city, contact)
        
        self.empNo = empNo
        self.classTeacher = classTeacher
        self.previousSchool = previousSchool
        self.post = post
        self.doj = doj
        self.salary = salary
        self.servicePeriod = servicePeriod
        self.subjectTeaches = subjectTeaches