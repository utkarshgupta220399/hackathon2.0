#LOGIN DATA - FACULTY
login={"CSELECT01":["0001","Kamal Mehta"],"CSELECT02":["0002","Aakanksha Choubey"],"CSELECT03":["0003","Abhishek Dewangan"],
       "CSELECT04":["0004","Rajesh Tiwari"],"CSELECT05":["0005","K.K. Pandey"],"CSELECT06":["0006","Manjula Swarnakar"],
       "CSELECT07":["0007","Yamini Chouhan"], "CSELECT08":["0008","Siddharth Choubey"], "CSELECT09":["0009","Samta Gajbhiye"],
       "CSELECT10": ["0010", "Yogesh Sahu"], "CSELECT11":["0011","Megha Mishra"], "CSELECT12":["0012","Vishnu Mishra"],
       "CSELECT13": ["0013", "Sampada Massey"], "CSELECT14":["0014","Prageet Vajpayee"]}

login_student = {"CSESTUD01":["0001","A"], "CSESTUD02":["0002","B"], "CSESTUD03":["0003","C"]}

#CLASS A
timeTable_4A = [
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DM'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DM', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DM', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DM', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DM', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]
subjectwise_faculty_4A = {"CSA":"Aakanksha Choubey","DS":"Samta Gajbhiye","DM":"Manjula Swarnakar","OS":"Megha Mishra","DS LAB":"Samta Gajbhiye", "CM":"K.K. Pandey","OOPS":"Rajesh Tiwari", "H/W LAB":"Aakanksha Choubey", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Rajesh Tiwari"}

class_4A_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 2.5, 1.5, 8, 7],
    ["DS", 2, 2.5, 8, 10],
    ["CM", 2, 3.5, 9, 8],
    ["DM", 1, 1, 8, 6],
    ["OOPS", 3, 2, 7, 7],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0],
    ["DS LAB", 0, 0, 0, 0]
]

#CLASS B
timeTable_4B = [
    ['MON', 'DM', 'OS', 'OOPS LAB', 'OOPS LAB', 'B', 'CM', 'OOPS', 'CSA'],
    ['TUE', 'OS', 'DM', 'DS', 'CSA', 'R', 'OOPS', 'GUI LAB', 'GUI LAB'],
    ['WED', 'OOPS', 'CM', 'OS', 'DM', 'E', 'DS', 'DS LAB', 'DS LAB'],
    ['THU', 'DS', 'CSA', 'H/W LAB', 'H/W LAB', 'A', 'OS', 'CM', 'OOPS'],
    ['FRI', 'CM', 'OS', 'OOPS', 'CSA', 'K', 'DM', 'DS', 'DS'],
]

subjectwise_faculty_4B = {"OOPS":"Abhishek Dewangan","OS":"Megha Mishra", "CM":"K.K. Pandey", "DM":"Yogesh Sahu", "DS":"Yamini Chouhan", "CSA":"Kamal Mehta", "H/W LAB":"Kamal Mehta", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Abhishek Dewangan", "DS LAB": "Yamini Chouhan"}

class_4B_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 1, 3.5, 8, 10],
    ["DS", 0, 3.5, 3, 6],
    ["CM", 2, 3.5, 9, 8],
    ["DM", 1, 3.5, 5, 5],
    ["OOPS", 3.5, 3.5, 10, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0],
    ["DS LAB", 0, 0, 0, 0]
]

#CLASS C
timeTable_4C = [
    ['MON', 'DS', 'DS', 'DM', 'CM', 'B', 'OOPS', 'H/W LAB', 'H/W LAB'],
    ['TUE', 'CM', 'CSA', 'DS LAB', 'DS LAB', 'R', 'DM', 'OOPS', 'OS'],
    ['WED', 'CSA', 'OOPS', 'DS', 'DS', 'E', 'OS', 'DM', 'CM'],
    ['THU', 'OOPS', 'CSA', 'DM', 'CM', 'A', 'OS', 'DS', 'DS'],
    ['FRI', 'OS', 'OOPS', 'OOPS LAB', 'OOPS LAB', 'K', 'CSA', 'CM', 'DM'],
]
subjectwise_faculty_4C = {"DS":"Siddharth Choubey", "CSA":"Aakanksha Choubey", "CM":"Yogesh Sahu", "DM":"Manjula Swarnakar", "OS":"Megha Mishra", "OOPS":"Abhishek Dewangan", "H/W LAB":"Prageet Vajpayee", "GUI LAB":"Sampada Massey", "OOPS LAB":"Abhishek Dewangan", "DS LAB": "Siddharth Choubey"}

