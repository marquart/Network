from tkinter import *
import csv

window = Tk()
global Kategorie
Kategorie = ["Geburtsjahr","Geburtsort","Fachrichtung"]

def standardMenu(Parent):
	myMenu = Menu(Parent)
	Parent.config(menu=myMenu)

	editMenu = Menu(Parent)
	myMenu.add_cascade(label="New..", menu=editMenu)
	editMenu.add_command(label="Conections", command=guiCon)
	editMenu.add_separator()
	editMenu.add_command(label="Exit")

def writeBasicData():
    csvfile = open('BasicData.csv', 'a', newline='')
    csvfileWriter = csv.writer(csvfile)
    csvfileWriter.writerow([Name.get(), Kategorie.index(selected.get()), selected.get(), FilledKategorie.get()])

    csvfile.close()
	
def writeEdgeList():
    csvfile = open('EdgeList.csv', 'a', newline='')
    csvfileWriter = csv.writer(csvfile)
    csvfileWriter.writerow([entry_Source.get(), entry_Target.get()])

    csvfile.close()
    entry_Target.delete(0, END)

def gui():
    global selected, Name, FilledKategorie
	
    standardMenu(window)

    Label(window, text="Name").grid(row=0, column=0)

    selected = StringVar()
    selected.set(Kategorie[0])
    KatgeorieAuswahl = OptionMenu(window,selected,*Kategorie).grid(row=0, column=1)

    Name = Entry(window)
    FilledKategorie = Entry(window)

    Name.grid(row=1, column=0)
    FilledKategorie.grid(row=1, column=1)

    endbutton = Button(window, text="Sichern", command=writeBasicData).grid(row=3, column=0, sticky=W, pady=4)

    window.mainloop()

def guiCon():
    global entry_Source, entry_Target
	
    windowCon = Tk()
	
    standardMenu(windowCon)
	
    Label(windowCon, text="Source").grid(row=0, column=0)
    Label(windowCon, text="Target").grid(row=0, column=1)	
    entry_Source = Entry(windowCon)
    entry_Source.grid(row=1, column=0)
    entry_Target = Entry(windowCon)
    entry_Target.grid(row=1, column=1)
    endbutton = Button(windowCon, text="Sichern", command=writeEdgeList).grid(row=2, column=1, sticky=W, pady=4)
    windowCon.mainloop()

gui()
