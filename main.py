from tkinter import *
import customtkinter
from time import sleep
import threading
import pickle

win = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")


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
    title_font = ("font1", 25)
    title = customtkinter.CTkLabel(win, text="Main Menu", font=title_font)
    title.grid(row=0, column=0)
    # haha mainframe
    main_frame = customtkinter.CTkFrame(win, height=300, corner_radius=10)
    main_frame.grid(row=1, column=0, ipady=200, rowspan=138)
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
    :return:
    """


    # thread = threading.Thread(target=function)
    # thread.start()


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


clear_screen()
menu()
win.geometry("420x400")
win.mainloop()

