## ___________________________________________
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|__________|__________|__________|__________|
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|__________|__________|__________|__________|
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|__________|__________|__________|__________|
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|          |          |          |          |
##|__________|__________|__________|__________|
##
##
##
## ___________________________________________
##|  ______  |  ______  |  ______  |  ______  |
##| |      | | |      | | |      | | |      | |
##| |      | | |      | | |      | | |      | |
##| |______| | |______| | |______| | |______| |
##|__________|__________|__________|__________|
##|  ______  |  ______  |  ______  |  ______  |
##| |      | | |      | | |      | | |      | |
##| |      | | |      | | |      | | |      | |
##| |______| | |______| | |______| | |______| |
##|__________|__________|__________|__________|
##|  ______  |  ______  |  ______  |  ______  |
##| |      | | |      | | |      | | |      | |
##| |      | | |      | | |      | | |      | |
##| |______| | |______| | |______| | |______| |
##|__________|__________|__________|__________|
##|  ______  |  ______  |  ______  |  ______  |
##| |      | | |      | | |      | | |      | |
##| |      | | |      | | |      | | |      | |
##| |______| | |______| | |______| | |______| |
##|__________|__________|__________|__________|
##
##________________________________________________________________________________________________
##________________________________________________________________________________________________



### IMPORTING MODULES


from time import sleep
from random import randint
from msvcrt import getch
import msvcrt
import os
from colorama import Fore, Back, Style, init
init()


### MAIN VARIABLES ###


'''oc        - It is a dictionary containing positions of tiles on the board in the form
               of tupples as key and the number in each tile as value
   posnor/pn - The positions on the board which are filled, numbered from 1-4
   posgrid/pg- The positions on the board which are filled, numbered based on position
               in the list which is the grid
   posmid/pm - The positions on the board which are filled, numbered as per middle
               of tile, where numbers are written
   orgrid    - It is a 2D matrix of the grid with empty slots
   figrid    - It is a 2D matrix of the grid with filled slots
   ch        - It is a choice of whether to play the game or quit
   score     - Your score
'''


### FUNCTIONS ###




def addtile(oc):  #function to randomly add a tile
    d=oc.keys()
    a,b=d[0]
    while (a,b) in oc:   #obtaining random empty spot
        a=randint(1,4)
        b=randint(1,4)
    va=randint(1,2)   #random value
    va*=2
    va=str(va)
    oc[(a,b)]=va   #adding new tile to oc
    return oc

def convert(a):   #function to obtain pn,pg,pm
    posnor=a.keys()   #a is oc
    posnor.sort()
    a=posnor          #a is pn
    b=[]
    c=[]
    for i in range(len(a)):
        j=a[i][0]   #row value
        k=a[i][1]   #column value
        d=5*j       #grid value of row
        e=k*2-1     #grid value of column
        for j in range(5):
            b.append((d,e))  #pg
            d-=1
        c.append((d+3,e))   #pm
    return (a,b,c)  #returning pn,pg,pm



def prnt(k,i,j,a):
    p=a[i][j][1:7]
    q=a[k][j][1:7]
    if int(p)==2:
        print ' '+Fore.WHITE+Back.WHITE+Style.BRIGHT+q+norr()+' ',
    elif int(p)==4:
        print ' '+Fore.CYAN+Back.WHITE+Style.BRIGHT+q+norr()+' ',
    elif int(p)==8:
        print ' '+Fore.CYAN+Back.CYAN+Style.BRIGHT+q+norr()+' ',
    elif int(p)==16:
        print ' '+Fore.MAGENTA+Back.CYAN+Style.BRIGHT+q+norr()+' ',
    elif int(p)==32:
        print ' '+Fore.BLUE+Back.CYAN+Style.NORMAL+q+norr()+' ',
    elif int(p)==64:      
        print ' '+Fore.CYAN+Back.MAGENTA+Style.BRIGHT+q+norr()+' ',
    elif int(p)==128:
        print ' '+Fore.MAGENTA+Back.MAGENTA+Style.BRIGHT+q+norr()+' ',
    elif int(p)==256:
        print ' '+Fore.BLUE+Back.MAGENTA+Style.NORMAL+q+norr()+' ',
    elif int(p)==512:
        print ' '+Fore.CYAN+Back.BLUE+Style.BRIGHT+q+norr()+' ',
    elif int(p)==1024:
        print ' '+Fore.MAGENTA+Back.BLUE+Style.BRIGHT+q+norr()+' ',
    else:
        print ' '+Fore.BLACK+Back.BLUE+Style.NORMAL+q+norr()+' ',


