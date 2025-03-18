from threading import *
from volunteer import Volunteer
from tutor import Tutor
import customException


class Student:

    next_student_id = 0

    def __init__(self, name: str, grade: int, email: str, notes: str = "", volunteerHours=0,
                 tutorHours=0, status=0, attendance=0, log=None) -> None:

        """ Here we declare our varibles. 
        Because we do not want our name, email, grade, or status varibles to be easily changed we use properties to store then such that it is hard to accidentally change them
        We use the student_id varible to help the computer keep track of the students.
        The log list stores all volunteering and tutoring activities a student has done."""
        if log is None:
            log = []
        self.name = name
        self.email = email
        self.grade = grade
        self.status = status
        self.volunteerHours = volunteerHours
        self.tutorHours = tutorHours
        self.attendance = attendance
        self.student_id = Student.next_student_id
        Student.next_student_id = Student.next_student_id + 1
        self.log = log
        self.notes = notes
        self.volunteerHours = self.getTotalVolunteerHours()
        self.tutorHours = self.getTotalTutorHours()
        self.allHours = self.getTotalHours()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = self.truncate_name(name)


    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, student_id) -> None:
        self._student_id = student_id

    @property
    def status(self) -> int:
        return self._status

    @status.setter
    def status(self, status) -> None:
        """
        Status must be an integer between 0 and 4. This test first ensure that the value passed is an integer then
        verifies it is between 0 and 4 (excluding 4).
        """
        if not (isinstance(status, int)):
            raise customException.CustomException("Status must be an integer")
        if not (status >= 0 and status < 4):
            raise customException.CustomException("Status integer out of bounds")
        # Set value
        self._status = status

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, grade) -> None:
        self._grade = grade

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        self._email = email

    @property
    def attendance(self) -> int:
        return self._attendance
    
    @attendance.setter
    def attendance(self, attendance)-> None:
        if not isinstance(attendance, int):
            raise customException.CustomException("Attendance must be an integer")
        elif attendance < 0:
            raise customException.CustomException("Attendance must be a positive number")
        else:
            self._attendance = attendance

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    """ This function gets the total time a club member has spent volunteering by running through their list of activies and checking if every activity is a volunteer activity or not.
    For all the volunteer activities it adds up the time spent working on them"""

    def getTotalVolunteerHours(self) -> float:
        self.volunteerHours = 0
        for i in self.log:
            if type(i) != Tutor and type(i) == Volunteer:
                print(type(i), i.location)
                self.volunteerHours = self.volunteerHours + i.time
        return self.volunteerHours

    """ This function is essentially the same, but for the tutoring activites."""

    def getTotalTutorHours(self) -> float:
        self.tutorHours = 0
        for i in self.log:
            if type(i) == Tutor:
                print(type(i), i.tutee)
                self.tutorHours = self.tutorHours + i.time
        return self.tutorHours

    """ This function adds up the results of the getVolunteerHoursFunction and the getTutorHours function to get the total hours spent meeting NHS requirements."""

    def getTotalHours(self) -> float:
        vHours = self.getTotalVolunteerHours()
        tHours = self.getTotalTutorHours()
        totalHours = vHours + tHours
        return totalHours

    def getStatusString(self):
        """
        This function returns a string value for status. Takes the int value stored in status and converts it to its
        respective string value for easy access in the program.
        """
        if self.status == 0:
            return "Poor"
        if self.status == 1:
            return "Medium"
        if self.status == 2:
            return "Good"
        if self.status == 3:
            return "On Track for Cords"
        else:
            raise customException.CustomException("Status integer too large")
    
    def clear (self):
        self.log.clear
        self.volunteerHours = 0
        self.tutorHours = 0
        self.allHours = 0
       
    def clearAttendance(self):
        self.attendance = 0

    def incrementAttendance(self):
        self.attendance += 1

    @staticmethod
    def truncate_name(name):
        spacePosition = 0
        for character in name:
            if character == " ":
                break
            spacePosition = spacePosition + 1
        name = (name[0] + "." + name[spacePosition:])
        return name


    def identify_email(self, email):
        """
        Identifies if the student's name corresponds with the email given
        :return:
        """
        if email.contains(self.name[3:]) and (email[0] == self.name[0]):
            return True
        return False
