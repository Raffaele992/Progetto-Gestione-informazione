import tkinter
import tkinter.messagebox

top = tkinter.Tk()

top.geometry("750x500")

def helloCallBack():
   msg = tkinter.messagebox.showinfo("Hello Python", "HelloWorld")


L1 = tkinter.Label (top, text = "Inserisci la parola da cercare")
L1.pack(side = tkinter.LEFT)

E1 = tkinter.Entry(top, bd = 5, width = 50)
E1.pack(side = tkinter.RIGHT)


B = tkinter.Button (top, text = "Prova", command = helloCallBack)

B.place(x = 125, y = 150)
top.mainloop()