def norr():
    return Fore.WHITE+Back.BLACK+Style.NORMAL



def printgrid(a,score):
    os.system('cls')
    print 'To end the game at any time, press t'
    print
    for i in range(21):
        for j in range(9):
            if j%2==0:
                print norr()+a[i][j],
            elif a[i][j][0]=='|':
                if i%5==3:
                    prnt(i,i,j,a)
                if i%5==2:
                    prnt(i,i+1,j,a)
                if i%5==4:
                    prnt(i,i-1,j,a)
            else:
                print norr()+a[i][j], 
        if i==1:
            print Fore.MAGENTA+Back.BLACK+Style.NORMAL+"          SCORE:",score,
        print
    print Fore.RESET + Back.RESET + Style.RESET_ALL+'',


#print this if using getch
print "WARNING: please donot open with IDLE"
sleep(1)


def playturn(sc,oc,og,fg):

    global gg1
    global one
    
    pn,pg,pm=convert(oc)
    oloc={}   #copy of oc to check if move has been successful
    for i in oc:
        oloc[i]=oc[i]

        
    if len(pn)==16:   #if grid is full
        for i in range(len(pm)):
            if pn[i][0]==4 and pn[i][1]==4:
                continue
            elif pn[i][0]==4:
                if oc[pn[i]]==oc[(pn[i][0],pn[i][1]+1)]:
                    break
            elif pn[i][1]==4:
                if oc[pn[i]]==oc[(pn[i][0]+1,pn[i][1])]:
                    break
            elif oc[pn[i]]==oc[(pn[i][0]+1,pn[i][1])]:
                break
            elif oc[pn[i]]==oc[(pn[i][0],pn[i][1]+1)]:
                break
        else:
            return ([],sc)   #no more moves


    dir=msvcrt.getch()  #taking input
