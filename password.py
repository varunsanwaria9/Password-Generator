from tkinter import *
from random import randint
import pyperclip as p

root = Tk()
root.geometry("300x220")
root.title("Passsword Generator")

class Password():
    def __init__(self):
        self.s = ""

    def copy_fn(self):
        p.copy(self.s)
        Label(root,text= "Password is copied in clipboard ",font="Corier 10 italic").pack(pady=4)

    def password(self,n):
        l = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$^123456789"
        for i in range(n):
            a = randint(0,65)
            self.s += l[a]
        Label(root,text=f"Password : {self.s}",font="Corier 20 bold").pack(pady=6)
        Button(root,text="Copy",command=vs.copy_fn).pack(pady=4)

vs = Password()

def take_len():
    vs.password(int(len_password.get()))

        
Label(root,text= "Length").pack(pady=4)
len_password = Entry(root)
len_password.pack(pady=4)
len_password.focus()
print(len_password.get())
Button(root,text="Submit",command=take_len).pack(pady=4)
root.mainloop()
