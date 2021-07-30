import random
from random import randint
lan = input("Choose language / Dil seçiniz (EN/TR)")
tr = ["tr","Tek oyuncu mu çok oyuncu mu? (Tek oyuncu için s çok oyuncu için m)","Kelime Giriniz: "," \nTebrikler kazandınız \n ","\nHarf veya kelime giriniz: ","Lütfen bir kelime giriniz","\nKalan canlar : ","\nTebrikler, harf, kelimede bulunmakta\n ", "KAYBETTIÜİNİZ"]
en = ["en","Multiplayer or Singleplayer? (M/S)","Please Enter a Word: "," \nCongragulations! You won!\n ","\nEnter a word or a letter: ","Please enter a word","\nRemaining HP: ","Congragulations, letter is in the word.","YOU PERISHED"]
if lan.lower() == "en":
	lan = en
else:
	lan = tr
player = input(lan[1])
wordsFile = open(lan[0]+'.txt', 't')
words = wordsFile.read().splitlines()
print(words)
if player.lower() == "m" or player.lower() == "multiplayer":
    player = "multiplayer"
else:
    player = "singleplayer"
def ranWord():
    return (words[randint(0,len(words-1))])
def lowList(iList):
    a = 0
    try:
        for i in iList:
            iList[a] = i.lower()
            a+=1
        return(iList)
    except:
        return("")
while(True):
    if player == "multiplayer":
        word = input(lan[2])
    else:
        word = ranWord()
    h = 30
    a = word.split(" ")
    p = ""
    while "" in a:
        a.remove("")
    for i in range(len(a)-1):
        p+=a[i]
        p+=" "
    try:
        p += a[len(a)-1]
    except:
        pass
    solved = False
    l = []
    rList = []
    for i in range(4):
        print("\n")
    while(solved == False and h>0):
        d = ""
        for t in p:
            if t.lower() not in lowList(l) and t!=" ":
                d+= "_"
            elif t == " ":
                d+=" "
            else:
                d+= t
        print(d)
        if d.lower() == p.lower():
            print(lan[4])
            solved = True
        if solved == False:
            w = input(lan[4])
            if w == "" and not solved:
                print(lan[5])
            if w.lower() == p.lower():
                print(lan[3])
                print(p)
                print(lan[6] + str(h)+" \n ")
                solved = True
            elif w.lower() in p.lower() and w.lower() not in lowList(l):
                l.append(w)
                print(lan[7])
            else:
                h -= 1
                print(lan[6] + str(h)+" \n ")

if solved:
    print(lan[4])
elif h == 0:
    print(lan[7])
