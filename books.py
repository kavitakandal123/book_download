'''Download book from 8novels.net '''
import requests
from bs4 import BeautifulSoup
import tkinter.messagebox

# download books here using any url
def bookDownload(url,bookName):
    sourceCode=requests.get(url).text
    soup = BeautifulSoup(sourceCode,'html.parser')

    # get the last page no. of book to download whole book
    for soupLine in soup.findAll('div',{'class':'dede_pages'}):
         for soupLine2 in soupLine.findAll('ul',{'class':'pagelist'}):
               pages = soupLine2.li.a.string.split()
               lastPageNo = int(pages[0])
               print(lastPageNo)
    pageNo = 1

    #finally download book in a word file
    bookName = bookName.split('(', 1)[0] + '.doc'
    book = open(bookName, 'a', 4)
    while (pageNo <= lastPageNo):
        print(pageNo)
        if pageNo>1:
           pageUrl = url+'index_'+str(pageNo)+'.html'
        else:
           pageUrl = url
        sourceCode = requests.get(pageUrl).text
        soup = BeautifulSoup(sourceCode,'html.parser')
        book.write(bookName + '\n')
        for bookContent in soup.findAll('p'):
            if bookContent.string!=None:
                book.write(bookContent.string+'\n')
        pageNo+=1
    else:
        message=tkinter.messagebox.showinfo('Download status','Download Complete')
