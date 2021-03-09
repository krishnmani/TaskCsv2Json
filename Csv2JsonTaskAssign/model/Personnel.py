class Personnel:
    def __init__(self, id, fullName, gender, dob, age, aadhar, city, contact):
        self.id = id
        self.fullName = fullName
        self.gender = gender
        self.dob = dob
        self.age = age
        self.aadhar = aadhar
        self.city = city
        self.contact = contact

    # def printName(self):
    #     print(self.city)

# perInstance = Personnel(1, "krishn manni", "male", "11-08-1996", 24, "812032323714", "patna")
# perInstance.printName()