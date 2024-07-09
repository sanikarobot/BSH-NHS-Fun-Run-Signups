import tkinter
from tkinter import *
import customtkinter
from time import sleep
import threading
import pickle
import student
import tutor
import volunteer
import csv

# Button dictionary for find_student search. Allows for the program to keep track of what buttons are on the screen.
buttons = {}


win = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
win.title("National Honor Society Management Portal")
entry = customtkinter.CTkEntry(win)
scrollable_frame = customtkinter.CTkScrollableFrame(win)
frame = customtkinter.CTkFrame(win)

error_label = customtkinter.CTkLabel(win)

students = []
entries = []
volunteer_entries = []
tutoring_entries = []

'''volunteering_entry1 =  volunteer.Volunteer("the greatest event of all time and places",
                                           "email1", "01/01/2001", 5, "location1")
volunteering_entry2 =  tutor.Tutor("vol2", "email2", "02/02/2002", 5, "location2",
                                   "Jonathan")
volunteering_entry3 =  volunteer.Volunteer("vol3", "email3", "03/03/2003", 5, "location3")
volunteering_entry4 =  volunteer.Volunteer("vol4", "email4", "04/04/4004", 5, "location4")
test_entries = [volunteering_entry4, volunteering_entry3, volunteering_entry2, volunteering_entry1]'''

#student1 = student.Student(name="Sanika", status=0, grade=11, email="hi", log=test_entries)
student2 = student.Student("Marley", 1, 11, "hi")
student3 = student.Student("Aaron", 2, 11, "hi")
student4 = student.Student("Samantha", 3, 12, "hi")
#students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)



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
    win.unbind("<Key>")
    global buttons
    buttons = {}
    clear_screen()
    win.geometry("420x270")
    title_font = ("font1", 25)
    title = customtkinter.CTkLabel(win, text="Main Menu", font=title_font)
    title.grid(row=0, column=0)
    # haha mainframe
    main_frame = customtkinter.CTkFrame(win, height=300, corner_radius=10)
    main_frame.grid(row=1, column=0, ipady=30, rowspan=138)
    option_label = customtkinter.CTkLabel(main_frame, text="Options", font=("font1", 20))
    option_label.grid(row=0, column=0, padx=50, pady=3)
    find_student_button = customtkinter.CTkButton(main_frame, text="Find Student", command=find_student)
    find_student_button.grid(row=1, column=0, padx=50, pady=3)
    import_button = customtkinter.CTkButton(main_frame, text="Import Spreadsheet", command=import_spreadsheet)
    import_button.grid(row=2, column=0, padx=50, pady=3)
    export_button = customtkinter.CTkButton(main_frame, text="Export Information", command=export_information)
    export_button.grid(row=3, column=0, padx=50, pady=3)
    help_button = customtkinter.CTkButton(main_frame, text="Help", command=help_page)
    help_button.grid(row=4, column=0, padx=50, pady=3)

    guide = customtkinter.CTkLabel(win, text="Select an option \n from the left!", width=20, anchor="n",
                                   font=("font1", 20))
    guide.grid(row=1, column=1, columnspan=2, ipadx=50)


def help_page():
    """
    Gives an overview of the program (through text?).
    :return:
    """
    clear_screen()
    menu_button = customtkinter.CTkButton(win, text="Return to main menu", command=menu)
    menu_button.pack()


def import_spreadsheet():
    """
    Reads in a .csv file into the program. This needs to be able to create new volunteering/tutoring logs depending on
    the passed parameters and then return to main menu.
    :return:
    """
    global error_label
    global frame
    # Get the file name from the user
    clear_screen()
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Import Spreadsheet", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=2)
    help_text = customtkinter.CTkLabel(main_frame,
                                       text="Put in the name of the \n spreadsheet you want \n to import from. "
                                            "This \n must be in the same \n folder as the program.")
    help_text.grid(row=1, column=1, padx=8)
    frame = customtkinter.CTkFrame(main_frame, corner_radius=6)
    frame.grid(row=1, column=0, ipady=20)
    field = customtkinter.CTkEntry(frame, placeholder_text="Put the name of the spreadsheet in here.", fg_color="grey",
                                   text_color="#000000", placeholder_text_color="#1f1f1f")
    field.grid(row=0, column=0, ipadx=120, pady=8, padx=10, sticky="nw")
    submit_button = customtkinter.CTkButton(frame, text="Submit File Name", command=lambda: import_file(field.get()))
    submit_button.grid(row=0, column=1, padx=10)
    exit_button = customtkinter.CTkButton(main_frame, text="Quit to main menu", command=menu)
    exit_button.grid(row=3, column=0, columnspan=2)
    win.geometry("700x300")


