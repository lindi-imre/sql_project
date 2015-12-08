import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

create_button= tkinter.Button(top, text ="Create", command = helloCallBack)
insert_button= tkinter.Button(top, text ="Insert", command = helloCallBack)
query_button= tkinter.Button(top, text ="Query", command = helloCallBack)
drop_button=tkinter.Button(top, text ="Drop", command = helloCallBack)

B.pack()
top.mainloop()
