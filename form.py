from tkinter import *
from tkinter import messagebox
from pymysql import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from tkcalendar import DateEntry
from PIL import Image, ImageTk

con=connect(host='localhost', port=3306, user='root', password='2002', database='form')
cur=con.cursor()

page=Tk()
page.geometry('1200x1200')
page.title('Sports registration form')
page.iconbitmap('C:\\Users\\jainu\\OneDrive\\Desktop\\CADD\\Form\\sports.ico')
page.configure(bg="ghost white")


p1=PanedWindow(master=page,bg='light blue', height=45)
p1.pack(fill='x', side='top')
ll1 = Label(p1, text="Sports Registration Form", bg='light blue', font=('Times New Roman', 18, 'bold'))
p1.add(ll1)

p2=PanedWindow(master=page,bg='light blue', height=45)
p2.pack(fill='x', side='top')
ll2 = Label(p2, text="SJS sports academy", bg='light grey', font=('Times New Roman', 10, 'bold'))
p2.add(ll2)


def save():

   # try:
        name = e1.get() #name
        age = e2.get() #Age
        dob = e3.get() #DOB
        sname = e4.get() #Schoolname
        locality = e5.get() # Locality
        gen = gender.get() #Gender
        #print("Sports interested:")
        spt_int=''
        if check_var1.get():
            spt_int+= 'Batminton'
        if check_var2.get():
            spt_int+= "Cricket"
        if check_var3.get():
            spt_int+="Volleyball"
        if check_var4.get():
            spt_int+="Basketball"
        if check_var5.get():
            spt_int+="Football"
        address = t1.get(1.0, END) # Address
        contact = e9.get() #COntact
        fb = s3.get(1.0, END) #Feedback
        li=[name,age,dob,sname,locality,gen,spt_int,address,contact,fb]
        
        for a in li:
            if a=='':
                messagebox.showerror(title='Error', message="Enter all the filed to proceed")
                break
            age=int(age)
            if age<=10 or age>=35:
                messagebox.showerror(title='Age error', message='Students less than age 10 and more than age 35 are not eligible')
                break
            
        else:
            try:
                li=[name,int(age),dob,sname,locality,gen,spt_int,address,contact,fb]
                cur.execute('insert into sports values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',li)
                con.commit()
                contact=int(contact)
         
                messagebox.showinfo(title="info", message="Details saved successfully")
             
                
                               
            except ValueError:
                messagebox.showerror(title="Value Error", message="Age and contact should only consists of digits")
                
            except Exception as e:
                messagebox.showerror(title="Error", message=str(e))
   # except Exception as e:
        #messagebox.showerror(title="Error", message=str(e))

#canvas for scrolled bar

canvas=Canvas(page)
img_s=ImageTk.PhotoImage(Image.open('C:\\Users\\jainu\\OneDrive\\Desktop\\CADD\\Form\\Sport.jpg'))
canvas.create_image(1000,50,anchor='ne',image=img_s)
img=ImageTk.PhotoImage(Image.open('C:\\Users\\jainu\\OneDrive\\Desktop\\CADD\\Form\\foot.jpg'))
canvas.create_image(1000,400,anchor='ne',image=img)
canvas.pack(side='left', fill='both', expand='True')

#scroll bar
scrollbar = Scrollbar(page, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)

#form_frame


# Create a frame inside the canvas to hold the form widgets
form_frame = Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor='nw')

# Ensure the canvas resizes properly
form_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

# Frame for the form
f1 = Frame(form_frame)
f1.pack(anchor='w', padx=30, pady=30)


# Creating the form layout using a nested frame to align labels and entries side by side
# Name
name_frame = Frame(f1)
name_frame.pack(fill='x', pady=15)
l1 = Label(name_frame, text='Enter name:', width=25, anchor='w', font=('Times New Roman', 10))
l1.pack(side='left', padx=10)
e1 = Entry(name_frame, width=45)
e1.pack(side='left')

# Age
age_frame = Frame(f1)
age_frame.pack(fill='x', pady=15)
l2 = Label(age_frame, text='Enter age:', width=25, anchor='w', font=('Times New Roman', 10))
l2.pack(side='left', padx=10)
e2 = Entry(age_frame, width=45)
e2.pack(side='left')