def export_information():
    """
    Exports a file containing information about each student's volunteering/tutoring hours as well as their club status.
    :return:
    """
    # Get the file name from the user
    clear_screen()
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Export Spreadsheet", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=2)
    help_text = customtkinter.CTkLabel(main_frame,
                                       text="Put in the name of \n the file you want \n to export to. ")
    help_text.grid(row=1, column=1, padx=8)
    frame = customtkinter.CTkFrame(main_frame, corner_radius=6)
    frame.grid(row=1, column=0, ipady=30)
    field = customtkinter.CTkEntry(frame, placeholder_text="Put the name of the spreadsheet in here.", fg_color="grey",
                                   text_color="#000000", placeholder_text_color="#1f1f1f")
    field.grid(row=0, column=0, ipadx=120, pady=8, padx=10)
    submit_button = customtkinter.CTkButton(frame, text="Submit File Name")
    submit_button.grid(row=0, column=1, padx=10)
    exit_button = customtkinter.CTkButton(main_frame, text="Quit to main menu", command=menu)
    exit_button.grid(row=3, column=0, columnspan=2)
    win.geometry("700x300")

    # thread = threading.Thread(target=function)
    # thread.start()


def find_student():
    """
    Brings up a search function that will allow for searching of various club members. This doesn't search for
    individual logs.
    needed: search field, continuous search,
    :return:
    """
    win.geometry("300x400")
    clear_screen()
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Find Student", font=("font1", 25))
    title.grid(row=0, column=0)
    frame = customtkinter.CTkFrame(main_frame, corner_radius=6)
    frame.grid(row=1, column=0)
    global entry
    entry = customtkinter.CTkEntry(frame, placeholder_text="Student Name")
    entry.grid(row=0, column=0)
    win.bind("<Key>", button_creator_setup)
    quit_button = customtkinter.CTkButton(main_frame, text="Quit to main menu", command=menu)
    quit_button.grid(row=3, column=0)
    global scrollable_frame
    scrollable_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Matching Students")
    scrollable_frame.grid(row=2, column=0)
    button_creator_setup()


def button_creator_setup(event=None):
    print(event)
    populate_buttons()


def populate_buttons(key_pressed=None):
    """
    When searching for a user, this function will execute. This will check and remove any buttons that do not match
    with the search query and will add any which do match with the search query. This will execute once per call, but
    not continuously.
    :return:
    """
    query = entry.get().lower().strip()
    # Search inside the students list
    for index, local_student in enumerate(students):
        # Create button below the previous button (or below entry fields) if the student name starts with the search
        # query. However, if the button already exists (with a student existing in buttons), don't execute.
        if local_student.name.lower().strip().startswith(query) and not local_student in buttons:
            # Create a button with a command that gets the student assigned to the button.
            button = customtkinter.CTkButton(scrollable_frame, text=local_student.name,
                                             command=lambda passed_student=local_student:
                                             manage_student(passed_student))
            button.grid(row=index, column=0, padx=30, pady=1)
            buttons[local_student] = button
        # If there exists a button for a student but the student name no longer starts with the search query,
        # then the button needs to be destroyed.
        # Also, remove the student from the buttons' dictionary.
        elif local_student in buttons and not local_student.name.lower().strip().startswith(query):
            button = buttons[local_student]
            button.destroy()
            buttons.pop(local_student)
    # If a button has been pressed, student_found will have bene set to true. If this is the case, go to the
    # management page for that student.