class_4C_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 2.5, 1.5, 8, 7],
    ["DS", 1, 4, 10, 10],
    ["CM", 1, 3.5, 5, 5],
    ["DM", 1, 1, 8, 6],
    ["OOPS", 3.5, 3.5, 10, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0],
    ["DS LAB", 0, 0, 0, 0]
]

def preference(tt,subject_faculty,temp):
    global day
    global section
    for i in tt:
        if i[0] == day:
            for j in range(9):
                if j in temp:
                    if i.count(i[j])>1:
                        i[j]= subject_faculty[1][0]
                    else:
                        i[j] = subject_faculty[0][0]
            break
    arr = []
    for row in tt:
        if row[0] == day:
            for i in temp:
                arr.append(row[i])
    for i in range(0, len(temp)):
        if temp[i] >= 5:
            temp[i] = temp[i] -1
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=\nDay-%s\nSection-%s\nLecture-%s\nSubject-%s\n%s&language=english&route=p&numbers=9171039045" %(day, section, temp, arr, "has been updated.") 
    headers = {
    'authorization': "9ghEGQ3pI8FquHZo5lMi2XtJK07x6AndPVevjYNfDBkmsCzULb5q3sBDuHIo29hQRUbNJXr1S4FwmzAg",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

# Print TT
"""
def printTable(table):
    for i in range(0, 6):
        for j in range(0, 9):
            print('{:^18}'.format(table[i][j]), end = "")
        print("\n")
    print("\n\n\n")
"""



#LIBRARIES
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

#FUNCITONS

#1
def raise_frame(frame):
    frame.tkraise()

#2
#LOGIN PAGE ENTRY
def getdata():
    global e1
    global e2
    e1 = user_.get()
    e2 = pass_.get()
    if e1[0:7] == "CSESTUD":
        student_validation()
    else:
        validation()

#3

def student_validation():
    flag=0
    for key,value in login_student.items():
        if (e1 == key):
            if (e2 == value[0]):
                flag=1
                break
            else:
                flag=0
        else:
             flag=0
    if flag==0:
        messagebox.showerror("Unauthorized Accesss", "Incorrect User id or Password")
    else:
        def raise_frame(frame):
            frame.tkraise()
        root = tk.Toplevel()
        f1 = tk.Frame(window)
        f2 = tk.Frame(window)
        root.title('SSTC Automatic Time-Table Generator')
        root.geometry("1300x750")
        root.configure(bg = '#002248')
        for frame in (f1, f2):
            frame.pack()
        logo_nex = tk.PhotoImage(file = "sstc.png")
        logo_labe = tk.Label(root, image = logo_nex)
        logo_labe.image = logo_nex
        logo_labe.pack(pady = 50)
        sect = login_student[e1][1]
        def display_time_table(timetable):
            frame = tk.Frame(root)
            frame.pack()
            style = ttk.Style(root)
            style.theme_use("clam")
            style.configure("Treeview", background="#002248", fieldbackground="#002248", foreground="white")
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 5, show = "headings")
            tree.pack(side = 'left')
            tree.heading(1, text="Day")
            tree.heading(2, text="Lecture 1")
            tree.heading(3, text="Lecture 2")
            tree.heading(4, text="Lecture 3")
            tree.heading(5, text="Lecture 4")
            tree.heading(6, text="")
            tree.heading(7, text="Lecture 5")
            tree.heading(8, text="Lecture 6")
            tree.heading(9, text="Lecture 7")
            tree.column(1, width = 100, anchor = "center")
            tree.column(2, width = 100, anchor = "center")
            tree.column(3, width = 100, anchor = "center")
            tree.column(4, width = 100, anchor = "center")
            tree.column(5, width = 100, anchor = "center")
            tree.column(6, width = 100, anchor = "center")
            tree.column(7, width = 100, anchor = "center")
            tree.column(8, width = 100, anchor = "center")
            tree.column(9, width = 100, anchor = "center")
            for val in timetable:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6], val[7], val[8]))
        def destruction():
            root.destroy()
            user_.delete(0, 'end')
            pass_.delete(0, 'end')
        tk.Button(root, text="Logout", command = destruction).pack()
        if sect == 'A':
            display_time_table(timeTable_4A)
        elif sect == 'B':
            display_time_table(timeTable_4B)
        elif sect == 'C':
            display_time_table(timeTable_4C)

