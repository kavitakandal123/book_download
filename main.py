'''main app thing that has the tkinter coding'''
from searchBooks import *
from tkinter import *
from books import *
from bs4 import BeautifulSoup
import requests
root = Tk()
count = 0
def showFrame():
    bottomFrame = Frame(root, height=200, width=300)
    bottomFrame.pack(side=BOTTOM)
    return bottomFrame
bottomFrame = showFrame()
def buttonList(searchedItem):
    global count,bottomFrame
    count+=1

    def showButtonList(bottomFrame):
        for element in searchedItem:
            Button(bottomFrame,text=element, border= 0, bg='pink', command= showCallBack(element)).pack()#grid()
    showButtonList(bottomFrame)

    if count>1:
        bottomFrame.destroy()
        bottomFrame = showFrame()
        showFrame()
        showButtonList(bottomFrame)

def showCallBack(element):
    def CallBack():
        return bookInfo(element)
    return CallBack

#display the content of book and
def bookInfo(bookName):
    new = Toplevel(root)
    new.title('Book Information')
    bookDict = bookRetrieve()
    bookLink = bookDict[bookName]
    sourceCode = requests.get(bookLink).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    bookPage = '\n'
    j=0
    for line in soup.findAll('p'):
        while(j<40):
            if line.string != None:
                i = 0

                if len(line.string)>150:
                    while i < len(line.string.split('.', 5)):
                        bookPage += line.string.split('.',5)[i] +'\n'
                        i+=1
                else:
                    bookPage+=line.string+'\n'
            j+=1
    Label(new,text=bookName,fg='green',anchor=W,justify=LEFT).pack()
    Button (new, bd=3, text='Download Complete Book', command=lambda: bookDownload(bookLink,bookName),bg='purple').pack()
    Label(new ,text=bookPage, height=400, width=400, anchor=W, fg='blue', justify=LEFT).pack()
    new.mainloop()



root.title('Book Downloading Application')
s = StringVar()
frame = Frame(root,bd=1,height=500,width=800)
searchQuery = Entry(frame ,textvariable=s).pack()

def getEntryText():
    buttonList(bookSearch(s.get()))

searchButton = Button(frame,text='Search',border= 3, bg='purple',command= getEntryText).pack()
frame.pack()
root.mainloop()