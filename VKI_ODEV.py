import tkinter

window=tkinter.Tk()
window.title("vucut kitle indeksi hesaplama")
window.minsize(200, 200)


my_label1=tkinter.Label(text="Enter Your Weight kg")
my_label1.pack()




my_entry1=tkinter.Entry(width=20)
my_entry1.pack()


my_label2=tkinter.Label(text="Enter Your Height cm")
my_label2.pack()
my_entry2=tkinter.Entry(width=20)
my_entry2.pack()

def vki_calculator():
    a=int(my_entry1.get())
    b=int(my_entry2.get())
    try:
        c=float(a/((b/100)*(b/100)))
        if c <18:
            print("cok zayifsin")
        elif c>18 and c<25:
            print("ideal kilodasin")
    except:
        print("please enter a number")



my_button=tkinter.Button(text="Calculate", command=vki_calculator)
my_button.pack()


window.mainloop()