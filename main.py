from data import *
import matplotlib.pyplot as plt
from tkinter import *


def operation():

    T = []
    ofx = 0
    ofy = 0
    # miesiace = int(input())
    miesiace = int(txt.get())
    # regola =  int(input("podaj regole :2,3,4,5,6,7,10,12\n"))
    regula =int(listbox.get(listbox.curselection()))
    # systems.setf(regola);
    systems = allSystems(1, 1, regula, 2)
    offset = systems.readData(txt3.get()+".txt",txt4.get()+".txt")
    miesiace += offset
    j = 0
    #print(len(T))
    #print(miesiace - offset)
    for i in range(offset + 1, miesiace + 1):
        # print(j)

       # labeltext[j].set("#############" + str(i) + "###############\n")
        #print("#############" + str(i) + "###############\n")
        systems.computeToFill(i)
        systems.update(i)

        j += 1
    # systems.print_()
    temp = 0
    YvalSys = []
    TimesSys = []
    functSys = []
    text = ""
    leg = []
    color = ['b','g','r','y','c','k','m']
    for i in range(systems.n):
        YvalSys.append(systems.getSysYval(i))
        TimesSys.append(systems.getSysTimes(i))
        functSys.append(systems.getSysFunctions(i))
        plt.plot(TimesSys[i],YvalSys[i],'ro', c = color[(i)%len(color)])
        leg.append("system: "+str(i+1))
        text = text + "system: " + str(i+1) + " " + str(functSys[i]) + "\n"
    max = plt.ylim()[1]
    plt.text(2000,max, text)
    plt.legend(leg)
    plt.grid(True)
    plt.axvline(x=int(offset/12) + 2000 + (offset%12)/100,linewidth=2, color='m')
    # labeltext1.set(functSys3)
    temp = 0

    plt.show()


# systems.save(fileout);
# fileout.close();
# file.close();

window = Tk()

window.title("GUI")
window.geometry('800x400')

label = Label(window, text="Miesiące symulacji:")
label.grid(column=10, row=0)
txt = Entry(window)
txt.grid(column=10, row=1)
txt.focus()
txt.insert(0, "500")

label2 = Label( window, text = "Reguła:")
label2.grid(column=10, row=2)
scrollbar = Scrollbar(window)
scrollbar.grid(column=10, row=3)

listbox = Listbox(window, yscrollcommand=scrollbar.set, height=8,width=5)
for i in range(2,8):
    listbox.insert(END, str(i))
'''listbox.insert(END, "2 - najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie sameto wybieramy ten który ma największą krotność")
listbox.insert(END, "3 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy łączny czas zalegania")
listbox.insert(END, "4 - najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie sameto wybieramy ten który ma największą krotność")
listbox.insert(END, "5 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy czas zalegania" )
listbox.insert(END, "6 - najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność")
listbox.insert(END, "7 - najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo")
listbox.insert(END, "10 - największą krotność jeśli są takie sameto wybieramy losowo")
listbox.insert(END, "12 - wybór losowy")'''
listbox.insert(END, str(10))
listbox.insert(END, str(12))
label = Label(window, text = "-najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie same to wybieramy ten który ma największą krotność")
label.place(x=100,y=60)
label = Label(window, text = "-największą krotność jeśli są takie same to wybieramy ten który ma najdłuższy łączny czas zalegania" )
label.place(x=100,y=75)
label = Label(window, text = "-najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie same to wybieramy ten który ma największą krotność" )
label.place(x=100,y=92)
label = Label(window, text = "-największą krotność jeśli są takie same to wybieramy ten który ma najdłuższy czas zalegania" )
label.place(x=100,y=107)
label = Label(window, text = "-najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność" )
label.place(x=100,y=124)
label = Label(window, text = "-najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo" )
label.place(x=100,y=139)
label = Label(window, text = "-największą krotność jeśli są takie sameto wybieramy losowo" )
label.place(x=100,y=157)
label = Label(window, text = "-wybór losowy" )
label.place(x=100,y=173)
listbox.grid(column=10, row=3)

scrollbar.config(command=listbox.yview)
'''txt2 = Entry(window,width=10)
txt2.grid(column=10, row=3)
txt2.insert(0,"0")'''

label3 = Label(window, text="Plik txt z danymi:")
label3.grid(column=20, row=0)
txt3 = Entry(window)
txt3.grid(column=20, row=1)
txt3.insert(0, "datainput2")

label4 = Label(window, text="Plik txt z okresami:")
label4.grid(column=30, row=0)
txt4 = Entry(window)
txt4.grid(column=30, row=1)
txt4.insert(0, "timeinput2")

btn = Button(window, text="Enter", bg="white", fg="black", command=operation)
btn.grid(column=10, row=6)
#do helpa czy czegos takiego
'''t = "reguły wyboru funkcjolanlości ze zbioru zaległych:\n " \
    "2 - najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie sameto wybieramy ten który ma największą krotność\n" \
    "3 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy łączny czas zalegania\n" \
    "4 - najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie sameto wybieramy ten który ma największą krotność\n" \
    "5 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy czas zalegania\n" \
    "6 - najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność\n" \
    "7 - najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo\n" \
    "10 - największą krotność jeśli są takie sameto wybieramy losowo\n" \
    "12 - wybór losowy\n"
'''
window.mainloop()