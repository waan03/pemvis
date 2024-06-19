from tkinter import *

print("====================Excercise#1====================")
print("===Mencetak data dari Entry Widget dengan Button===")
print("===================================================")
root =Tk()
root.geometry('400x200')

def CetakData():
    teks = entry1.get()
    print(teks)
    return None

entry1 = Entry(root, width=20); entry1.pack()
Button(root, text="Cetak Data", command=CetakData).pack()

root.mainloop()

print("====================Excercise#2====================")
print("===Mengambil Data dan Menampilkan Data (Part 1)====")
print("===================================================")
from tkinter import *
import tkinter.messagebox

class DataInOut:

    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')
        
        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        frame4 =Frame(frame1)
        frame4.grid(row=2, column=1)

        FirstNum = StringVar()
        SecondNum = StringVar()

        self.lblFirstNum = Label(frame2, text ='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row= 1,column=0) 
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()


print("====================Excercise#2====================")
print("===Mengambil Data dan Menampilkan Data (Part 2)====")
print("===================================================")
from tkinter import *
import tkinter.messagebox

class DataInOut:

    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        
        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame2 = Frame(frame1)
        frame2.grid(row=1, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        self.FirstNum = StringVar()
        self.SecondNum = StringVar()
        self.Hasil = StringVar()

        self.lblFirstNum = Label(frame2, text ='Masukan First Number')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Masukan Second Number')
        self.lblSecondNum.grid(row= 1,column=0) 
        self.txtSecondNum = Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text ='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Label(frame2, textvariable=self.Hasil)
        self.txtHasil.grid(row=2,column=1)

        self.btnJumlahkan = Button(frame3, text="Jumlahkan", command=self.Jumlahkan)
        self.btnJumlahkan.grid(row=2, column=0)
        self.btnReset = Button(frame3, text="Reset", command=self.Reset)
        self.btnReset.grid(row=2, column=1)
        self.btnKeluar = Button(frame3, text="Keluar", command=self.root.destroy)
        self.btnKeluar.grid(row=2, column=2)

    def Jumlahkan(self):
        try:
            pertama = float(self.FirstNum.get())
            kedua = float(self.SecondNum.get())
            hasil = pertama + kedua
            self.Hasil.set(str(hasil))
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Masukkan angka yang valid')

    def Reset(self):
        self.FirstNum.set('')
        self.SecondNum.set('')
        self.Hasil.set('')


if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()


