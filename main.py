from tkinter import *
from tkinter.scrolledtext import *
from sqlite3 import *
from tkinter.messagebox import *
import socket
import requests
import bs4
import matplotlib.pyplot as plt



try:
    socket.create_connection(("www.google.com", 80))
    print("Connected")
    res = requests.get("https://ipinfo.io")
    data = res.json()
    city = data['city']
    a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2 = "&q=" + city
    a3 = "&appid=c6e315d09197cec231495138183954bd"
    api_address =  a1 + a2  + a3
    res1 = requests.get(api_address)
    data1 = res1.json()
    temp = data1['main']['temp']

except OSError as e:
    print("Issue: ", e)


res = requests.get("https://www.brainyquote.com/quote_of_the_day")
soup = bs4.BeautifulSoup(res.text, "lxml")

data = soup.find("img", {"class" : "p-qotd"})
text = data['alt']


def f1():
    main.withdraw()
    adst.deiconify()
    adst_entRno.delete(0, END)
    adst_entName.delete(0, END)
    adst_entMarks.delete(0, END)
    adst_entRno.focus()

def f2():
    adst.withdraw()
    main.deiconify()
def f3():
    main.withdraw()
    vist.deiconify()
    vist_stData.delete(1.0, END)
    con = None
    try:
        con = connect("Student.db")
        cursor = con.cursor()
        sql = "select * from student";
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info + "rno.:" + str(d[0]) + "  name:" + str(d[1]) + "    marks:" + str(d[2]) + "\n"
        vist_stData.insert(INSERT, info)
    except Exception as e:
        showerror("failure", e)
    finally:
        if con is not None:
            con.close()
def f4():
    vist.withdraw()
    main.deiconify()
def f5():
    main.withdraw()
    udst.deiconify()
    udst_entRno.delete(0, END)
    udst_entName.delete(0, END)
    udst_entMarks.delete(0, END)
    udst_entRno.focus()

def f6():
    udst.withdraw()
    main.deiconify()
def f7():
    main.withdraw()
    dels.deiconify()
    del_entRno.delete(0, END)
    del_entRno.focus()

def f8():
    dels.withdraw()
    main.deiconify()
def f9():
    con = None
    try:
        con = connect("Student.db")
        cursor = con.cursor()
        sql = "insert into student values('%d','%s','%d')"
        r = adst_entRno.get()
        name = adst_entName.get()
        m = adst_entMarks.get()
        if r.isalpha() == True:
            raise Exception("Roll number can only contain positive integers")
        elif r == '':
            raise Exception("Roll cannot be empty")
        rno = int(r)
        if rno<1:
            raise Exception("Roll number cannot be negative")
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        elif len(name)<2:
            raise Exception("Name should contain alphabets with min. length 2")
        elif name.isalpha() != True:
            raise Exception("Name should only contain alphabets")
        if m.isalpha() == True:
            raise Exception("Marks can only contain integers")
        elif m == '':
            raise Exception("Marks cannot be empty")
        marks = int(m)
        if marks<0 or marks>100:
            raise Exception("Marks should be in range of 0 - 100")
        args = (rno, name, marks)
        cursor.execute(sql %args)
        con.commit()
        showinfo("Success", "Record added")
    except ValueError:
        showerror("Failure", "Only Integers allowed in Roll no. and Marks")
    except IntegrityError:
        showerror("Failure", "Roll number already exists")
    except Exception as e:
        showerror("Failure", e)
        con.rollback()
    finally:
        if con is not None:
            con.close()
