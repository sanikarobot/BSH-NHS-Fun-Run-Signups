from threading import Thread
import customException

class Volunteer():
    def __init__(self, title: str, email: str, date: str, time: float, location: str, notes: str = "") -> None:
        # Copypaste: volunteer.Volunteer(title, email, date, time, location)
        self.title = title
        self.email = email
        self.date = date
        self._dateInts = []
        self.analyzeDate()
        self.month = self._dateInts[0]
        self.day = self._dateInts[1]
        self.year = self._dateInts[2]
        self.time = time
        self.location = location


    @property
    def title(self)-> str:
        return self._title
    
    @title.setter
    def title(self, title)-> None:
        self._title = title

    @property
    def email(self)-> str:
        return self._email
    
    @email.setter
    def email(self, email)-> None:
        self._email = email

    @property
    def date(self)-> str:
        return self._date
    
    @date.setter
    def date(self, date)-> None:
        self._date = date

    @property
    def time(self)-> str:
        return self._time
    
    @time.setter
    def time(self, time)-> None:
        self._time = time

    @property
    def location(self)-> str:
        return self._location
    
    @location.setter
    def location(self, location)-> None:
        self._location = location

    @property
    def notes(self)-> str:
        return self._notes
    
    @notes.setter
    def notes(self, notes)-> None:
        self._notes = notes

    @property
    def month(self)-> str:
        return self._month

    @month.setter
    def month(self, value):
        self._month = ""
        if value == 1:
            self._month= "January"
        elif value == 2:
            self._month= "February"
        elif value == 3:
            self._month= "March"
        elif value == 4:
            self._month= "April"
        elif value == 5:
            self._month= "May"
        elif value == 6:
            self._month= "June"
        elif value == 7:
            self._month= "July"
        elif value == 8:
            self._month= "August"
        elif value == 9:
            self._month= "September"
        elif value == 10:
            self._month= "October"
        elif value == 11:
            self._month= "November"
        elif value == 12:
            self._month= "December"
        else:
            raise customException.CustomException("Value provided for month out of bounds (1-12 required)")

    @property
    def day(self)-> str:
        return self._day

    @day.setter
    def day(self, value) -> None:
        self._day = value

    @property
    def year(self)-> str:
        return self._year

    @year.setter
    def year(self, value) -> None:
        self._year = value

    def analyzeDate(self):
        if "/" in self.date:
            self._dateInts = self.date.split("/")
        elif "-" in self.date:
            self._dateInts = self.date.split('-')
        return self._dateInts
    
    def getMonth(self)-> str:
        numMonth = self._dateInts[0]
        self.month = self._dateInts[0]
        if numMonth == 1:
            return "January"
        elif numMonth == 2:
            return "February"
        elif numMonth == 3:
            return "March"
        elif numMonth == 4:
            return "April"
        elif numMonth == 5:
            return "May"
        elif numMonth == 6:
            return "June"
        elif numMonth == 7:
            return "July"
        elif numMonth == 8:
            return "August"
        elif numMonth == 9:
            return "September"
        elif numMonth == 10:
            return "October"
        elif numMonth == 11:
            return "November"
        elif numMonth == 12:
            return "December"
        else:
            raise customException.CustomException("Value provided for month out of bounds (1-12 required)")
    
    def getDay(self)-> str:
        self.day = self._dateInts[1]
        return self.day
    
    def getYear(self)-> str:
        self.year = self._dateInts[2]
        return self.year
