# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
form = tk.Tk()
form.geometry('800x800+800+200')
form.title('New User')

entr = tk.StringVar()
entr1 = tk.StringVar()
entr2 = tk.StringVar()
entr3 = tk.StringVar()
entr4 = tk.StringVar()


llb_username = tk.Label(form, text = 'User Name:',font='Times 12').place(x=450,y=100)
llb_displayname = tk.Label(form, text = 'Display Name',font='Times 12').place(x=450,y=140)
llb_phone = tk.Label(form, text = 'Phone:',font='Times 12').place(x=450,y=180)
llb_Email = tk.Label(form, text = 'EMail:',font='Times 12').place(x=450,y=220)
llb_UserRoles = tk.Label(form, text = 'User Roles:',font='Times 12').place(x=450,y=260)
llb_Enabled = tk.Label(form, text = 'Enabled:',font='Times 12').place(x=450,y=310)


entry_username = tk.Entry(textvariable=entr).place(x= 600, y = 103)
entry_displayname = tk.Entry(textvariable=entr1).place(x= 600, y = 143)
entry_phone = tk.Entry(textvariable=entr2).place(x= 600, y = 183)
entry_Email = tk.Entry(textvariable=entr3).place(x= 600, y = 223)

#In this section I tried to add scroll bar but code doesn't work and I have didn't solved it.
#scrol=tk.Scrollbar()
#scrol.pack(side=tk.RIGHT,fiil=tk.Y)

#ListBox=tk.ListBox(form,yscrollcommand=scrol.get())
#ListBox.insert('Guest','Admin','SuperAdmin')
#ListBox.pack(side=tk.LEFT)
#scrol.config(command=ListBox.yview)


x = tk.IntVar()  
x.set(0)
def control():
    if x.get()==0:
        print('false')
    else:
        
        print('true')
        
Button1 = tk.Checkbutton(form, text = "Enabled",  
                      variable = x, 
                      command=control,
                      height = 2, 
                      width = 10).place(x=600,y=304)

def saveuser():
    
    llb_username = tk.Label(form, text = 'User Name:',font='Times 12').place(x=450,y=100)
    llb_displayname = tk.Label(form, text = 'Display Name',font='Times 12').place(x=450,y=140)
    llb_phone = tk.Label(form, text = 'Phone:',font='Times 12').place(x=450,y=180)
    llb_Email = tk.Label(form, text = 'EMail:',font='Times 12').place(x=450,y=220)
    
    llb_username1 = tk.Label(form, text = entr.get(),font='Times 12').place(x=250,y=100)
    llb_displayname1 = tk.Label(form, text = entr1.get(),font='Times 12').place(x=250,y=140)
    llb_phone1 = tk.Label(form, text = entr2.get(),font='Times 12').place(x=250,y=180)
    llb_Email1 = tk.Label(form, text = entr3.get(),font='Times 12').place(x=250,y=220)
   
    Button11 = tk.Checkbutton(form, text = entr4.get(),  
                      variable = x, 
                      command=control,
                      height = 2, 
                      width = 10).place(x=600,y=304)

suser=tk.Button(form,text='Save User', bg = 'blue',activebackground = 'green', command = saveuser).place(x=665, y=50)








form.mainloop()



