from volunteer import Volunteer
from threading import Thread

class Tutor(Volunteer):
    def __init__(self, email: str, date: str, time: float, location: str, title: str, notes: str, tutee: str) -> None:
        super().__init__(email, date, time, location, notes)
        self.tutee = tutee
        self.title = title

    @property
    def tutee(self)-> str:
        return self._tutee
    
    @tutee.setter
    def tutee(self, tutee)-> None:
        self._tutee = tutee