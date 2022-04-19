from tkinter import *
from config import auth
from sqlalchemy import create_engine
from PIL import ImageTk,Image

engine = create_engine('postgresql://{}:{}@localhost/university1'.format(auth['user'],auth['password']),echo=True)

cursor = engine.connect()



query = '''
select *
from students
'''

querySALL = '''
select return_students()
'''


root = Tk()

root.geometry('800x600-600-200')
root.title("ННГУ имени Александра Невского")


canvas = Canvas(root, width = 800, height = 600)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("2.png"))
canvas.create_image(600, 430, anchor=W, image=img)



#button

def changer(btn, entry, entry2):
    def change():
        btn['text'] = 'OK'
        btn['bg'] = '#000000'
        btn['fg'] = '#ffffff'
        btn['activebackground'] = '#555555'
        btn['activeforeground'] = '#Aadd55'
        print(f"DEBUG:: LOGIN = {entry.get()}")
        print(f"DEBUG:: PASS = {entry2.get()}")
    return change


#return every student
#1. set query = select return_students()
#2. launch query
#3. print query




#personel_shower
def studentshower(btn,entry):
    def showstudent():
        print(f"SEARCH FOR STUDENT SURNAME COMMAND INPUT\n")
        query = (f"select show_student({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return showstudent


#student_remover
def studentremover(btn,entry):
    def removestudent():
        print(f"REMOVE FROM STUDENT SURNAME COMMAND INPUT\n")
        query = (f"select delete_student({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return removestudent


#student_show_all
def studentsprinter(btn):
    def printstudents():
        print(f"PRINT STUDENTS COMMAND INPUT\n")
        query = '''
        select return_students()
        '''
        result = cursor.execute(query)
        print(result)
        print(list(result))

    return printstudents

#student_add
def studentadder(btn,entry):
    def addstudent():
        print(f"ADD STUDENT COMMAND INPUT\n")
        query = (f"select insert_student3({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return addstudent

#personel_remover
def personelremover(btn,entry):
    def removepersonel():
        print(f"REMOVE FROM PERSONEL NAME COMMAND INPUT\n")
        query = (f"select delete_personel({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return removepersonel

#personel_add
def personeladder(btn,entry):
    def addpersonel():
        print(f"ADD PERSONEL COMMAND INPUT\n")
        query = (f"select insert_personel({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return addpersonel


#personel_show_all
def personelprinter(btn):
    def printpersonel():
        print(f"PRINT PERSONEL COMMAND INPUT\n")
        query = '''
        select return_personel()
        '''
        result = cursor.execute(query)
        print(result)
        print(list(result))

    return printpersonel

#personel_shower
def personelshower(btn,entry):
    def showpersonel():
        print(f"SEARCH FOR PERSONEL NAME COMMAND INPUT\n")
        query = (f"select show_personel({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return showpersonel




#exams_purge_all
def examspurger(btn):
    def purgeexams():
        print(f"PURGE EXAMS COMMAND INPUT\n")
        query = '''
        select purge_exams()
        '''
        result = cursor.execute(query)
        print(result)
        print(list(result))

    return purgeexams

#exams_show_all
def examsprinter(btn):
    def printexams():
        print(f"PRINT EXAMS COMMAND INPUT\n")
        query = '''
        select return_exams()
        '''
        result = cursor.execute(query)
        print(result)
        print(list(result))

    return printexams



#grade_add
def gradeadder(btn,entry):
    def addgrade():
        print(f"ADD GRADE COMMAND INPUT\n")
        query = (f"select insert_grades({entry.get()})")

        result = cursor.execute(query)
        print(result)
        print(list(result))

    return addgrade

#grades_show_all
def gradesprinter(btn):
    def printgrades():
        print(f"PRINT GRADES COMMAND INPUT\n")
        query = '''
        select return_grades()
        '''
        result = cursor.execute(query)
        print(result)
        print(list(result))

    return printgrades


l1 = Label(text="Мега GUI v.3001",font='Arial 32')
l1.place(anchor="center",relx=0.5,rely=0.05)
l1['bg'] = '#ffaaaa'

#entry1(lgn)
e1 = Entry(width=15)
e1.insert(0,'cool-user')
e1.pack()
e1.place(anchor="center",relx=0.5,rely=0.15)

#entry2(pwd)
e2 = Entry(width=15)
e2.insert(0,'cool-pass')
e2.pack()
e2.place(anchor="center",relx=0.5,rely=0.2)


#btn1(login)
b1 = Button(text='Login', width=5,height=1)
b1.place(anchor="center",relx=0.5,rely=0.3)
b1.config(command=changer(b1,e1,e2))


#btn2(create_bd)
b2 = Button (text='Create DB', width=10,height=1)
b2.place(anchor="center",relx=0.2,rely=0.3)

#btn3(remove_bd)
b3 = Button (text='Remove DB', width=10,height=1)
b3.place(anchor="center",relx=0.8,rely=0.3)


#entry3_search-main-field
e3 = Entry(width=30)
e3.insert(0,'sql')
e3.pack()
e3.place(anchor="center",relx=0.5,rely=0.9)

#--------------students
l2 = Label(text="Students",font='Arial 20')
l2.place(anchor="center",relx=0.1,rely=0.4)

Ssearch = Button (text='search', width=10,height=1)
Ssearch.place(anchor="center",relx=0.1,rely=0.5)
Ssearch.config(command=studentshower(Ssearch,e3))

Sadd = Button (text='add', width=10,height=1)
Sadd.place(anchor="center",relx=0.1,rely=0.55)
Sadd.config(command=studentadder(Sadd,e3))

Srm = Button (text='remove', width=10,height=1)
Srm.place(anchor="center",relx=0.1,rely=0.6)
Srm.config(command=studentremover(Srm,e3))

Sall = Button (text='show_all', width=10,height=1)
Sall.place(anchor="center",relx=0.1,rely=0.65)
Sall.config(command=studentsprinter(Sall))
#--------------


#--------------personel
l3 = Label(text="Personel",font='Arial 20')
l3.place(anchor="center",relx=0.3,rely=0.4)

Psearch = Button (text='search', width=10,height=1)
Psearch.place(anchor="center",relx=0.3,rely=0.5)
Psearch.config(command=personelshower(Psearch,e3))

Padd = Button (text='add', width=10,height=1)
Padd.place(anchor="center",relx=0.3,rely=0.55)
Padd.config(command=personeladder(Padd,e3))

Prm = Button (text='remove', width=10,height=1)
Prm.place(anchor="center",relx=0.3,rely=0.6)
Prm.config(command=personelremover(Prm,e3))

Pall = Button (text='show_all', width=10,height=1)
Pall.place(anchor="center",relx=0.3,rely=0.65)
Pall.config(command=personelprinter(Pall))
#--------------

#-------------- exams
l4 = Label(text="Exams",font='Arial 20')
l4.place(anchor="center",relx=0.5,rely=0.4)

Esearch = Button (text='search', width=10,height=1)
Esearch.place(anchor="center",relx=0.5,rely=0.5)

Eadd = Button (text='add', width=10,height=1)
Eadd.place(anchor="center",relx=0.5,rely=0.55)

Erm = Button (text='purgeAll', width=10,height=1)
Erm.place(anchor="center",relx=0.5,rely=0.6)
Erm.config(command=examspurger(Erm))

Eall = Button (text='show_all', width=10,height=1)
Eall.place(anchor="center",relx=0.5,rely=0.65)
Eall.config(command=examsprinter(Eall))


#-------------- grades
l5 = Label(text="Grades",font='Arial 20')
l5.place(anchor="center",relx=0.7,rely=0.4)

Gsearch = Button (text='search', width=10,height=1)
Gsearch.place(anchor="center",relx=0.7,rely=0.5)

Gadd = Button (text='add', width=10,height=1)
Gadd.place(anchor="center",relx=0.7,rely=0.55)
Gadd.config(command=gradeadder(Gadd,e3))

Grm = Button (text='remove', width=10,height=1)
Grm.place(anchor="center",relx=0.7,rely=0.6)

Gall = Button (text='show_all', width=10,height=1)
Gall.place(anchor="center",relx=0.7,rely=0.65)
Gall.config(command=gradesprinter(Gall))

####
#result= cursor.execute(query)
#print(result)
#print(list(result))

root.mainloop()