#DOB
dob_frame = Frame(f1)
dob_frame.pack(fill='x', pady=15)
l3 = Label(dob_frame, text='Enter your date of birth:', width=25, anchor='w', font=('Times New Roman', 10))
l3.pack(side='left', padx=10)
#e3 = DateEntry(dob_frame, width=45, background='sky blue',foreground='White', borderwidth=3, date_pattern='y-mm-dd')
e3 = Entry(dob_frame, width=45, fg='grey')
e3.pack(side='left')
e3.insert(0,'DD-MM-YYYY')

#Previous academy/school
sch_frame = Frame(f1)
sch_frame.pack(fill='x', pady=15)
l4 = Label(sch_frame, text='Enter your school name:', width=25, anchor='w', font=('Times New Roman', 10))
l4.pack(side='left', padx=10)
e4 = Entry(sch_frame, width=45)
e4.pack(side='left')

#Location
loc=Frame(f1)
loc.pack(fill='x', pady=15)
l5=Label(loc, text='Locality:', width=25,anchor='w', font=('Times New Roman', 10))
l5.pack(side='left', padx=10)
e5=Entry(loc, width=45)
e5.pack(side='left')

#Gender
gender=StringVar()
gen_frame=Frame(f1)
gen_frame.pack(fill='x',pady=15)
l6=Label(gen_frame, text='Gender: ', width=25, anchor='w', font=('Times New Roman', 10))
l6.pack(side='left', padx=10)
r1=Radiobutton(gen_frame,text='Male', variable=gender, value='male')
r1.pack(side='left', padx=10)
r2=Radiobutton(gen_frame,text='Female', variable=gender, value='female')
r2.pack(side='left', padx=10)
r3=Radiobutton(gen_frame,text='Prefer not to say', variable=gender, value='Do not specify')
r3.pack(side='left', padx=10)

#Sports interested

cb_frame1=Frame(f1)
cb_frame1.pack(fill='x',padx=10, pady=15)

cb_frame=Frame(f1)
cb_frame.pack(fill='x',padx=10, pady=15)


check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()
check_var4 = IntVar()
check_var5 = IntVar()

l7=Label(cb_frame1, text='Sports interested: ', width=25, anchor='w', font=('Times New Roman', 10))
l7.pack(side='left', padx=1)

c1=Checkbutton(cb_frame, text='Badminton', variable=check_var1, font=('Times New Roman', 10))
c1.pack(side='left', padx=10)
c2=Checkbutton(cb_frame, text='Cricket', variable=check_var2, font=('Times New Roman', 10))
c2.pack(side='left', padx=10)
c3=Checkbutton(cb_frame, text='Vollyball', variable=check_var3, font=('Times New Roman', 10))
c3.pack(side='left', padx=10)
c4=Checkbutton(cb_frame, text='Basket ball', variable=check_var4, font=('Times New Roman', 10))
c4.pack(side='left', padx=10)
c5=Checkbutton(cb_frame, text='Foot ball', variable=check_var5, font=('Times New Roman', 10))
c5.pack(side='left', padx=10)

#address

text_frame=Frame(f1)
text_frame.pack(fill='x', pady=15)
l8=Label(text_frame, text='Address: ', font=("Times New Roman", 10))           
l8.pack(side='left', padx=10)
t1=Text(text_frame, height=5, width=20)
t1.pack(side='left', padx=10)

#Contact
con_frame=Frame(f1)
con_frame.pack(fill='x', pady=15)
l9=Label(con_frame, text='Enter mobile no:', width=25,anchor='w', font=('Times New Roman', 10))
l9.pack(side='left', padx=10)
e9=Entry(con_frame, width=45)
e9.pack(side='left')


#scrolled text
lb1=LabelFrame(f1, bg='#F7FCFE', width=20, height=35, text='Any feedback', font=('Times New Roman', 10))
lb1.pack(fill='x', pady=15)
s3=ScrolledText(master=lb1, wrap='word', width=40, height=15)
s3.pack()

#Submit button


#b_frame=Frmae(f1)
b_frame=Frame(f1)
b_frame.pack(fill='x', pady=15)
b1=Button(b_frame, text='SUBMIT',command=save, bg='light blue', fg='brown', padx=10, pady=10, activebackground='green', relief='ridge', bd=2, font=('Times New Roman', 12))
b1.pack()



page.mainloop()
