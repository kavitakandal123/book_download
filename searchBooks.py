'''This file searches for books '''
import requests
import re
from bs4 import BeautifulSoup

#search for genre and then store them in genreDict dictionary
def genreStore(url=r'https://www.8novels.net'):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode,'html.parser')
    genreFile = open('8Novels_Genre.txt','w',3)
    for bookName in soup.findAll('ul'):
        for bookName2 in bookName.findAll('li'):
            genreFile.write(str(bookName2.a.string.strip() + ':' + url + bookName2.a['href'].strip() + '\n'))

#retrieve genre from 8Novels_Genre.txt file and store in genreDict and return the dict
def genreRetrieve():
    genreDict = {}
    genreFile = open('8Novels_Genre.txt')
    file = genreFile.read()
    for k in file.splitlines():
        genreList = k.split(':',1)
        genreDict.update({genreList[0] : genreList[1] })
    return genreDict

#search for genre and then store them in genreDict dictionary
def bookStore():
    genreDict = genreRetrieve()
    bookFile = open('8Novels_books.txt','w')
    for book,link in genreDict.items():
        sourceCode = requests.get(link).text
        soup = BeautifulSoup(sourceCode, 'html.parser')
        for s1 in soup.findAll('li'):
            for s2 in soup.findAll('span', {'class': 'pageinfo'}):
                lastPageNo = int(s2.strong.string)
        i = 1
        while i<=lastPageNo:
            if i > 1:
                link2 = link + str(i) +'.html'
                sourceCode = requests.get(link2).text
            else:
                ourceCode = requests.get(link).text
            soup = BeautifulSoup(sourceCode, 'html.parser')
            for l in soup.findAll('a', {'class': 'a2'}):
                try:
                    bookFile.write(
                        str(l.string.strip() + ':' + 'http://www.8novels.net' + l['href'].strip() + '\n'))
                except:
                    continue
            i += 1



#retrieve genre from 8Novels_Genre.txt file and store in genreDict and return the dict
def bookRetrieve():
    bookDict = {}
    bookFile = open('8Novels_books.txt')
    file = bookFile.read()
    for book in file.splitlines():
        bookList= book.split(':',1)
        bookDict.update({bookList[0] : bookList[1]})
    return bookDict

#search for keywords of the book entered by user in the bookDict
def bookSearch(bookName):
    bookDict = bookRetrieve()
    bookSearchList = bookName.strip().split()
    bookNameList = bookDict.keys()
    matchedObjectDict = {}
    for i in bookNameList:
        try:
            for i2 in bookSearchList:
                matchedObject = re.search('.*'+i2+'.*',i,re.I)
                if matchedObject:
                    matchedObjectDict.update({i:bookDict[i]})
        except AttributeError:
            continue
    return matchedObjectDict