def manage_student(member):
    """
    Displays information about a member's club status, volunteer/tutoring status, and ***any other information
    necessary***. Also provides buttons which allow for management of the member.
    :return:
    """
    clear_screen()
    win.unbind("<Key>")
    global buttons
    buttons = {}
    win.geometry("600x340")
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Manage Student", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=4)
    info_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Member Information")
    info_frame.grid(row=1, column=0, ipadx=8, ipady=8, padx=10, rowspan=10)
    name_label = customtkinter.CTkLabel(info_frame, justify="left",
                                        text="Name: " + str(member.name) + "\n\nVolunteer Hours: "
                                        + str(member.volunteerHours) + "\n\nTutoring Hours: " + str(member.tutorHours) +
                                        "\n\nClub Standing: " + member.getStatusString() + "\n\n" +
                                        wrap_text("Notes: " + member.notes, 35), font=("font1", 13))
    name_label.grid(row=0, column=0, padx=5, pady=5)
    """
    volunteer_hours_label = customtkinter.CTkLabel(info_frame, text="Volunteer Hours: " + str(member.volunteerHours))
    volunteer_hours_label.grid(row=1, column=0, padx=5, pady=5)
    tutoring_hours_label = customtkinter.CTkLabel(info_frame, text="Tutoring Hours: " + str(member.tutorHours))
    tutoring_hours_label.grid(row=2, column=0, padx=5, pady=5)
    club_standing_label = customtkinter.CTkLabel(info_frame, text="Club Standing: " + member.getStatusString())
    club_standing_label.grid(row=3, column=0, padx=5, pady=5)
    notes_label = customtkinter.CTkLabel(info_frame, text="Notes: " + member.notes)
    notes_label.grid(row=4, column=0, padx=5, pady=5)
    """
    actions_frame = customtkinter.CTkFrame(main_frame)
    actions_frame.grid(row=1, column=1, ipadx=8, ipady=8, padx=10)
    actions_frame_title = customtkinter.CTkLabel(actions_frame, text="Actions")
    actions_frame_title.grid(row=0, column=0)
    actions_frame.anchor("n")

    edit_student_information_button = customtkinter.CTkButton(actions_frame, text="Edit Student Information",
                                                              command=lambda passed_member=member:
                                                              edit_student_information(passed_member))
    edit_student_information_button.grid(row=3, column=0, padx=5, pady=5)
    manage_club_standing_button = customtkinter.CTkButton(actions_frame, text="Manage Club Standing",
                                                          command=lambda passed_member=member:
                                                          manage_club_standing(passed_member))
    manage_club_standing_button.grid(row=4, column=0, padx=5, pady=5)
    view_volunteering_entries_button = customtkinter.CTkButton(actions_frame, text="View Volunteering Entries",
                                                        command=lambda passed_member = member:
                                                        view_volunteering_entries(passed_member))
    view_volunteering_entries_button.grid(row=5, column=0, padx=5, pady=5)

    quit_button = customtkinter.CTkButton(main_frame, text="Return to main menu", command=menu)
    quit_button.grid(row=3, column=1, padx=10, pady=10)


def view_volunteering_entries(member: student.Student):
    clear_screen()
    win.unbind("<Key>")
    win.geometry("600x340")
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Volunteering Entries for " + member.name, font=("font1", 25))
    title.grid(row=0, column=0, columnspan=100)
    info_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Volunteering Entries")
    info_frame.grid(row=1, column=0, columnspan=10, ipadx=400)
    for index, volunteer_entry in enumerate(member.log):
        volunteer_entry_frame = customtkinter.CTkFrame(info_frame, fg_color="#1a1a1a")
        volunteer_entry_frame.grid(row=index, column=0, ipadx=200, pady=5, columnspan=5, sticky="nw")
        volunteer_entry_title = customtkinter.CTkLabel(volunteer_entry_frame, text=volunteer_entry.title,
                                                       font=("font1", 20))
        volunteer_entry_title.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky="nw")
        button = customtkinter.CTkButton(volunteer_entry_frame, text="View Information",
                                         command=lambda passed_volunteer_entry=volunteer_entry:
                                         view_volunteer_entry(passed_volunteer_entry, member))
        button.grid(row=1, column=0, padx=10, pady=5, columnspan=4, sticky="nw")
        buttons[volunteer_entry] = button
    quit_button = customtkinter.CTkButton(main_frame, text="Return to Student Information",
                                          command=lambda passed_member=member: manage_student(passed_member))
    quit_button.grid(row=3, column=0, columnspan=100)


