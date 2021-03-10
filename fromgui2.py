from tkinter import *
##from phones import *
from main import zoomauto
from data import lst1

def save():
    f = open("data.py", "w")
    f.write("lst1= [\n")
    f.close()
    f = open("data.py", "a")
    for lst in lst1:
        f.write("\t[")
        for list_d in lst:
            f.write("'{}', ".format(list_d))
        f.write("],\n")
    f.write("]")
    f.close()


def which_selected():
    print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def add_entry():
    lst1.append([fnamevar.get(), lnamevar.get(), phonevar.get()])
    set_select()


def update_entry():
    lst1[which_selected()] = [fnamevar.get(),
                                   lnamevar.get(),
                                   phonevar.get()]

def delete_entry():
    del lst1[which_selected()]
    set_select()


def load_entry():
    fname, lname, phone = lst1[which_selected()]
    fnamevar.set(fname)
    lnamevar.set(lname)
    phonevar.set(phone)


def click():
    mylabel=Label(win, zoomauto())
    mylabel.pack()


def make_window():
    global fnamevar, lnamevar, phonevar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Meeting Link").grid(row=0, column=0, sticky=W)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar)
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Starting Time").grid(row=1, column=0, sticky=W)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar)
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Ending Time").grid(row=2, column=0, sticky=W)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar)
    phone.grid(row=2, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2, text=" Add  ", command=add_entry)
    b2 = Button(frame2, text="Update", command=update_entry)
    b3 = Button(frame2, text="Delete", command=delete_entry)
    b4 = Button(frame2, text="Load  ", command=load_entry)
    b5 = Button(frame2, text="Refresh", command=set_select)
    b6 = Button(frame2, text="Save", command=save)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)
    b6.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll1 = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll1.set, height=6)
    scroll1.config(command=select.yview)
    scroll1.pack(side=RIGHT, fill=Y)
    scroll2 = Scrollbar(frame3, orient=HORIZONTAL)
    select = Listbox(frame3, xscrollcommand=scroll2.set, width=25)
    scroll2.config(command=select.xview)
    scroll2.pack(side=BOTTOM, fill=X)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    frame4 = Frame(win)       # select of names
    frame4.pack()
    # e=Entry(root,width=30)
    # e.pack()
    # e.insert(0,"")

    mybtn=Button(frame4,text="launch meetings",bg="grey",command=click)
    mybtn.pack()
    return win


def set_select():
    lst1.sort(key=lambda record: record[1])
    select.delete(0, END)
    for fname, lname, phone in lst1:
        select.insert(END, "{0}, {1}".format(lname, fname))


win = make_window()
win.title("ZOOM AUTOMATION")
win.iconbitmap("zoom_icon.ico")
win.geometry('400x400')

set_select()
win.mainloop()
