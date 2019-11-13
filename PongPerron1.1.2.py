# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:38:46 2019

@author: ALVARO SOTELO
"""

import turtle

class Ventana:
    def __init__(self,wn):
        wn.title("El ping pong más perrón")
        wn.bgcolor("black")
        wn.setup(width = 800, height = 600)
        wn.tracer(0)
        

class Paleta:
    def __init__(self, x):
        self.paleta = turtle.Turtle()
        self.x = x
        self.paleta.speed(0)
        self.paleta.shape("square")
        self.paleta.color("white")
        self.largo = 5
        self.paleta.penup()
        self.paleta.goto(self.x, 0)
        self.puntaje = 0
        self.activacion = True
        self.paleta.shapesize(stretch_wid=self.largo, stretch_len=1)
        
    def grande(self):
        self.paleta.shapesize(stretch_wid=self.largo*2, stretch_len=1)
        
    
    def toogleActivacion(self):
        if self.activacion:
            self.activacion=False
        else:
            self.activacion=True
    
    def auto(self, pe):
        if self.activacion==False:
            self.paleta.goto(self.x, pe.pelota.ycor()+1)
        
    def arriba(self):
        if self.activacion:
            y = self.paleta.ycor()
            self.paleta.sety(y+20)
        
        
    def abajo(self):
        if self.activacion:
            y = self.paleta.ycor()
            self.paleta.sety(y-20)

    def hitBox(self, pe):
        if (pe.pelota.xcor() <= self.paleta.xcor() + 20 and 
                pe.pelota.xcor() >= self.paleta.xcor() - 20) and (
                pe.pelota.ycor() < self.paleta.ycor() +(self.largo/5*70) and 
                pe.pelota.ycor() > self.paleta.ycor() ):
            pe.dx*=-1.0
            if  pe.dy<0:
                pe.dy *=-1
        if (pe.pelota.xcor() <= self.paleta.xcor() + 20 and 
                pe.pelota.xcor() >= self.paleta.xcor() - 20) and (
                pe.pelota.ycor() < self.paleta.ycor() and 
                pe.pelota.ycor() > self.paleta.ycor() -(self.largo/5*70) ):
            pe.dx*=-1.0    
            if  pe.dy>0:
                pe.dy *=-1

class Pelota:
    def __init__(self):
        self.pelota = turtle.Turtle()
        self.pelota.speed(0)
        self.pelota.shape("circle")
        self.pelota.color("white")
        self.pelota.penup()
        self.pelota.goto(0, 0)
        self.dx = 0.25
        self.dy = 0.2
        self.acel = 1.0002

class Fisicas:
    def __init__(self,pe,pa,pb):
        self.pe = pe
        self.pa = pa
        self.pb = pb
        
    def movimiento(self):
        self.pe.pelota.sety(self.pe.pelota.ycor() + self.pe.dy)
        self.pe.pelota.setx(self.pe.pelota.xcor() + self.pe.dx)
        self.pe.dy *= self.pe.acel
        self.pe.dx *= self.pe.acel
        
    def bordes(self):
        if self.pe.pelota.ycor() > 290 or self.pe.pelota.ycor() < -290:
            self.pe.dy *= -1
        if self.pe.pelota.xcor() > 342:
            self.pe.pelota.goto(0,0)
            self.pa.puntaje+=1
            self.pe.dx = 0.25
            self.pe.dy = 0.25
        if self.pe.pelota.xcor() < -342:
            self.pe.pelota.goto(0,0)
            self.pb.puntaje+=1
            self.pe.dx = -0.25
            self.pe.dy = 0.25
    
    def hitboxesUpdate(self):
        self.pa.hitBox(self.pe)
        self.pb.hitBox(self.pe)
        
        
class Score:
    def __init__(self,pa,pb):
        self.pa=pa
        self.pb=pb
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,260)
    def scoreUpdate(self):
        self.pen.clear()
        self.pen.write("Jugador 1: {} | Jugador 2: {}".format(self.pa.puntaje,self.pb.puntaje), align="center", font=("Courier", 24,"normal"))
        
        
class Tecla:
    def __init__(self,wn,pa,pb,pe):
        wn.listen()
        wn.onkeypress(pa.arriba,"w")
        wn.onkeypress(pa.abajo,"s")
        wn.onkeypress(pb.arriba,"Up")
        wn.onkeypress(pb.abajo,"Down")
        wn.onkeypress(pb.toogleActivacion,"1")
        wn.onkeypress(pb.grande,"g")
        
        
        
def main():
    wn = turtle.Screen()
    Ventana(wn)
    pa = Paleta(-350)
    pb = Paleta(350)
    pe = Pelota()
    Tecla(wn, pa, pb, pe)
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
    
    

