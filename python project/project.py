from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)




def main_window():
    global enter1,enter2
    win = Tk()

    win.geometry("500x370")
    win.resizable(False,False)
    win.config(bg="Blue")
    win.title("Wscube Tech")

    label1 = Label(win,text="Incorrect Spelling",font=("Time New Roman",25, "bold"),bg = "Blue", fg = "white")
    label1.place(x=100,y=20,height=50,width=300)

    enter1= Entry(win,font=("Time New Roman",20))
    enter1.place(x=50, y = 80,height=50,width=400)

    label2 = Label(win,text="Correct Spelling",font=("Time New Roman",25, "bold"),bg = "Blue", fg = "white")
    label2.place(x=100,y=140,height=50,width=300)

    enter2 = Entry(win,font=("Time New Roman",20))
    enter2.place(x=50, y = 200,height=50,width=400)

    button2 = Button(win,text="Done",font=("Time New Roman",25,"bold"),bg="yellow",command=correct_spelling)
    button2.place(x = 150,y = 280,height=50,width=200,)

    win.mainloop()

main_window()  




def Incorrect_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)




def name_window():
    global enter1,enter2
    tok = Tk()

    tok.geometry("500x370")
    tok.resizable(False,False)
    tok.config(bg="Blue")
    tok.title("Wscube Tech")

    label1 = Label(tok,text="Correct Spelling",font=("Time New Roman",25, "bold"),bg = "Blue", fg = "white")
    label1.place(x=100,y=20,height=50,width=300)

    enter1= Entry(tok,font=("Time New Roman",20))
    enter1.place(x=50, y = 80,height=50,width=400)

    label2 = Label(tok,text="Incorrect Spelling",font=("Time New Roman",25, "bold"),bg = "Blue", fg = "white")
    label2.place(x=100,y=140,height=50,width=300)

    enter2 = Entry(tok,font=("Time New Roman",20))
    enter2.place(x=50, y = 200,height=50,width=400)

    button1 = Button(tok,text="change",font=("time New Roman",25,"bold"),bg="green",command=Incorrect_spelling)
    button1.place(x = 150,y = 280, height= 50, width=200)

    tok.mainloop()

name_window()  





     







