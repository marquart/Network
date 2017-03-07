from tkinter import *
import csv

def writeBasicData():
    csvfile = open('BasicData.csv', 'a', newline='')
    csvfileWriter = csv.writer(csvfile)
    csvfileWriter.writerow([Name.get(), Geburtsjahr.get()])
    
    csvfile.close()
def gui():
    window = Tk()
    Label(window, text="Name").grid(row=0)
    Label(window, text="Geburtsjahr").grid(row=1)
    
    global Name, Geburtsjahr
    
    Name = Entry(window)
    Geburtsjahr = Entry(window)
    
    Name.grid(row=0, column=1)
    Geburtsjahr.grid(row=1, column=1)
    
    
    endbutton = Button(window, text="Sichern", command=writeBasicData).grid(row=3, column=0, sticky=W, pady=4)
    
    
    window.mainloop()
gui()