##    dir=raw_input()
    
    if dir=='t':
        exi=raw_input("Are you sure yuo want to stop the game? ")
        if exi[0] in 'Nn':
            oc,sc=playturn(sc,oc,og,fg)
            return (oc,sc)
        return ([],sc)
    
    if dir=='w':   #logic cannot be explained through hashtags

        gg1[1]=sc
        gg1[2]=dict(oc)

        ## move up
        
        for i in range(len(pm)):
            if pn[i][0]==1:
                continue
            elif pn[i][0]==2:
                if (1,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(1,pn[i][1])]=d
                elif oc[(2,pn[i][1])]==oc[(1,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(1,pn[i][1])]=d
                else:
                    pass
            elif pn[i][0]==3:
                if (1,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(1,pn[i][1])]=d
                elif (2,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(1,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(1,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(2,pn[i][1])]=d
                elif oc[pn[i]]==oc[(2,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(2,pn[i][1])]=d
                else:
                    pass
            elif pn[i][0]==4:
                if (1,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(1,pn[i][1])]=d
                elif (2,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(1,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(1,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(2,pn[i][1])]=d
                elif (3,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(2,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(2,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(3,pn[i][1])]=d
                elif oc[pn[i]]==oc[(3,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(3,pn[i][1])]=d
                else:
                    pass
            else:
                print "error"
        

    elif dir=='a':   #logic cannot be explained through hashtags

        gg1[1]=sc
        gg1[2]=dict(oc)
        
        ## move left
        
        for i in range(len(pm)):
            if pn[i][1]==1:
                continue
            elif pn[i][1]==2:
                if (pn[i][0],1) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],1)]=d
                elif oc[pn[i]]==oc[(pn[i][0],1)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],1)]=d
                else:
                    pass
            elif pn[i][1]==3:
                if (pn[i][0],1) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],1)]=d
                elif (pn[i][0],2) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],1)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],1)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],2)]=d
                elif oc[pn[i]]==oc[(pn[i][0],2)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],2)]=d
                else:
                    pass
            elif pn[i][1]==4:
                if (pn[i][0],1) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],1)]=d
                elif (pn[i][0],2) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],1)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],1)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],2)]=d
                elif (pn[i][0],3) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],2)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],2)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],3)]=d
                elif oc[pn[i]]==oc[(pn[i][0],3)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],3)]=d
            else:
                print "error"
        


    
    elif dir=='s':   #logic cannot be explained through hashtags

        gg1[1]=sc
        gg1[2]=dict(oc)
        
        ## move down
        
        pn.reverse()
        for i in range(len(pm)):
            if pn[i][0]==4:
                continue
            elif pn[i][0]==3:
                if (4,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(4,pn[i][1])]=d
                elif oc[(3,pn[i][1])]==oc[(4,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(4,pn[i][1])]=d
                else:
                    pass
            elif pn[i][0]==2:
                if (4,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(4,pn[i][1])]=d
                elif (3,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(4,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(4,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(3,pn[i][1])]=d
                elif oc[pn[i]]==oc[(3,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(3,pn[i][1])]=d
                else:
                    pass
            elif pn[i][0]==1:
                if (4,pn[i][1]) not in oc:
                    d=oc.pop(pn[i])
                    oc[(4,pn[i][1])]=d
                elif (3,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(4,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(4,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(3,pn[i][1])]=d
                elif (2,pn[i][1]) not in oc:
                    if oc[pn[i]]==oc[(3,pn[i][1])]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(3,pn[i][1])]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(2,pn[i][1])]=d
                elif oc[pn[i]]==oc[(2,pn[i][1])]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(2,pn[i][1])]=d
                else:
                    pass
            else:
                print "error"



        
    elif dir=='d':   #logic cannot be explained through hashtags

        gg1[1]=sc
        gg1[2]=dict(oc)
        
        ## Move right

        pn.reverse()
        for i in range(len(pm)):
            if pn[i][1]==4:
                continue
            elif pn[i][1]==3:
                if (pn[i][0],4) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],4)]=d
                elif oc[pn[i]]==oc[(pn[i][0],4)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],4)]=d
                else:
                    pass
            elif pn[i][1]==2:
                if (pn[i][0],4) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],4)]=d
                elif (pn[i][0],3) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],4)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],4)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],3)]=d
                elif oc[pn[i]]==oc[(pn[i][0],3)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],3)]=d
                else:
                    pass
            elif pn[i][1]==1:
                if (pn[i][0],4) not in oc:
                    d=oc.pop(pn[i])
                    oc[(pn[i][0],4)]=d
                elif (pn[i][0],3) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],4)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],4)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],3)]=d
                elif (pn[i][0],2) not in oc:
                    if oc[pn[i]]==oc[(pn[i][0],3)]:
                        d=oc.pop(pn[i])
                        d=int(d)
                        d*=2
                        sc+=d
                        d=str(d)
                        oc[(pn[i][0],3)]=d
                    else:
                        d=oc.pop(pn[i])
                        oc[(pn[i][0],2)]=d
                elif oc[pn[i]]==oc[(pn[i][0],2)]:
                    d=oc.pop(pn[i])
                    d=int(d)
                    d*=2
                    sc+=d
                    d=str(d)
                    oc[(pn[i][0],2)]=d
                else:
                    pass

    elif dir=='u':
        if one==' ':
            print "You can't undo something you haven't done.  #deep"
            oc,sc=playturn(sc,oc,og,fg)
            return (oc,sc)
        if one==True:
            print "You can't use the undo move twice! Play again."
            oc,sc=playturn(sc,oc,og,fg)
            return (oc,sc)
        else:
            one=True
            gg1=tuple(gg1)
            ggg,sc,oc=gg1
            oc=newgrid(sc,oc, og, fg)
            gg1=list(gg1)
            return (oc,sc)

                
    else:   #play again
        oc,sc=playturn(sc,oc,og,fg)
        return (oc,sc)
    if oloc==oc:
        oc,sc=playturn(sc,oc,og,fg)
        return (oc,sc)

    one=False
    
    oc=addtile(oc)
    oc=newgrid(sc,oc,og,fg)
    return (oc,sc)
    

