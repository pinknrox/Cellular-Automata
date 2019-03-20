from Tkinter import *

import networkx as nx
import random
import math
import operator
import numpy as np
import sys
root=Tk()
c=Canvas(root,width=650,height=650)
c.pack()

Maze= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1],
[1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1],
[1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
[1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
[1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
[1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1],
[1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
[1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1],
[1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
[1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1],
[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
[1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1],
[1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1],
[1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
[1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1],
[1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1],
[1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
[1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1],
[1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]




#def get_color(self, x, y):

        #if self.maze.start_cell == (x, y):

            #return 'red'

        #if self.maze.exit_cell == (x, y):

            #return 'green'

        #if self.maze.maze[y][x] == 1:

            #return 'black'



MazeBG=[]

B1=0
Arg=0
Dep=15

for Col in Maze:
    A1=0
    for j in Col:
        if j ==1:
            MazeBG.append([A1,B1,'black',Arg])
        else:
            MazeBG.append([A1,B1,'white',Arg])
        A1+=1
        Arg+=1
    B1+=1


G = nx.Graph()
row=len(Maze)+1
edge=[]
border=[]
point={}
for DAT in MazeBG:
    point[(DAT[0],DAT[1])]=DAT[3]
    if DAT[2]=='white':
        edge.append((DAT[0],DAT[1]))
neighbor={}
G.add_nodes_from(edge)

 #x0, y0 = cell

        #x1, y1 = neighbor

        # Vertical

        #if x0 == x1:

            #x = x0

            #y = (y0 + y1) / 2

        # Horizontal

        #if y0 == y1:

            #x = (x0 + x1) / 2

            #y = y0

        #self.maze[y][x] = 0 # remove wall






for DAT in MazeBG:

    a=DAT[0]
    b=DAT[1]
    BG=DAT[2]
    North=DAT[1]-1
    South=DAT[1]+1
    East=DAT[0]+1
    West=DAT[0]-1
    static=[(a,b,0.8),(East,b,1),(West,b,1),(a,North,1),(a,South,1),(East,North,math.sqrt(2)),(West,North,math.sqrt(2)),(East,South,math.sqrt(2)),(West,South,math.sqrt(2))]

#x, y = cell

        #neighbors = []



        #if x - 2 > 0:

            #neighbors.append((x-2, y))

        #if x + 2 < self.width:

            #neighbors.append((x+2, y))
        #if y - 2 > 0:

            #neighbors.append((x, y-2))


        #if y + 2 < self.height:

            #neighbors.append((x, y+2))






    if BG =='white':
        for Neighbors in static:
            if MazeBG[point[(Neighbors[0],Neighbors[1])]][2]=='white':
                border.append([(Neighbors[0],Neighbors[1]),(DAT[0],DAT[1]),Neighbors[2]])
                if (DAT[0],DAT[1]) in neighbor:
                    neighbor[(DAT[0],DAT[1])]=neighbor[(DAT[0],DAT[1])]+[(Neighbors[0],Neighbors[1])]
                else:
                    neighbor[(DAT[0],DAT[1])] =[(Neighbors[0],Neighbors[1])]





G.add_weighted_edges_from(border)
Exit_Point=(17,41)
length= nx.single_source_shortest_path_length(G,Exit_Point)
normal=0


#Border 
for i in MazeBG:
    c.create_rectangle(i[0]*Dep,i[1]*Dep,i[0]*Dep+Dep,i[1]*Dep+Dep,fill=i[2],outline="black")
c.update()
c.after(1000)


#class Rectangle(object):

    #def __init__(self, width, height, x, y, index, canvas, delay):

        #self.delay = delay

        #self.canvas = canvas

        #self.width = width

        #self.height = height

        #self.x = x

        #self.y = y

        #self.index = index

        #            [left, right, top, bot]

        #self.walls = [True, True, True, True]

        #self.virgin = True

        #self.col = self.x / self.width

        #self.row = self.y / self.height
g=0
class ball:
    def __init__(self,a,b,Dep):
        self.a,self.b=a,b
        self.Dep=Dep
    def draw(self):
        self.Oval=c.create_oval(self.a*Dep,self.b*Dep,self.a*Dep+Dep,self.b*Dep+Dep,fill='green',outline='black')
        return self.a,self.b,self.Dep,self.Oval
    def move(self,A1,B1):
        self.A1,self.B1=A1,B1
        c.coords(self.Oval,self.A1*self.Dep,self.B1*self.Dep,self.A1*self.Dep,self.B1*self.Dep+self.Dep)



        #def show(self, verbose=False):


        #x0, y0 = self.exit_cell

        #self.maze[y0][x0] = 2

        #x1, y1 = self.start_cell

        #self.maze[y1][x1] = 3

        #for row in self.maze:

            #print ' '.join([MAP[col] for col in row])

        #if verbose:

            #print "Steps from A to B:", self.steps

Ball_Number=10
Start=[]
Person=[]
Appear=random.sample(edge,Ball_Number)



Start=Appear
for i in Appear:
    i=ball(i[0],i[1],Dep)
    Person.append(i)

for i in Person:
    i.draw()
c.update()
c.after(1000)


next_move={}
PATHS=[]

for i in range(Ball_Number):
    PATHS.append([Start[i]])
    next_move[Start[i]]=[Start[i]]

print (length)


while 1>0:
    First={}
    keys=next_move.keys()
    next_move={}
    print (next_move)
    for P in PATHS:
        #print (length)
        for k in length.keys():
            if k in keys:
                First[k]=0
            else:
                First[k]=math.exp(-length[k]*5)
        
        Chance = []
        Chance_move = []


        if P[-1]==Exit_Point:
            next_move[Exit_Point]=[Exit_Point]
            P.append(Exit_Point)
            continue

        for i in neighbor[P[-1]]:
            Chance.append(First[i])

        if sum(Chance)==0:
            if P[-1] in next_move.keys():
                next_move[P[-1]]=next_move[P[-1]]+[P[-1]]
            else:
                next_move[P[-1]]=[P[-1]]
            P.append(P[-1])
        else:

            for i in range(len(Chance)):
                Chance_move.append(Chance[i]/sum(Chance))
            chose=random.uniform(0,1)
            for i in range(len(neighbor[P[-1]])):
                if sum(Chance_move[:i])<chose<=sum(Chance_move[:i+1]):
                    if neighbor[P[-1]][i] in next_move.keys():
                        next_move[neighbor[P[-1]][i]]=next_move[neighbor[P[-1]][i]]+[P[-1]]
                    else:
                        next_move[neighbor[P[-1]][i]]=[P[-1]]
                    P.append(neighbor[P[-1]][i])


 #def check_move(self, x, y):

        #x0, y0 = self.get_cell_coords()

        #x1 = x0 + x

        #y1 = y0 + y

        #return self.maze.maze[y1][x1] == 0



    for k in next_move.keys():
        m=next_move[k]
        if len(m)>1:
            same=m
            Gofirst=m[random.randint(0,len(m)-1)]
            next_move[k]=[Gofirst]

            for CA in same:
                if CA != Gofirst:
                    if CA in next_move.keys():
                        next_move[CA]=next_move[CA]+[CA]
                    else:
                        next_move[CA]=[CA]
                    number =[i for i in range(len(PATHS)) if PATHS[i][-2] == CA]
                    del PATHS[number[0]][-1]
                    PATHS[number[0]].append(CA)



    next_move1=[]
    for i in range(len(Person)):
        Person[i].move(PATHS[i][-1][0],PATHS[i][-1][1])
        next_move1.append([i,PATHS[i][-1][0],PATHS[i][-1][1]])

    c.update()
    c.after(50)
    g+=1


