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

#SCALE
my_scale=Scale(from_=0, to=50)
my_scale.pack()


def my_spinbox_goes():
    print(my_spinbox.get())

#SPINBOX
my_spinbox=Spinbox(from_=0, to=50, command=my_spinbox_goes)
my_spinbox.pack()

def checkbutton_selected():
    print(check_state.get())

check_state=IntVar()

#CHECKBUTTON
my_checkbutton=Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()




#RADIOBUTTON
def radio_selected():
    print(radio_check.get())

radio_check=IntVar()
my_radiobutton=Radiobutton(text="1. option", value=10, variable=radio_check, command=radio_selected)
my_radiobutton2=Radiobutton(text="2. option", value=20, variable=radio_check, command=radio_selected)

my_radiobutton.pack()
my_radiobutton2.pack()


#LISTBOX
my_listbox=Listbox()
name_list=["Talha", "Anya", "Cocuk"]

for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])

my_listbox.pack()


window.mainloop()