def f10():
    con = None
    try:
        con = connect("Student.db")
        cursor = con.cursor()
        sql = "update student set name = '%s', marks = '%r' where rno = '%r'"
        r = udst_entRno.get()
        name = udst_entName.get()
        m = udst_entMarks.get()
        if r.isalpha() == True:
            raise Exception("Roll number can only contain positive integers")
        elif r == '':
            raise Exception("Roll number cannot be empty")
        rno = int(r)
        if rno<1:
            raise Exception("Roll number cannot be negative")
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        elif len(name)<2:
            raise Exception("Name should contain alphabets with min. length 2")
        elif name.isalpha() != True:
            raise Exception("Name should only contain alphabets")
        if m.isalpha() == True:
            raise Exception("Marks can only contain integers")
        elif m == '':
            raise Exception("Marks cannot be empty")
        marks = int(m)
        if marks<0 or marks>100:
            raise Exception("Marks should be in range of 0 - 100")
        args = (name, marks, rno)
        cursor.execute(sql %args)
        if cursor.rowcount >= 1:
            con.commit()
            showinfo("Success", "Record updated")
        else:
            showerror("Failure", "Roll number does not exists")
    except ValueError:
        showerror("Failure", "Only Integers allowed in Roll no. and Marks")
    except Exception as e:
        con.rollback()
        showerror("Failure", e)
    finally:
        if con is not None:
            con.close()
def f11():
    con = None
    try:
        con = connect("Student.db")
        cursor = con.cursor()
        sql = "delete from student where rno = '%r'"
        r = del_entRno.get()
        if r.isalpha() == True:
            raise Exception("Roll number can only contain positive integers")
        elif r == '':
            raise Exception("Roll number cannot be empty")
        rno = int(r)
        if rno<1:
            raise Exception("Roll number cannot be negative")
        args = (rno)
        cursor.execute(sql %args)
        if cursor.rowcount >= 1:
            con.commit()
            showinfo("Success", "Record deleted")
        else:
            showerror("Failure", "Roll number does not exists")
    except ValueError:
        showerror("Failure", "Only integers allowed")
    except Exception as e:
        con.rollback()
        showerror("Failure", e)
    finally:
        if con is not None:
            con.close()
def f12():
    main.withdraw()
    con = None
    try:
        con = connect("Student.db")
        cursor = con.cursor()
        sql = "select * from student";
        cursor.execute(sql)
        data = cursor.fetchall()
        name = []
        marks = []
        for d in data:
            name.append(d[1])
            marks.append(d[2])
        plt.plot(name, marks, marker = 'o', markersize = 10, label = 'Chart',linewidth = 2)
        plt.xlabel("Names")
        plt.ylabel("Marks")
        plt.title("Student data")
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        showerror("failure", e)
    finally:
        if con is not None:
            con.close()




main = Tk()
main.title("S.M.S")
main.geometry("570x500+420+130")
main.configure(background = 'gray94')

main_lbl = Label(main, text = "Student Management System", font = ('Corbel Light', 20, 'bold'))
btnAdd = Button(main, text="Add", width=10, font = ('Corbel Light', 18), command = f1)
btnView = Button(main, text="View", width=10, font = ('Corbel Light', 18), command = f3)
btnUpdate = Button(main, text="Update", width=10, font = ('Corbel Light', 18), command = f5)
btnDelete = Button(main, text="Delete", width=10, font = ('Corbel Light', 18), command = f7)
btnCharts = Button(main, text="Charts", width=10, font = ('Corbel Light', 18), command = f12)
main_lblloc = Label(main, text = "Location: ", font = ('Corbel Light', 10, 'bold'))
main_lblcity = Label(main, text = city, font = ('Corbel Light', 10))
main_lbltemp = Label(main, text = "Temperature: ", font = ('Corbel Light', 10, 'bold'))
main_lbldegrees = Label(main, text = temp, font = ('Corbel Light', 10))
main_lblquote = Label(main, text = "QOTD: ", font = ('Corbel Light', 10, 'bold'))
main_lblqotd = Label(main, text = text, font = ('Corbel Light', 10, 'bold'), wraplength = 500, justify = 'left')

