class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Student(Person):
    def __init__(self, name, cources = {}):
        super().__init__(name)
        self.cources = {}
    
    def getCources(self):
        return self.cources
    
    def addCourses(self,course):
        pass
        #self.cources.update(course)

    @staticmethod
    def getAge():
        return 23

class Course:
    def __init__(self,name,institution):
        self.name = name
        self.institution = institution
        self.status = "Active"

    def to_JSON(self):
        return {
            "name" : self.name,
            "institution" : self.institution,
            "status" : self.status
        }
    
danial = Student("Danial")
danial.addCourses(Course("Computer Engineering","Hs Augsburg"))

print(Student.getAge())