def newgrid(sc,oc, og, fg):   #function to create game grid-gg
    gg=[['' for i in range(9)]for j in range(21)]
    posnor,posgrid,posmid=convert(oc)
    for i in range(21):
        for j in range(9):
            if (i,j) in posgrid:   #if tile is present in the location
                gg[i][j]=fg[i][j]
            else:
                gg[i][j]=og[i][j]
    for i in range(len(posmid)):
        c=0
        while len(oc[posnor[i]])<4:  #adding spaces to fit the box
            if c%2==0:
                oc[posnor[i]]=" "+oc[posnor[i]]
            else:
                oc[posnor[i]]+=" "
            c+=1
        gg[posmid[i][0]][posmid[i][1]]='| '+oc[posnor[i]]+' |'
    printgrid(gg,sc)
    return oc

def htp():
    print '''HOW TO PLAY
2048 is a single-player puzzle game, played on 4x4 grid. The objective
is to slide numbered tiles on a grid to combine them and create a tile with the
number 2048. Every turn, a new tile will randomly appear in an empty spot on the
board with a value of either 2 or 4. Tiles slide as far as possible in the
chosen direction until they are stopped by either another tile or the edge of
the grid. If two tiles of the same number collide while moving, they will merge
into a tile with the total value of the two tiles that collided. The resulting
tile cannot merge with another tile again in the same move. A scoreboard on the
upper-right keeps track of the user's score. The game is won when a tile with a
value of 2048 appears on the board. When the player has no more moves, the game
ends.

If you're too lazy to read that...
Use the w,a,s,d keys and find out what happens :)'''    




### GRIDS ###





orgrid=[[' ','________','_','________','_','________','_','________',' '],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','________','|','________','|','________','|','________','|']]

figrid=[[' ','________','_','________','_','________','_','________',' '],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','________','|','________','|','________','|','________','|'],
        ['|','        ','|','        ','|','        ','|','        ','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','|      |','|','|      |','|','|      |','|','|      |','|'],
        ['|','________','|','________','|','________','|','________','|']]








### MAIN CODE ###




### Full Screen


# ??????????


### How to play

help=raw_input('''Do you know how to play 2048?
    Enter YES if you know
    or NO if you donot know
        ->''')
if help in 'NOPENopenope':
    htp()



### Game Begins


print "CONTROLS: Use the w,a,s,d keys for up down left and right. Press u to undo once."
sleep(3)

raw_input("Press Enter when you are ready")


ch='yes'
while ch[0] in 'yY':

    gg1=[0,0,0]
    one=' '

    ###Beginning Game

    sleep(0.1)
    print "Okay then..."
    sleep(0.8)
    print "The Game",
    sleep(1)
    print "Starts",
    sleep(1)
    print "NOW!!"
    sleep(0.5)

    #initialising variables and grid values
    oc={}                                                                                                                                                                                                                                                                                                                  
    a1=randint(1,4)
    a2=randint(1,4)
    b1=randint(1,4)
    b2=randint(1,4)
    while (a1,b1)==(a2,b2):
        a1=randint(1,4)
    va1=randint(1,2)
    va1*=2
    va1=str(va1)
    va2=randint(1,2)
    va2*=2
    va2=str(va2)
    score=0
    oc[(a1,a2)]=va1
    oc[(b1,b2)]=va2

    oc=newgrid(score,oc,orgrid,figrid)

    ### 
    cont=True
    
    while cont:
        oc,score=playturn(score,oc,orgrid,figrid)
        if not oc:
            sleep(0.5)
            print "      GAME OVER      "
            print "   Your Score :", score
            print
            print
            sleep(1)
            break
        elif '2048' in oc.values():
            print "CONGRATULATIONS! YOU WON!"
            print "   Your Score :", score
            sleep(1)
            ch=raw_input("Do you want to continue playing?")
            if ch in " Nope NOPE nope ":
                sleep(1)
                print
                break

            

    ch=raw_input('''Would you like to play this game again?  ''')
    if ch[0] not in "Yy":
        ch=raw_input("Are you sure you want to exit?  ")
        if ch[0] not in 'Yy':
            ch=raw_input("So you want to play again?  ")
        else:
            ch='no'

print
print
print "Goodbye then :)"
sleep(5)
