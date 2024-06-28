from volunteer import Volunteer
from threading import Thread

class Tutor(Volunteer):
    def __init__(self, title: str, email: str, date: str, time: float, location: str, notes: str = "") -> None:
        super().__init__(title, email, date, time, location, notes)