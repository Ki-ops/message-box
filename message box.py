from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Key error")
root.geometry("500x500")

lbl=Label(root,text="Dictionary")
lbl.place(relx=0.5,rely=0.3,anchor=CENTER)

dictionary ={"fruit":"Dragon fruit",
            "colour":"Black",
            "animal":"Black panther"
            
             }

def ABC():
    
    try:
        print(dictionary["fruit"])
        print(dictionary["bird"])
    except:
        print("The key is not defined in the dictionary")
        messagebox.showinfo("ERROR","The key is not defined in the dictionary")

    
btn=Button(root,text="Display The Result",command=ABC)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
    
root.mainloop()



