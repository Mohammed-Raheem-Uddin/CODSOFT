from tkinter import *
import random
from tkinter import messagebox

def results():
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    symbols="@#$%^&*()!+_<>/'"

    length = int(ulenght.get())

    option=choice.get()

    if option==1 and (length>=8 and length<=20):
        messagebox.showinfo("Note", "Weak passwords consist of only lowercase alphabets")
        g_pass = ''.join(random.choices(lowercase, k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)

    elif option==2 and (length>=8 and length<=20):
        messagebox.showinfo("Note", "Normal passwords does not include symbols")
        g_pass = ''.join(random.choices(uppercase + lowercase + numbers, k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)

    elif option==3 and (length>=8 and length<=20):
        g_pass=''.join(random.choices(uppercase+lowercase+numbers+symbols, k=length))
        password.config(text=g_pass)
        ui.clipboard_clear()
        ui.clipboard_append(g_pass)
    else :
       messagebox.showerror("ERROR","Specify the length and complexity of your password as per to the instructions")

ui=Tk()
ui.geometry("580x650")
ui.resizable(False,False)
ui.config(bg="lightblue")
ui.title("Internship (Task-2)")

frame1=Frame(ui,bg="lightgreen")
frame1.pack(fill="x")
heading=Label(frame1,text="Random Password Generator", font="aerial 20 bold", bg="lightgreen")
heading.pack(pady=10)

frame2=Frame(ui,bg="lightblue")
frame2.place(x=10,y=60)
len=Label(frame2,text="1. LENGTH (Specify the length of your password in the range from 8~20)", font="arial 12 bold", bg="lightblue", wraplength=580)
len.pack(pady=5,)
ulenght=Entry(frame2,font="arial 15")
ulenght.pack()

choice=IntVar()

frame3=Frame(ui,bg="lightblue")
frame3.place(x=10,y=150)
com=Label(frame3,text="2. COMPLEXITY (Select the complexity type of your password)", font="arial 12 bold", bg="lightblue", wraplength=580)
com.pack(pady=10)
easy=Radiobutton(frame3,text="Weak",variable=choice,bg="lightgreen",wraplength=60,font="arial 12", value=1)
easy.pack(anchor="nw")
normal=Radiobutton(frame3,text="Normal",variable=choice,bg="lightgreen",wraplength=60,font="arial 12",value=2)
normal.pack()
hard=Radiobutton(frame3,text="Strong",variable=choice,bg="lightgreen",wraplength=60,font="arial 12",value=3)
hard.pack(anchor="ne")

bt=Button(ui,text="Create Password and copy",font="arial 10 bold", command=results, borderwidth=10,bg="lightgreen")
bt.place(x=170,y=380)

password=Label(ui, text="", font="arial 20 bold", bg="lightblue",borderwidth=10,wraplength=250)
password.place(x=140,y=300)

ui.mainloop()
