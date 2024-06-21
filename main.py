from tkinter import *
import customtkinter
from time import sleep
import threading
import pickle
import student
import tutor
import volunteer

# Button dictionary for find_student search. Allows for the program to keep track of what buttons are on the screen.
buttons = {}

win = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
win.title("National Honor Society Management Portal")
entry = customtkinter.CTkEntry(win)
scrollable_frame = customtkinter.CTkScrollableFrame(win)

students = []
entries = []
volunteer_entries = []
tutoring_entries = []

student1 = student.Student("Sanika")
student2 = student.Student("Marley")
student3 = student.Student("Aaron")
student4 = student.Student("Samantha")
students.append(student1)
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
    clear_screen()
    win.geometry("420x220")
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
    frame.grid(row=1, column=0, ipady=30)
    field = customtkinter.CTkEntry(frame, placeholder_text="Put the name of the spreadsheet in here.", fg_color="grey",
                                   text_color="#000000", placeholder_text_color="#1f1f1f")
    field.grid(row=0, column=0, ipadx=120, pady=8, padx=10)
    submit_button = customtkinter.CTkButton(frame, text="Submit File Name")
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


def button_creator_setup(event):
    print(event)
    thread = threading.Thread(target=populate_buttons)
    thread.start()


def populate_buttons(key_pressed=None):
    """
    When searching for a user, this function will execute. This will check and remove any buttons that do not match
    with the search query and will add any which do match with the search query. This will execute once per call, but
    not continuously.
    :return:
    """
    print(key_pressed)
    # Get search term
    query = entry.get().lower().strip()
    # Search inside the students list
    for index, local_student in enumerate(students):
        # Create button below the previous button (or below entry fields) if the student name starts with the search
        # query. However, if the button already exists (with a student existing in buttons), don't execute.
        if local_student.name.lower().strip().startswith(query) and not local_student in buttons:
            # Create a button with a command that gets the student assigned to the button.
            button = customtkinter.CTkButton(scrollable_frame, text=local_student.name,
                                             command=lambda: manage_student(local_student))
            button.grid(row=index, column=0)
            buttons[local_student] = button
        # If there exists a button for a student but the student name no longer starts with the search query,
        # then the button needs to be destroyed.
        # Also, remove the student from the buttons' dictionary.
        elif local_student.name in buttons and not local_student.name.lower().strip().startswith(query):
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
    win.unbind("<Key>", "button_creator_setup()")
    clear_screen()
    main_frame = customtkinter.CTkFrame(win, fg_color="transparent")
    main_frame.pack()
    title = customtkinter.CTkLabel(main_frame, text="Manage Student", font=("font1", 25))
    title.grid(row=0, column=0, columnspan=4)
    info_frame = customtkinter.CTkScrollableFrame(main_frame, label_text="Member Information")
    info_frame.grid(row=1, column=0, ipadx=8, ipady=8, padx=10  )
    volunteer_hours_label = customtkinter.CTkLabel(info_frame, text="Volunteer Hours: Not implemented")
    volunteer_hours_label.grid(row=0, column=0, padx=5, pady=5)
    tutoring_hours_label = customtkinter.CTkLabel(info_frame, text="Tutoring Hours: Not implemented")
    tutoring_hours_label.grid(row=1, column=0, padx=5, pady=5)
    club_standing_label = customtkinter.CTkLabel(info_frame, text="Club Standing: Not implemented")
    club_standing_label.grid(row=2, column=0, padx=5, pady=5)
    notes_label = customtkinter.CTkLabel(info_frame, text="Notes: Not implemented")
    notes_label.grid(row=3, column=0, padx=5, pady=5)

    actions_frame = customtkinter.CTkFrame(main_frame)
    actions_frame.grid(row=1, column=1, ipadx=8, ipady=8, padx=10)
    actions_frame_title = customtkinter.CTkLabel(actions_frame, text="Actions")
    actions_frame_title.grid(row=0, column=0)
    edit_volunteer_entries_button = customtkinter.CTkButton(actions_frame, text="Edit Volunteering Entries",
                                                            command=edit_volunteer_entries)
    edit_volunteer_entries_button.grid(row=1, column=0, padx=5, pady=5)
    edit_tutoring_entries_button = customtkinter.CTkButton(actions_frame, text="Edit Tutoring Entries",
                                                           command=edit_tutoring_entries)
    edit_tutoring_entries_button.grid(row=2, column=0, padx=5, pady=5)

    edit_student_information_button = customtkinter.CTkButton(actions_frame, text="Edit Student Information",
                                                              command=edit_student_information)
    edit_student_information_button.grid(row=3, column=0, padx=5, pady=5)
    manage_club_standing_button = customtkinter.CTkButton(actions_frame, text="Manage Club Standing",
                                                          command=manage_club_standing)
    manage_club_standing_button.grid(row=4, column=0, padx=5, pady=5)


def manage_club_standing():
    """
    Provides options to add a flag to a member denoting their current status within the club. This is where people can
    be manually changed to be in good standing, poor standing, tenuous standing, or eligible for cords.
    :return:
    """


def edit_student_information():
    """
    Allows changes to personal information within the system. This can change the displayed email address, name, or
    grade. This does not change information inside of the spreadsheet, rather just what is displayed within the program.
    :return:
    """


def edit_volunteer_entries():
    """
    Allows for changes to entries. This can change the contents of the spreadsheet, or it can create a new spreadsheet
    with all the changes logged within it.
    :return:
    """


def edit_tutoring_entries():
    """
    Allows for changes to entries. This can change the contents of the spreadsheet, or it can create a new spreadsheet
    with all the changes logged within it.
    :return:
    """


clear_screen()
menu()
win.mainloop()
