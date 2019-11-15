# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:26:01 2019

@author: v6508
"""
import random
from turtle import Turtle, Screen

class Ventana:
    def __init__(self,wn):
        self.wn=wn
        self.wn.title("El ping pong más perrón")
        self.wn.bgcolor("black")
        self.wn.setup(width = 800, height = 600)
        self.wn.tracer(0)
    def Teclas(self, pa, pb):
        self.wn.listen()
        self.wn.onkeypress(pa.arriba,"w")
        self.wn.onkeypress(pa.abajo,"s")
        self.wn.onkeypress(pb.arriba,"Up")
        self.wn.onkeypress(pb.abajo,"Down")
        self.wn.onkeypress(pb.toogleActivacion,"1")
        self.wn.onkeypress(pb.toogleGrande,"g")
        

class Paleta(Turtle):
    def __init__(self, x):
        Turtle.__init__(self)
        self.x = x        
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.x, 0)
        self.largo = 5
        self.shapesize(stretch_wid=self.largo, stretch_len=1)
        self.puntaje = 0
        self.activacion = True
        self.grande = False
        
    def toogleGrande(self):
        if not self.grande:
            self.shapesize(stretch_wid=self.largo*2, stretch_len=1)
            self.grande = True
        else:
            self.shapesize(stretch_wid=self.largo, stretch_len=1)
            self.grande = False
    
    def toogleActivacion(self):
        if self.activacion:
            self.activacion=False
        else:
            self.activacion=True
    
    def auto(self, pe):                                                                                                                                                                                             
        if self.activacion==False:
            self.goto(self.x, pe.ycor()+1)
        
    def arriba(self):
        if self.activacion:
            y = self.ycor()
            self.sety(y+20)
        
        
    def abajo(self):
        if self.activacion:
            y = self.ycor()
            self.sety(y-20)

    def hitBox(self, pe):
        val = [-1.0,1.0]
        if (pe.xcor() <= self.xcor() + 20 and 
                pe.xcor() >= self.xcor() - 20) and (
                pe.ycor() < self.ycor() +(self.largo/5*70) and 
                pe.ycor() > self.ycor() -(self.largo/5*70)):
            pe.dx*=-1.0
            pe.dy *=random.sample(val,1)
        

class Pelota(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.25
        self.dy = 0.2
        self.acel = 1.0002

class Fisicas:
    def __init__(self,pe,pa,pb):
        self.pe = pe
        self.pa = pa
        self.pb = pb
        
    def movimiento(self):
        self.pe.sety(self.pe.ycor() + self.pe.dy)
        self.pe.setx(self.pe.xcor() + self.pe.dx)
        self.pe.dy *= self.pe.acel
        self.pe.dx *= self.pe.acel
        
    def bordes(self):
        if self.pe.ycor() > 290 or self.pe.ycor() < -290:
            self.pe.dy *= -1
        if self.pe.xcor() > 342:
            self.pe.goto(0,0)
            self.pa.puntaje+=1
            self.pe.dx = 0.25
            self.pe.dy = 0.25
        if self.pe.xcor() < -342:
            self.pe.goto(0,0)
            self.pb.puntaje+=1
            self.pe.dx = -0.25
            self.pe.dy = 0.25
    
    def hitboxesUpdate(self):
        self.pa.hitBox(self.pe)
        self.pb.hitBox(self.pe)
        
        
class Score(Turtle):
    def __init__(self,pa,pb):
        Turtle.__init__(self)
        self.pa=pa
        self.pb=pb
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        
    def scoreUpdate(self):
        self.clear()
        self.write("Jugador 1: {} | Jugador 2: {}".format(self.pa.puntaje,self.pb.puntaje), align="center", font=("Courier", 24,"normal"))
        
        
        
def main():
    wn = Screen()
    vn = Ventana(wn)
    pa = Paleta(-350)
    pb = Paleta(350)
    pe = Pelota()
    vn.Teclas(pa,pb)
    fi = Fisicas(pe,pa,pb)
    sc = Score(pa,pb)
    while True:
        wn.update()
        sc.scoreUpdate()
        fi.movimiento()
        fi.bordes()
        fi.hitboxesUpdate()
        pb.auto(pe)
    
if __name__ == "__main__":
    main()
