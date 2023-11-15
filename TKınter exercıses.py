from tkinter import *
window=Tk()
window.title("Tkinter exercises")
window.minsize(600, 600)


my_label=Label(text="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10) # x ve y de yanindakilerle ne kadar bosluk birakacigini hesaba katiyor
my_label.pack()

def button_clicked():
    print("button clicked")
    #print(my_entry.get())
    print(my_text.get("1.0", END))
my_button=Button(text="Button", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

my_entry=Entry(width=30)
my_entry.pack()

my_text=Text(width=30, height=15)
my_text.pack()






window.mainloop()
