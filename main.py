from tkinter import *
from time import sleep
import threading
import pickle

win = Tk()


def clear_screen():
    """
    Destroys all of the items on the window, thus clearing the screen.
    """
    for child in win.winfo_children():
        child.destroy()


def menu():
    """
    Main menu. Displays buttons which lead to different pages, as well as an option to go to a help page.
    Buttons: find_student, import spreadsheet, export information, and a help page button.
    :return:
    """
    clear_screen()
    # haha mainframe
    title_font = ("Lato", 15)
    title = Label(text="Welcome to NHS Management!", font=title_font)
    title.pack()
    main_frame = LabelFrame(text="Options", padx=5, pady=5, borderwidth=2, highlightbackground="red")
    main_frame.pack()
    find_student_button = Button(main_frame, text="Find Student", command=find_student)
    find_student_button.pack()




def help_page():
    """
    Gives an overview of the program (through text?).
    :return:
    """


def import_spreadsheet():
    """
    Reads in a .csv file into the program. This needs to be able to create new volunteering/tutoring logs depending on
    the passed parameters and then return to main menu.
    :return:
    """


def export_information():
    """
    Exports a file containing information about each student's volunteering/tutoring hours as well as their club status.
    :return:
    """


def find_student():
    """
    Brings up a search function that will allow for searching of various club members. This doesn't search for
    individual logs.
    :return:
    """


def manage_person():
    """
    Displays information about a member's club status, volunteer/tutoring status, and ***any other information
    necessary***. Also provides buttons which allow for management of the member.
    :return:
    """


def manage_club_standing():
    """
    Provides options to add a flag to a member denoting their current status within the club. This is where people can
    be manually changed to be in good standing, poor standing, tenuous standing, or eligible for cords.
    :return:
    """


def edit_person_information():
    """
    Allows changes to personal information within the system. This can change the displayed email address, name, or
    grade. This does not change information inside of the spreadsheet, rather just what is displayed within the program.
    :return:
    """


def edit_entries():
    """
    Allows for changes to entries. This can change the contents of the spreadsheet, or it can create a new spreadsheet
    with all the changes logged within it.
    :return:
    """


menu()
win.geometry("400x400")
win.mainloop()

