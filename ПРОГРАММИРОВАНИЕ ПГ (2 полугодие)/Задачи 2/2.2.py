class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def enroll_in_subject(self, subject, grade):
        self.subjects[subject] = grade

    def drop_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]

    def calculate_average_grade(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)


student = Student("Ivan", 20)
student.enroll_in_subject("Math", 90)
student.enroll_in_subject("Physics", 85)
student.drop_subject("Math")
print(student.calculate_average_grade())
