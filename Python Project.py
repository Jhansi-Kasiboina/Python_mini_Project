




from tkinter import *
import pymysql
from tkinter import ttk

class StudentsInfo:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1550x800')
        title1 = Label(self.root, text='Welcome To Students Details Page', font=('Cooper Black', 50), bd=4, relief=RAISED, bg= 'green', fg= 'white')
        title1.pack(fill='x')

        self.rollnoVar = StringVar()
        self.fnameVar= StringVar()
        self.lname= StringVar()
        self.email= StringVar()
        self.mobile= StringVar()
        self.cname= StringVar()
        self.fee= StringVar()
        self.iname= StringVar()
        self.location= StringVar()

        #Creating Frames
        formFrame = Frame(self.root, bg='yellow')
        formFrame.place(x=10, y=100, width=500, height=580)


        displayFrame = Frame(self.root, bg='pink')
        displayFrame.place(x=520, y=100, width=830, height=580)

        #Working with formFrame
        title2 = Label(formFrame, text='Data Entry Here', font=('Arial Black', 20), bd=10, relief=RAISED, bg= 'yellow', fg='red')
        title2.grid(row=0, columnspan=2, padx=100, pady=20)
        
        #Roll No
        rollnoLb1 = Label(formFrame, text='Roll No: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        rollnoLb1.grid(row=1, column= 0, padx=10, sticky = 'W')

        rollnoEntry = Entry(formFrame, font=('Arial Black', 20), textvariable = self.rollnoVar)
        rollnoEntry.grid(row=1, column=1)

        #First Name
        fnameLb2 = Label(formFrame, text='First Name: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        fnameLb2.grid(row=2, column= 0, padx=10, sticky = 'W')

        fnameEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.fnameVar)
        fnameEntry.grid(row=2, column=1)

        #Last Name
        lnameLb3 = Label(formFrame, text='Last Name: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        lnameLb3.grid(row=3, column= 0, padx=10, sticky = 'W')

        lnameEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.lname)
        lnameEntry.grid(row=3, column=1)

        #Email
        emailLb4 = Label(formFrame, text='Email Id: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        emailLb4.grid(row=4, column= 0, padx=10, sticky = 'W')

        emailEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.email)
        emailEntry.grid(row=4, column=1)

        #Mobile Number
        mobileLb5 = Label(formFrame, text='Mobile No: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        mobileLb5.grid(row=5, column= 0, padx=10, sticky = 'W')

        mobileEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.mobile)
        mobileEntry.grid(row=5, column=1)

        #Course Name
        cnameLb6 = Label(formFrame, text='Course Name: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        cnameLb6.grid(row=6, column= 0, padx=10, sticky = 'W')

        cnameEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.cname)
        cnameEntry.grid(row=6, column=1)

        #Fee
        feeLb7 = Label(formFrame, text='Fee: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        feeLb7.grid(row=7, column= 0, padx=10, sticky = 'W')

        feeEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.fee)
        feeEntry.grid(row=7, column=1)

        #Institute Name
        inameLb8 = Label(formFrame, text='Institute Name: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        inameLb8.grid(row=8, column= 0, padx=10, sticky = 'W')

        inameEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.iname)
        inameEntry.grid(row=8, column=1)

        #Location
        locLb9 = Label(formFrame, text='Location: ', font=('Arial Black', 15), bg= 'yellow', fg='red')
        locLb9.grid(row=9, column= 0, padx=10, sticky = 'W')

        locEntry = Entry(formFrame, font=('Arial Black', 20), textvariable= self.location)
        locEntry.grid(row=9, column=1)


        #Creating BtnFrame
        btnFrame= Frame(formFrame, bd=4, relief=RAISED, bg= 'yellow')
        btnFrame.place(x=10, y=490, width=480, height=80)

        #Creating Buttons
        addBtn= Button(btnFrame, text='Add', font=('Arial Black', 15), bd=4, relief=RAISED, bg='pink', command=self.addingData)
        addBtn.grid(row=0, column=0, padx=15, pady=13)

        updateBtn= Button(btnFrame, text='Update', font=('Arial Black', 15), bd=4, relief=RAISED, bg='green', command=self.updatingData)
        updateBtn.grid(row=0, column=1, padx=15, pady=13)

        delBtn= Button(btnFrame, text='Delete', font=('Arial Black', 15), bd=4, relief=RAISED, bg='red', command=self.deletingData)
        delBtn.grid(row=0, column=2, padx=15, pady=13)

        cleBtn= Button(btnFrame, text='clear', font=('Arial Black', 15), bd=4, relief=RAISED, bg='blue')
        cleBtn.grid(row=0, column=3, padx=15, pady=13)

        


        #Working with displayFrame
        title3 = Label(displayFrame, text='Data Display Here', font=('Arial Black', 20), bd=10, relief=RAISED, bg= 'pink', fg='blue')
        title3.grid(row=0, columnspan=2, padx=280, pady=20)

        tb1Frame = Frame(displayFrame, bg='pink', width=760, height=400, bd=4, relief=RAISED )
        tb1Frame.place(x=35, y=100)

        self.studentsinfo= ttk.Treeview(tb1Frame, columns=('rollno', 'fname', 'lname', 'email', 'mobile', 'cname', 'fee', 'iname', 'location'))
        self.studentsinfo.heading('rollno', text= 'Roll No')
        self.studentsinfo.heading('fname', text= 'First Name')
        self.studentsinfo.heading('lname', text= 'Last Name')
        self.studentsinfo.heading('email', text= 'Email')
        self.studentsinfo.heading('mobile', text= 'Mobile No')
        self.studentsinfo.heading('cname', text= 'Course')
        self.studentsinfo.heading('fee', text= 'Fee')
        self.studentsinfo.heading('iname', text= 'Institute')
        self.studentsinfo.heading('location', text= 'Location')

        self.studentsinfo['show']='headings'
        self.studentsinfo.column('rollno', width=30, anchor = CENTER)
        self.studentsinfo.column('fname', width=80, anchor = CENTER)
        self.studentsinfo.column('lname', width=70, anchor = CENTER)
        self.studentsinfo.column('email', width=140, anchor = CENTER)
        self.studentsinfo.column('mobile', width=90, anchor = CENTER)
        self.studentsinfo.column('cname', width=90, anchor = CENTER)
        self.studentsinfo.column('fee', width=90, anchor = CENTER)
        self.studentsinfo.column('iname', width=90, anchor = CENTER)
        self.studentsinfo.column('location', width=90, anchor = CENTER)
        
        self.studentsinfo.pack()
        self.studentsinfo.bind('<ButtonRelease-1>', self.getRow)
        self.fetchingData()

    def addingData(self):
        connection = pymysql.connect(host ='localhost', user='root', password= 'root', db= 'pythonprojectdb',charset='utf8')
        c = connection.cursor()
        c.execute('insert into studentsinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                  ( self.rollnoVar.get(),
                      self.fnameVar.get(),
                      self.lname.get(),
                      self.email.get(),
                      self.mobile.get(),
                      self.cname.get(),
                      self.fee.get(),
                      self.iname.get(),
                      self.location.get()
                      )
                  )

                  
                 
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()


    def clearingData(self):
        self.rollnoVar.set(''),
        self.fnameVar.set(''),
        self.lname.set(''),
        self.email.set(''),
        self.mobile.set(''),
        self.cname.set(''),
        self.fee.set(''),
        self.iname.set(''),
        self.location.set('')


        #fetching data
    def fetchingData(self):
        connection = pymysql.connect(host ='localhost', user='root', password= 'root', db= 'pythonprojectdb',charset='utf8')
        c = connection.cursor()
        c.execute('select * from studentsinfo;')
        rows = c.fetchall()
        self.studentsinfo.delete(*self.studentsinfo.get_children())
        for i in rows:
            self.studentsinfo.insert('',END, value = i)

        connection.commit()
        connection.close()

        #get row for selection
    def getRow(self, a):
        cursor_row = self.studentsinfo.focus()
        content = self.studentsinfo.item(cursor_row)
        x = content['values']
        self.rollnoVar.set(x[0]),
        self.fnameVar.set(x[1]),
        self.lname.set(x[2]),
        self.email.set(x[3]),
        self.mobile.set(x[4]),
        self.cname.set(x[5]),
        self.fee.set(x[6]),
        self.iname.set(x[7]),
        self.location.set(x[8])


    def updatingData(self):
        connection = pymysql.connect(host ='localhost', user='root', password= 'root', db= 'pythonprojectdb',charset='utf8')
        c = connection.cursor()
        c.execute('update studentsinfo set fname=%s, lname=%s, emailid=%s, mobile=%s, cname=%s, fee=%s, iname=%s, location=%s where  rollno=%s',
                  (
                      self.fnameVar.get(),
                      self.lname.get(),
                      self.email.get(),
                      self.mobile.get(),
                      self.cname.get(),
                      self.fee.get(),
                      self.iname.get(),
                      self.location.get(),
                      self.rollnoVar.get()

                      ))
                   

        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()


    def deletingData(self):
        connection = pymysql.connect(host ='localhost', user='root', password= 'root', db= 'pythonprojectdb',charset='utf8')
        c = connection.cursor()
        c.execute('delete from studentsinfo where rollno=%s', (self.rollnoVar.get()))


        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()


     

        
root=Tk() #Main windo
obj=StudentsInfo(root)
