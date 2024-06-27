from threading import Thread

class Volunteer():
    def __init__(self, title: str, email: str, date: str, time: float, location: str, notes: str) -> None:
        self.title = title
        self.email = email
        self.date = date
        self.time = time
        self.location = location
        self.month = ""
        self.day = ""
        self.year = ""
        self.dateInts = []

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
        
    # We should also add in a notes section as 
    
    def analyizeDate(self):
        if "/" in self.date:
            self.dateInts = self.date.split("/")
        elif "-" in self.date:
            self.date.split('-')
        return self.dateInts
    
    def getMonth(self)-> str:
        numMonth = self.dateInts[0]
        self.month = ""
        if numMonth == 1:
            self.month = "January"
        elif numMonth == 2:
            self.month = "February"
        elif numMonth == 3:
            self.month = "March"
        elif numMonth == 4:
            self.month = "April"
        elif numMonth == 5:
            self.month = "May"
        elif numMonth == 6:
            self.month = "June"
        elif numMonth == 7:
            self.month = "July"
        elif numMonth == 8:
            self.month = "August"
        elif numMonth == 9:
            self.month = "September"
        elif numMonth == 10:
            self.month = "October"
        elif numMonth == 11:
            self.month = "Novemeber"
        elif numMonth == 12:
            self.month = "December"
        return self.month
    
    def getDay(self)-> str:
        self.day = self.dateInts[1]
        return self.day
    
    def getYear(self)-> str:
        self.year = self.dateInts[2]
        return self.year
