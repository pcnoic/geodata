#application name: Geodata
#description: creates a coordinate text file
#author: christos alexiou

from tkinter import *
import time


########### key down function
def clickSubmit1():

    def createLabels(proX, proY):

        def dataWriteFirst(Xpro, Ypro):
            #here we take the data from the textboxes we created in CreateNewLabels() and empty the text boxes

            xFinale = inputX.get()
            yFinale = inputY.get()

            if xFinale and yFinale:
                inputX.delete(0, END)
                inputY.delete(0, END)

            dataWriteFirst.counter += 1

            with open('coordinates.txt', 'a') as coordFile:
                dataToWrite = str(dataWriteFirst.counter) + "," + str(Xpro) + str(xFinale) + "," + str(Ypro) + str(yFinale)
                coordFile.write(dataToWrite + '\n')

            #return the tuple of the data
            #return xFinale, yFinale


        dataWriteFirst.counter = 0

        enterXlabel = Label(window, text="Εισάγετε τη τεταγμένη x: ", bg="black", fg="white", font="none 12 bold")
        enterXlabel.grid(row=1, column=1, sticky=W)

        inputX = Entry(window, width=10, bg="white")
        inputX.grid(row=1, column=2, sticky=W)

        enterYlabel = Label(window, text="Εισάγετε τη τετμημένη y: ", bg="black", fg="white", font="none 12 bold")
        enterYlabel.grid(row=2, column=1, sticky=W)

        inputY = Entry(window, width=10, bg="white")
        inputY.grid(row=2, column=2, sticky=W)

        secondSubmitButton = Button(window, text="Next", width=4, command= lambda: dataWriteFirst(proX, proY))
        secondSubmitButton.grid(row=3, column=2, sticky=W)

        exitButton = Button(window, text="EXIT", width=4, command=close_window)
        exitButton.grid(row=3, column=3, sticky=W)

        #x , y = dataWriteFirst()

        #trying to write the data (idea 1)
        #with open('coordinates.txt', 'a') as coordFile:
            #dataToWrite = str(counter) + "," + str(proX) + str(x) + "," + str(proY) + str(y)
            #coordFile.write(dataToWrite + '\n')


    #collectin the data from textboxes
    prothemaXdata = int(prothemaX.get())
    prothemaYdata = int(prothemaY.get())

    if(isinstance(prothemaXdata, int) and isinstance(prothemaYdata, int)):

        #clearing the window to draw new labels
        prothemaXLabel.grid_forget()
        prothemaX.grid_forget()

        prothemaYLabel.grid_forget()
        prothemaY.grid_forget()

        submitButton.grid_forget()

        #creating new labels
        createLabels(prothemaXdata, prothemaYdata)





def close_window():
    window.destroy()
    exit()

#############main window
window = Tk()
window.title("Geodata v0.1")
window.configure(background="black")

iconPhoto = PhotoImage(file="icon.gif")
Label (window, image=iconPhoto,bg="black") .grid(row=0, column=0, sticky=W)


#############creating text labels and inputs

prothemaXLabel = Label(window, text="Εισάγετε το πρόθεμα της συντεταγμένης X: ", bg="black", fg="white", font="none 12 bold")
prothemaXLabel.grid(row=2, column=0, sticky=W)
prothemaX = Entry(window, width=10, bg="white")
prothemaX.grid(row=2,column=1,sticky=W)


prothemaYLabel= Label(window, text="Εισάγετε το πρόθεμα της συντεταγμένης Y: ", bg="black", fg="white", font="none 12 bold")
prothemaYLabel.grid(row=3, column=0, sticky=W)
prothemaY = Entry(window, width=10, bg="white")
prothemaY.grid(row=3,column=1,sticky=W)

submitButton = Button(window, text="SUBMIT", width=6, command=clickSubmit1)
submitButton.grid(row=4, column=2, sticky=W)


############running the main window loop
window.mainloop()

