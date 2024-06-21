

class Student:

    next_student_id = 0

    def __init__(self, name):
        self.name = name
        self.student_id = Student.next_student_id
        Student.next_student_id = Student.next_student_id + 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id