main_lbl.pack(pady = 10)
btnAdd.pack(pady = 10)
btnView.pack(pady = 10)
btnUpdate.pack(pady = 10)
btnDelete.pack(pady = 10)
btnCharts.pack(pady = 10)
main_lblloc.place(x = 0, y = 430)
main_lblcity.place(x = 60, y = 430)
main_lbltemp.place(x = 200, y = 430)
main_lbldegrees.place(x = 290, y = 430)
main_lblquote.place(x = 0, y = 450)
main_lblqotd.place(x = 45, y = 450)

adst = Toplevel(main)
adst.title("Add St. ")
adst.geometry("500x500+400+100")

adst_lblRno = Label(adst, text = "Enter rno", font = ('Yu Gothic Light', 18))
adst_entRno = Entry(adst, bd = 2, font = ('Yu Gothic Light', 18))
adst_lblName = Label(adst, text = "Enter name", font = ('Yu Gothic Light', 18))
adst_entName = Entry(adst, bd = 2, font = ('Yu Gothic Light', 18))
adst_lblMarks = Label(adst, text = "Enter Marks", font = ('Yu Gothic Light', 18))
adst_entMarks = Entry(adst, bd = 2, font = ('Yu Gothic Light', 18))
adst_btnSave = Button(adst, text = "Save", font = ('Corbel Light', 18), command = f9)
adst_btnBack = Button(adst, text = "Back", font = ('Corbel Light', 18), command = f2)

adst_lblRno.pack(pady = 10)
adst_entRno.pack(pady = 10)
adst_lblName.pack(pady = 10)
adst_entName.pack(pady = 10)
adst_lblMarks.pack(pady = 10)
adst_entMarks.pack(pady = 10)
adst_btnSave.pack(pady = 10)
adst_btnBack.pack(pady = 10)
adst.withdraw()


vist = Toplevel(main)
vist.title("View St. ")
vist.geometry("500x500+400+100")

vist_stData = ScrolledText(vist, width = 34, height = 15, font = ("courier", 18))
vist_btnBack = Button(vist, text = "Back", font = ('Corbel Light', 18), command = f4)

vist_stData.pack(pady = 10)
vist_btnBack.pack(pady = 10)
vist.withdraw()


udst = Toplevel(main)
udst.title("Update St. ")
udst.geometry("500x500+400+100")

udst_lblRno = Label(udst, text = "Enter rno", font = ('Yu Gothic Light', 18))
udst_entRno = Entry(udst, bd = 2, font = ('Yu Gothic Light', 18))
udst_lblName = Label(udst, text = "Enter name", font = ('Yu Gothic Light', 18))
udst_entName = Entry(udst, bd = 2, font = ('Yu Gothic Light', 18))
udst_lblMarks = Label(udst, text = "Enter Marks", font = ('Yu Gothic Light', 18))
udst_entMarks = Entry(udst, bd = 2, font = ('Yu Gothic Light', 18))
udst_btnSave = Button(udst, text = "Save", font = ('Corbel Light', 18), command = f10)
udst_btnBack = Button(udst, text = "Back", font = ('Corbel Light', 18), command = f6)

udst_lblRno.pack(pady = 10)
udst_entRno.pack(pady = 10)
udst_lblName.pack(pady = 10)
udst_entName.pack(pady = 10)
udst_lblMarks.pack(pady = 10)
udst_entMarks.pack(pady = 10)
udst_btnSave.pack(pady = 10)
udst_btnBack.pack(pady = 10)
udst.withdraw()


dels = Toplevel(main)
dels.title("Delete St.")
dels.geometry('500x500+400+100')

del_lblRno = Label(dels, text = "Enter rno", font = ('Yu Gothic Light', 18))
del_entRno = Entry(dels, bd = 2, font = ('Yu Gothic Light', 18))
del_btnDelete = Button(dels, text = "Delete", font = ('Corbel Light', 18), command = f11)
del_btnBack = Button(dels, text = "Back", font = ('Corbel Light', 18), command = f8)

del_lblRno.pack(pady = 10)
del_entRno.pack(pady = 10)
del_btnDelete.pack(pady = 10)
del_btnBack.pack(pady = 10)
dels.withdraw()

main.mainloop()