def view_volunteer_entry(volunteer_entry: volunteer.Volunteer, member: student.Student):
    clear_screen()
    win.unbind("<Key>")
    win.geometry("600x340")
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Volunteer Entry for " + member.name, font=("font1", 25))
    title.grid(row=0, column=0, columnspan=4)
    if volunteer_entry is tutor.Tutor:
        title.configure(text="Tutoring Entry for " + member.name)
    info_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Member Information")
    info_frame.grid(row=1, column=0, ipadx=8, ipady=8, padx=10, rowspan=10)
    name_label = customtkinter.CTkLabel(info_frame, justify="left",
                                        text="Title: " + str(volunteer_entry.title) + "\n\nDate: "
                                        + str(volunteer_entry.date) + "\n\nHours: " + str(volunteer_entry.time) +
                                        "\n\nLocation: " + volunteer_entry.location + "\n\nNotes: " +
                                        volunteer_entry.notes,
                                        font=("font1", 13))
    name_label.grid(row=0, column=0, padx=5, pady=5)
    quit_button = customtkinter.CTkButton(main_frame, text="Return to volunteer entries",
                                          command=lambda: view_volunteering_entries(member))
    quit_button.grid(row=1, column=1, padx=10, pady=10)



def manage_club_standing(member: student.Student):
    """
    Provides options to add a flag to a member denoting their current status within the club. This is where people can
    be manually changed to be in good standing, poor standing, tenuous standing, or eligible for cords.
    :return:
    """
    clear_screen()
    radio_var = tkinter.IntVar(value=member.status)
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Change Club Standing", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=4)

    radiobutton_frame = customtkinter.CTkFrame(main_frame)
    radiobutton_frame.grid(row=1, column=1, ipadx=30, padx=10)
    radio_button_1 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=0,
                                                  text="Poor")
    radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
    radio_button_2 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=1,
                                                  text="Medium")
    radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="w")
    radio_button_3 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=2,
                                                  text="Good")
    radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="w")
    radio_button_4 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=3,
                                                  text="On Track for Cords")
    radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="w")

    student_information_frame = customtkinter.CTkFrame(main_frame)
    student_information_frame.grid(row=1, column=0, ipadx=90, ipady=60)
    name_label = customtkinter.CTkLabel(student_information_frame, justify="left",
                                        text="Name: " + str(member.name) + "\n\nVolunteer Hours: "
                                        + str(member.volunteerHours) + "\n\nTutoring Hours: " + str(member.tutorHours) +
                                        "\n\n" + wrap_text("Notes: " + member.notes, 35),
                                        font=("font1", 13))
    name_label.grid(row=0, column=0, padx=5, pady=5)

    quit_button = customtkinter.CTkButton(main_frame, text="Back to student management page",
                                          command=lambda passed_member=member:
                                          manage_student(passed_member))
    quit_button.grid(row=3, column=0, columnspan=4)

    # This sets a keybind to call the set_member_status function. This passes the member which the status needs to be
    # modified and gives the value to set the member to. I don't know why this works, but it does.
    win.bind("<Button-1>", lambda passed_member=member: set_member_status(member, radio_var.get()))


def set_member_status(member: student.Student, value): member.status = value


def edit_student_information(member: student.Student):
    """
    Allows changes to personal information within the system. This can change the displayed email address, name, or
    grade. This does not change information inside of the spreadsheet, rather just what is displayed within the program.
    :return:
    """
    clear_screen()
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Change Club Standing", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=4)
    student_information_frame = customtkinter.CTkFrame(main_frame)
    student_information_frame.grid(row=1, column=0, ipadx=90, ipady=60)
    name_label = customtkinter.CTkLabel(student_information_frame, justify="left",
                                        text="Name: " + str(member.name) + "\n\nVolunteer Hours: "
                                        + str(member.volunteerHours) + "\n\nTutoring Hours: " + str(member.tutorHours) +
                                        "\n\n" + wrap_text("Notes: " + member.notes, 35), font=("font1", 13))
    name_label.grid(row=0, column=0, padx=5, pady=5)

    entry_fields_frame = customtkinter.CTkFrame(main_frame)
    entry_fields_frame.grid(row=1, column=1, padx=10, ipadx=10, ipady=10)
    entry_fields_title = customtkinter.CTkLabel(entry_fields_frame, text="Enter in new information here",
                                                font=("font1", 20))
    entry_fields_title.grid(row=0, column=0, columnspan=2)
    name_change_label = customtkinter.CTkLabel(entry_fields_frame, text="New Name:")
    name_change_label.grid(row=1, column=0, padx=15)
    name_change_field = customtkinter.CTkEntry(entry_fields_frame)
    name_change_field.grid(row=1, column=1, ipadx=150)
    name_change_field.insert(0, member.name)
    notes_change_label = customtkinter.CTkLabel(entry_fields_frame, text="Notes:")
    notes_change_label.grid(row=2, column=0, padx=15)
    notes_change_field = customtkinter.CTkEntry(entry_fields_frame)
    notes_change_field.grid(row=2, column=1, ipadx=150, ipady=100)
    notes_change_field.insert(0, member.notes)
    submit_button = customtkinter.CTkButton(entry_fields_frame, text="Submit Changes",
                                            command= lambda passed_member=member:
                                            set_member_info(member, name_change_field.get(), notes_change_field.get()))
    submit_button.grid(row=3, column=0, padx=30, pady=10, columnspan=2)
    quit_button = customtkinter.CTkButton(main_frame, text="Back to student management page",
                                          command=lambda passed_member=member:
                                          manage_student(passed_member))
    quit_button.grid(row=3, column=0, columnspan=4)


