from Personnel import Personnel

class Student(Personnel):
    def __init__(self, id, fullName, gender, dob, age, aadhar, city, contact, rollNumber,className, totalMarks, grade, secPercentage, hsStream):
        Personnel.__init__(self, id, fullName, gender, dob, age, aadhar, city, contact)
        
        self.rollNumber = rollNumber
        self.className = className
        self.totalMarks = totalMarks
        self.grade = grade
        self.secPercentage = secPercentage
        self.hsStream = hsStream


        