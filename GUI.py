from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # Window title
        self.master.title("Progetto Gestione informazioni")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_exit)

        quitButton.place(x=175, y=500)

        # Creation of the menu instance in which there are the objects
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Creation of the object "File"
        file = Menu(menu)

        # Allow to show commands inside "File"
        menu.add_cascade(label="File", menu=file)

        # Creation of the object "Edit"
        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="Edit", menu=edit)

        #Adds a button in the menu which close the program
        Exit = Menu(menu)
        menu.add_command(label="Exit", command=self.client_exit)


    def client_exit(self):
        exit()


root = Tk()

root.geometry("400x600")

app = Window(root)

root.mainloop()
