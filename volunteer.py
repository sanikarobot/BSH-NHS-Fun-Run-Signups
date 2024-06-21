

class Volunteer():
    def __init__(self, name: str, email: str, date: str, time: float, location: str) -> None:
        self.name = name
        self.email = email
        self.date = date
        self.time = time
        self.location = location

    @property
    def name(self)-> str:
        return self._name
    
    @name.setter
    def name(self, name)-> None:
        self._name = name

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
        


    # We should also add in a notes section as well


    pass
