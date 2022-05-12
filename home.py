from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
# from tkcalendar import DateEntry,Calender
root=Tk()
root.geometry("1100x600")
root.resizable(False, False)

root.title("TALLY PRIME")

# p1 = PhotoImage(file = 'images/fbicon.png')
# root.iconphoto(False, p1)
curnt_period = Label(root, text="CURRENT PERIOD",fg="blue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="blue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-23", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",borderwidth=3,fg="blue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry", fg="blue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22",fg="black").place(x=340, y=140)
separator = ttk.Separator(root,orient='vertical')
separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
frame = Label(root, text="Gateway of Tally",bg="blue",fg="white",width=40,padx=20,pady=10).place(x=540, y=50)
frame1 = Frame(root, bg="black", width=305, height=540)
frame1.place(x=540, y=80)
frame2 = Frame(frame1, bg="skyblue", width=305, height=540)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Masters",bg="skyblue",fg="black",font="17").place(x=670,y=100)
def func1():
    screen1 = Toplevel(root)
    screen1.title('Create')
    screen1.geometry('500x500')

def purchaseacount():
    top=Toplevel(root)
    top.geometry("900x400")
    # top.config(bg="white")
    top.title("purchase account")


def profitloss():
    top=Toplevel(root)
    top.geometry("900x400")
    # top.config(bg="white")
    top.title("profit & loss")
 
    separator = ttk.Separator(top,orient='vertical')
    separator.place(relx=0.5,rely=0,relwidth=0,relheight=1)

    date = Label(top, text="Particulars", fg="black").place(x=40, y=40)
    cmpny = Label(top, text="ABC Pvt.Ltd",fg="black").place(x=350, y=20)
    date = Label(top, text="For 1-Apr-22", fg="black").place(x=350, y=40)

    opstock = Button(top, text="Opening Stock",command=create,fg="black", activebackground="yellow",height=1,border=0).place(x=40, y=80)
    
    purchase = Button(top, text="Purchase Account",command=purchaseacount,fg="black", activebackground="yellow",height=1,border=0).place(x=40, y=100)
    purammount = Label(top, text="31,25000", fg="black").place(x=350, y=100)
    directex = Button(top, text="Direct Expences",command=create,fg="black", activebackground="yellow",height=1,border=0).place(x=40, y=120)
    directexamo = Label(top, text="40,00000", fg="black").place(x=350, y=120)
    sum = Label(top, text="71,25000", fg="black").place(x=350, y=140)
    gross = Label(top, text="Gross loss", fg="black").place(x=40, y=180)
    grossum = Label(top, text="31,25000", fg="black").place(x=350, y=180)
    indirect = Button(top, text="indirect Expences",command=create,fg="black", activebackground="yellow",height=1,border=0).place(x=40, y=200)
    indirectsum = Label(top, text="31,25000", fg="black").place(x=350, y=200)

    total = Label(top, text="Total", fg="black").place(x=40, y=350)
    totalammount = Label(top, text="31,25000", fg="black").place(x=350, y=350)



    cmpny = Label(top, text="Particulars",fg="black").place(x=480, y=40)
    cmpny = Label(top, text="ABC Pvt.Ltd",fg="black").place(x=800, y=20)
    date = Label(top, text="For 1-Apr-22", fg="black").place(x=800, y=40)

    saleacc = Button(top, text="Sales Account",command=create,fg="black", activebackground="yellow",height=1,border=0).place(x=480, y=80)
    saleammountt = Label(top, text="31,25000", fg="black").place(x=800, y=350)
    
    sclstocke = Button(top, text="Closing Stock",command=create,fg="black", activebackground="yellow",height=1,border=0).place(x=480, y=100)
    purammount = Label(top, text="31,25000", fg="black").place(x=800, y=100)
    grosloss = Label(top, text="Gross Loss", fg="black").place(x=480, y=120)
    directexamo = Label(top, text="40,00000", fg="black").place(x=800, y=120)
    sum = Label(top, text="71,25000", fg="black").place(x=800, y=140)
    gross = Label(top, text="Nett Loss ", fg="black").place(x=480, y=180)
    grossum = Label(top, text="31,25000", fg="black").place(x=800, y=180)
    

    total = Label(top, text="Total", fg="black").place(x=480, y=350)
    totalammount = Label(top, text="31,25000", fg="black").place(x=800, y=350)

b1 = Button(root, text="Create", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=140)

b2 = Button(root, text="Alter", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=170)
b3 = Button(root, text="Chart of Accounts", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=200)

mstrs1 = Label(root, text="Transactions",bg="skyblue",fg="black",font="17").place(x=640,y=230)
b5 = Button(root, text="Vouchers", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=260)
b6 = Button(root, text="Day Book", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=290)
mstrs2 = Label(root, text="Utilities",bg="skyblue",fg="black",font="17").place(x=670,y=320)
b7 = Button(root, text="Banking", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=350)

mstrs3 = Label(root, text="Reports",bg="skyblue",fg="black",font="17").place(x=670,y=380)
b8 = Button(root, text="Balance Sheet", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=410)
b9 = Button(root, text="Profit & Loss", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=profitloss).place(x=630, y=440)
b10 = Button(root, text="Stock Summary", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=470)

b10 = Button(root, text="Ratio Analysis", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=630, y=500)
b11 = Button(root, text="Display More Reports", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1, command=func1).place(x=630, y=530)
             
frame3 = Frame(root, bg="skyblue", width=130, height=750)
frame3.place(x=950, y=0)
date = Button(frame3, text="Date", width=20, fg="black", font=(
    "impact", 8), command=func1, activebackground="yellow", activeforeground="red")
date.place(x=13, y=20)


def func2():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('Company')
    screen2.geometry('430x430')
    Label(screen2, text='List Of Companies',bg="blue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(screen2, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=40)
    sbmibtn2 = Button(screen2, text='Alter Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=70)
    sbmibtn3 = Button(screen2, text='Select Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=create, fg='black',font=('Arial',9),activebackground='yellow', width=30,border=0).place(x=240, y=130)


def create():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('Create Company')
    screen3.geometry('940x520')
    Label(screen3, text='COMPANY CREATION',bg="navyblue",font='17',fg="white",width=640).pack()
    global  Cname,Cmailing,Caddress, email,state,country,pcode,tphone,mphone,fax,site,symbol,format
    Cname = StringVar()
    Cmailing = StringVar()
    Caddress = StringVar()
    email = StringVar()
    state = StringVar()
    country = StringVar()
    pcode = IntVar()
    tphone = StringVar()
    mphone = StringVar()
    fax = StringVar()
    site = StringVar()
    symbol = StringVar()
    format = StringVar()
    
    
    cname = Label(screen3, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen3, textvariable=Cname,width=40).place(x=120, y=70)
    y1 = Label(screen3, text='Financial Year begining From:').place(x=450, y=70)
    # e2 = DateEntry(screen3,width=25)
    adrs1 = Label(screen3, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen3, textvariable=Cmailing, width=40).place(x=120, y=110)
    y2 = Label(screen3, text='Books Begining From:').place(x=450, y=110)
    adrs = Label(screen3, text='Address:').place(x=20, y=150)
    e4 = Entry(screen3,textvariable=Caddress,width=40).place(x=120, y=150)
    
company = Button(frame3, text="Company", width=20, fg="black", font=(
    "impact", 8), command=func2, activebackground="yellow", activeforeground="red").place(x=13, y=50)


root.mainloop()


