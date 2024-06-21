from threading import *
from volunteer import Volunteer
from tutor import Tutor

class Student:


    # We should also add in a notes section as well


    next_student_id = 0

    def __init__(self, name, status, grade: int, email, volunteerHours=0, tutorHours=0)-> None:

        """ Here we declare our varibles. 
        Because we do not want our name, email, grade, or status varibles to be easily changed we use properties to store then such that it is hard to accidentally change them
        We use the student_id varible to help the computer keep track of the students.
        The log list stores all volunteering and tutoring activities a student has done."""
        self.name = name
        self.email = email
        self.grade = grade
        self.status = status
        self.volunteerHours = volunteerHours
        self.tutorHours = tutorHours
        self.student_id = Student.next_student_id
        Student.next_student_id = Student.next_student_id + 1
        self.log = []

    @property
    def name(self)-> str:
        return self._name

    @name.setter
    def name(self, name)-> None:
        self._name = name
        
    @property
    def student_id(self)-> str:
        return self._student_id

    @student_id.setter
    def student_id(self, student_id) -> None:
        self._student_id = student_id

    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, status) -> None:
        self._status = status

    @property
    def grade(self)-> str:
        return self._grade
    
    @grade.setter
    def grade(self, grade)-> None:
        self._grade = grade

    @property
    def email(self)-> str:
        return self._email
    
    @email.setter
    def email(self, email)-> None:
        self._email = email
    
    

    """ This function gets the total time a club member has spent volunteering by running through their list of activies and checking if every activity is a volunteer activity or not.
    For all the volunteer activities it adds up the time spent working on them"""
    def getTotalVolunteerHours(self)-> float:
        for i in self.log:
            if type(i) == Volunteer:
                self.volunteerHours = self.volunteerHours + i.time
        return self.volunteerHours
    
    volunteerThread = Thread(target=getTotalVolunteerHours)
    volunteerThread.start()

    """ This function is essentially the same, but for the tutoring activites."""
    def getTotalTutorHours(self)-> float:
        for i in self.log:
            if type(i) == Tutor:
                self.tutorHours = self.tutorHours + i.time
        return self.tutorHours

    tutorThread = Thread(target=getTotalTutorHours)
    tutorThread.start()

    """ This function adds up the results of the getVolunteerHoursFunction and the getTutorHours function to get the total hours spent meeting NHS requirements."""
    def getTotalHours(self)-> float:
        vHours = self.getTotalVolunteerHours()
        tHours = self.getTotalTutorHours()
        totalHours = vHours + tHours
        return tHours



