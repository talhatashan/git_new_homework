import tkinter


#WINDOW
window=tkinter.Tk()
window.title("Tkinter sayfasi")
window.minsize(500, 500)

#LABEL
my_label=tkinter.Label(text="this is a label")

#my_label kismina sonradan istedigimiz gibi ekleme yapabiliyoruz
my_label.config(bg="black", fg="white")
#pack islemi label konumunu belirten bir fonksiyon
my_label.pack()
#font kismini yukariya ekleyebilirdik. asagiya da olur
my_label.config(font=('arial', 30, "italic"))
#.CONFIG DIYEREK HER OZELLIGE SONRADAN ERISEBILIYORUZ
def click_button():
    a=my_entry.get()
    print(a)
    print("button clicked")

#BUTTON
#BURADA EN ONEMLI KOMUT= COMMAND KOMUTU, BUTONA TIKLAYINCA NE OLSUN
my_button=tkinter.Button(text="this is a button", command=click_button)
my_button.pack()


#ENTRY
my_entry=tkinter.Entry(width=35)
my_entry.place(x=100, y=100)


window.mainloop()