def validation():
    flag=0
    for key,value in login.items():
        if (e1 == key):
            if (e2 == value[0]):
                flag=1
                break
            else:
                flag=0
        else:
             flag=0
    if flag==0:
        messagebox.showerror("Unauthorized Accesss", "Incorrect User id or Password")
    else:
        #New Frame after login
        def raise_frame(frame):
            frame.tkraise()

        root = tk.Toplevel()
        f1 = tk.Frame(window)
        f2 = tk.Frame(window)
        root.title('SSTC Automatic Time-Table Generator')
        root.geometry("1300x750")
        root.configure(bg = '#002248')
        for frame in (f1, f2):
            frame.pack()
        logo_next = tk.PhotoImage(file = "sstc.png")
        logo_label = tk.Label(root, image = logo_next)
        logo_label.pack(pady = 50)
        #Dropdown Lists for Class & Day
        section = ""
        day = ""
        def display_time_table(timetable):
            frame = tk.Frame(root)
            frame.pack()
            style = ttk.Style(root)
            style.theme_use("clam")
            style.configure("Treeview", background="#002248", fieldbackground="#002248", foreground="white")
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 5, show = "headings")
            tree.pack(side = 'left')
            tree.heading(1, text="Day")
            tree.heading(2, text="Lecture 1")
            tree.heading(3, text="Lecture 2")
            tree.heading(4, text="Lecture 3")
            tree.heading(5, text="Lecture 4")
            tree.heading(6, text="")
            tree.heading(7, text="Lecture 5")
            tree.heading(8, text="Lecture 6")
            tree.heading(9, text="Lecture 7")
            tree.column(1, width = 100, anchor = "center")
            tree.column(2, width = 100, anchor = "center")
            tree.column(3, width = 100, anchor = "center")
            tree.column(4, width = 100, anchor = "center")
            tree.column(5, width = 100, anchor = "center")
            tree.column(6, width = 100, anchor = "center")
            tree.column(7, width = 100, anchor = "center")
            tree.column(8, width = 100, anchor = "center")
            tree.column(9, width = 100, anchor = "center")
            for val in timetable:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6], val[7], val[8]))
        def display_short_table(timetable):
            frame = tk.Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 1, show = "headings")
            tree.pack(side = 'left')
            tree.heading(1, text="Day")
            tree.heading(2, text="Lecture 1")
            tree.heading(3, text="Lecture 2")
            tree.heading(4, text="Lecture 3")
            tree.heading(5, text="Lecture 4")
            tree.heading(6, text="")
            tree.heading(7, text="Lecture 5")
            tree.heading(8, text="Lecture 6")
            tree.heading(9, text="Lecture 7")
            tree.column(1, width = 100, anchor = "center")
            tree.column(2, width = 100, anchor = "center")
            tree.column(3, width = 100, anchor = "center")
            tree.column(4, width = 100, anchor = "center")
            tree.column(5, width = 100, anchor = "center")
            tree.column(6, width = 100, anchor = "center")
            tree.column(7, width = 100, anchor = "center")
            tree.column(8, width = 100, anchor = "center")
            tree.column(9, width = 100, anchor = "center")
            tree.insert('', 'end', values = (timetable[0], timetable[1], timetable[2], timetable[3], timetable[4], "BREAK", timetable[6], timetable[7], timetable[8]))
            secondpage()

        def display(tt):
            for i in range(0, 5):
                for j in range(0, 9):
                    print('{:^18}'.format(tt[i][j]), end = "")
                print("\n")
            print("\n\n\n")

        def secondpage():
            global e1
            global section
            if section=='A':
                access(timeTable_4A, subjectwise_faculty_4A, login[e1][1])
            elif section=='B':
                access(timeTable_4B, subjectwise_faculty_4B, login[e1][1])
            else:
                access(timeTable_4C, subjectwise_faculty_4C, login[e1][1])

        def access(tt, faculty_dict, faculty_name):
            global day
            global section
            tempi = []
            for row in  tt:
                if row[0]==day:
                    tempi = row         #that particular days tt
                    break
            count = 0
            store_occurences = []               #Stores all lecture indices in selected row for that faculty
            for j in tempi:
                if count==0 or count==5:
                    count+=1
                else:
                    if faculty_dict[j] == faculty_name:
                        store_occurences.append(count)
                    count += 1
            if section == "A":
                preference(timeTable_4A, class_4A_faculty_details, store_occurences)
            elif section =='B':
                preference(timeTable_4B, class_4B_faculty_details, store_occurences)
            elif section=="C":
                preference(timeTable_4C, class_4C_faculty_details, store_occurences)
        
        def fetchlogindata():
            global section
            global day
            section = variable_class.get()
            day = variable_day.get()
            if section == "A":
                display_time_table(timeTable_4A)
            elif section == "B":
                display_time_table(timeTable_4B)
            elif section == "C":
                display_time_table(timeTable_4C)


        def newwin():
            global section
            global day
            section = variable_class.get()
            day = variable_day.get()
            if section == "A":
                copyTT = timeTable_4A
                for a in range(0, 5):
                    if day == copyTT[a][0]:
                        temp = copyTT[a]
                        display_short_table(temp)
            elif section == "B":
                copyTT = timeTable_4B
                for a in range(0, 5):
                    if day == copyTT[a][0]:
                        temp = copyTT[a]
                        display_short_table(temp)
            elif section == "C":
                copyTT = timeTable_4C
                for a in range(0, 5):
                    if day == copyTT[a][0]:
                        temp = copyTT[a]
                        display_short_table(temp)
        #DROPDOWN LIST
        def destruction():
            root.destroy()
            user_.delete(0, 'end')
            pass_.delete(0, 'end')
        tk.Button(root, text="Logout", command = destruction).pack(pady=3)
        variable_class = tk.StringVar(root)
        variable_class.set("Class")

        w = tk.OptionMenu(root, variable_class, "A", "B", "C")
        w.pack()
        
        variable_day = tk.StringVar(root)
        variable_day.set("Day")

        v = tk.OptionMenu(root, variable_day, "MON", "TUE", "WED", "THU", "FRI")
        v.pack(pady=5)
        displaybutton = tk.Button(root, text="Display TIme Table", command=fetchlogindata)
        displaybutton.pack(pady=5)
        
        editbutton = tk.Button(root, text="Edit", command=newwin)
        editbutton.pack(pady=5)

    
        #End of new frame
        root.mainloop()

