#imports
from tkinter import *
from tkinter import filedialog
from random import randint
#global variables
frontside=[]
backside=[]
amount=-1
characterPosition=0

class Window(Frame):

    def __init__(self, master=None):
        #initialize a frame
        Frame.__init__(self,master)
        #bind enter to submit button
        master.bind('<Return>',self.submit)
        #properties of window
        self.master=master
        self.importButton=None
        self.label=None
        self.entry=None
        self.submitButton=None
        self.currentFront=None
        self.init_window()
        self.put_text("Welcome")
        
    #functions for the window
    
    def init_window(self):
        #title of window
        self.master.title("Flash cards for Chinese characters")
        self.pack(fill=BOTH, expand=1)
        #button quit 
        quitButton= Button(self, text="Quit", borderwidth=2, height=3,
                           width=6, command=self.quitClient)
        quitButton.place(x=420,y=330)
        #button import
        self.importButton = Button(self, text="Import", borderwidth=2, height=3,
                             width=6, command=self.uploadFile)
        self.importButton.place(x=350,y=330)

    #command to put in the main label
    def put_text(self,texts):
        self.label = Label(self, text=texts, font=("Times",15))
        self.label.pack(side="top", fill="x", pady=10)
    
    #command to quit the client
    def quitClient(self):
        root.destroy()
    
    #upload file button
    def uploadFile(self):
        filename= filedialog.askopenfilename()
        global amount
        amount=0
        #parsing for chinese characters
        with open(filename,"r",encoding="utf8") as f:
            for line in f:
                amount+=1
                frontside.append(line)
                frontside[-1]=frontside[-1].strip()
                backside.append(frontside[-1][2:])
                frontside[-1]=frontside[-1][0]
        #display remaining charaters to go
        self.label.config(text="This list has"+ " " + str(amount)+ " " +"characters remaining")
        amount-=1
        #hide import button after selecting list
        self.importButton.destroy()
        #display first character
        global characterPosition
        characterPosition= randint(0,amount)
        self.displayFront(frontside[characterPosition])
        #display submit entry
        self.entry=Entry(self)
        self.entry.pack(side="top", fill="none",pady=5)
        self.entry.focus_set()
        #display submit button
        self.submitButton = Button(self, text="Submit", borderwidth=2, height=1,
                             width=10, command=self.submit)
        self.submitButton.place(x=208,y=135)
        
    #function for submit button    
    def submit(self,event=None):
        global characterPosition
        global amount
        #the if statement nullifies the enter button command
        if amount==(-1):
            return
        else :
            #get the input and clear it
            inputString=self.entry.get()
            self.entry.delete(0, END)
            #if the character is inputted right
            if (inputString==backside[characterPosition]):
                #remove that character and its answer from the list
                del frontside[characterPosition]
                del backside[characterPosition]
                if (amount!=0):
                    self.label.config(text="This list has"+ " " + str(amount)+ " " +"characters remaining")
                    amount-=1
                    #when theres only one character remaining randint does not work so select the first one
                    if amount==0:
                        characterPosition=0
                        self.currentFront.config(text=frontside[characterPosition])
                    #otherwise choose a random character from the remaining ones
                    else:
                        characterPosition= randint(0,amount)
                        self.currentFront.config(text=frontside[characterPosition])
                    self.entry.focus_set()
                #every character was correct
                else :
                    self.label.config(text="Every card has been used!")
                    self.submitButton.destroy()
                    self.currentFront.destroy()
                    self.entry.destroy()
                    amount-=1
                    #reappear of import button 
                    self.importButton = Button(self, text="Import", borderwidth=2, height=3,
                             width=6, command=self.uploadFile)
                    self.importButton.place(x=350,y=330)
            #wrong answer
            else :
                 self.label.config(text="Sorry, but this is incorrect")
        
    #function to display the first word of the card
    def displayFront(self,texts):
        self.currentFront = Label(self, text=texts, font=("Microsoft Yahei",20))
        self.currentFront.pack(side="top", fill="x", pady=10)
        
root= Tk()
root.geometry("500x400")
#organise
app= Window(root)
#for keeping the window open
root.mainloop()
