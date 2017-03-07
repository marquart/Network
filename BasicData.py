from tkinter import *
import csv

global Kategorie

Kategorie = ["Geburtsjahr","Geburtsort","Fachrichtung"]

def writeBasicData():
    csvfile = open('BasicData.csv', 'a', newline='')
    csvfileWriter = csv.writer(csvfile)
    csvfileWriter.writerow([Name.get(), Kategorie.index(selected.get()), selected.get(), FilledKategorie.get()])
    
    csvfile.close()
def gui():
    global selected, Name, FilledKategorie
    
    window = Tk()
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
gui()