def set_member_info(member, name, notes):
    member.name = name
    member.notes = notes


def wrap_text(text: str, character_count: int):
    """
    This function calls itself recursively in order to insert \n characters into text in order to allow for text to be
    wrapped according to
    :param text:
    :param character_count:
    :return:
    """
    if len(text) <= character_count:
        return text
    else:
        passes = 0
        return_value_location = 0
        while True:
            if text[character_count-passes] != " ":
                passes = passes + 1
            else:
                # I hate python strings sometimes
                text = text[:character_count-passes] + "\n" + text[character_count-passes+1:]
                return_value_location = character_count-passes
                break
        return_text = str(text[:return_value_location]) + str(wrap_text(text[return_value_location:], character_count))
        return return_text

def import_file(fileName: str)-> None:
    '''this whole thing likely will need to be changed based upon how we format the google sheet pretty much what it
    does is opens the .csv file and puts each row into a dictionary based upon the title at the top of the column
    then it checks to see if there is a person in the system already that matches the info in the row. if not it
    creates a new person and adds the entry to the person if there is it adds the entry to the person that it belongs
    to. the person identification is done using the email'''
    if not fileName.lower().endswith(".csv"):
        fileName = fileName + ".csv"
    try:
        with open(fileName, newline= '') as csvfile:
            memberReader = csv.DictReader(csvfile, restval= "notes")
            checker = False
            #we're going to need to add in some threads here to manage this monstrosity of for loops
            for row in memberReader:
                checker = False
                for member in students:
                    if row['email'] == member.email:
                        addNewActivity(row, member)
                        checker = True
                        break
                if checker == False:
                    newMember = student.Student(row["name"], row["grade"], row["email"])
                    students.append(newMember)
                    addNewActivity(row, newMember)

        error_label = customtkinter.CTkLabel(frame, text="Successfully imported files")
        error_label.grid(row=1, column=0, columnspan=2, padx=12, pady=8, sticky="nw")
        frame.grid(ipady=0)

    except FileNotFoundError:
        print("unable to find file.") #this should change to something that will actually work with the GUI
        error_label = customtkinter.CTkLabel(frame, text="Unable to find file")
        error_label.grid(row=1, column=0, columnspan=2, padx=12, pady=8, sticky="nw")
        frame.grid(ipady=0)

def addNewActivity(activity: dict, student: student.Student)-> None:
    """
    The implementation of this function is dependent on how we will be importing from Google Forms. This is likely
    better implemented as a function inside of the student class, but it's possible that it may be better to include a
    separate function outside of the student class.
    :param activity:
    :param student:
    :return:
    """
    if activity["type"] == "tutor":
        newTutor = tutor.Tutor(activity["email"], activity["date"], float(activity["time"]), activity["location"], activity["notes"], activity["tutee"])
        student.log.append(newTutor)
        student.tutorHours = student.getTotalTutorHours()
        student.allHours = student.getTotalHours()
    elif activity["type"] == "volunteer":
        newVolunteer = volunteer.Volunteer(activity["email"], activity["date"], float(activity["time"]), activity["location"], activity["notes"])
        student.log.append(newVolunteer)
        student.volunteerHours = student.getTotalVolunteerHours()
        student.allHours = student.getTotalHours()
    else:
        raise Exception ("error proccessing expeirence type, unable to tell if it is a volunteer or tutoring experience.")
    



print(wrap_text("this is a quick test to see if the text wrapping function works", 10))


clear_screen()
menu()
win.mainloop()