#WINDOW CONFIGURATIONS
window = tk.Tk()
window.title('SSTC Automatic Time-Table Generator')
window.geometry("1300x750")
window.configure(bg = '#002248')

#LOGIN PAGE SSTC LOGO
logo = tk.PhotoImage(file = "sstc.png")
default_image_label = tk.Label(window, image = logo)
default_image_label.pack(pady = 50)

#LOGIN PAGE HEADING
w = tk.Label(window, text="Shri Shankaracharya Technical Campus", font = ('Comic Sans MS', 25), bg = '#002248', fg = '#FFFFFF')
w.pack(anchor = "center")
v = tk.Label(window, text="Automatic Time-Table Generator", font = ('Comic Sans MS', 20), bg = '#002248', fg = '#FFFFFF')
v.pack(anchor = "center")

e1 = ""
e2 = ""

user_name = tk.Label(text = "Username: ", bg = '#002248', fg = '#FFFFFF')
user_name.pack(anchor = "center")
user_ = tk.Entry(window)
user_.pack(anchor = "center")
password = tk.Label(text = "Password: ", bg = '#002248', fg = '#FFFFFF')
password.pack(anchor = "center")
pass_ = tk.Entry(window, show = '*', width = 20)
pass_.pack(anchor = "center")
login_button = tk.Button(text = "Login")
login_button = tk.Button(window, text = "Login", command = getdata)
login_button.pack(pady = 10)

window.mainloop()
