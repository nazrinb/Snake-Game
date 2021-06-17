import tkinter.font as font
from tkinter import *
from turtle import * 
import time
import random

FONT = 'Comic Sans MS', 24, "bold"
COURT_HEIGHT = 600
COURT_WIDTH = 1000
CURSOR_SIZE = 20
FONT_SIZE = 12
FORWARD_DST = 15


def draw_border():
    border = Turtle(visible=False)
    border.speed('fastest')
    border.color('black')
    border.pensize(3)
    border.penup()
    border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.sety(-COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_WIDTH)
    border.pendown()
    border.sety(COURT_HEIGHT/2)

    return border

def init_pen():
    pen = Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 320)
    pen.clear()
    pen.write("Score: {}        Highest Score: {} ".format(0, 0), align="center", font=FONT)

    return pen

def init_cherry():
    cherry = Turtle()
    cherry.penup()
    cherry.pensize()
    cherry.shape('apple_00.gif')
    cherry.speed(0)
    cherry.goto(100, 0)

    return cherry 

def init_snake():
    snake = Turtle()
    snake.penup()
    snake.shape('square')
    snake.color('#021f31')
    snake.goto(-480, 0)
    snake.direction = "Stop"

    return snake

def init_screen():
    t = Turtle()
    t.hideturtle()
    
    scr = t.getscreen()
    scr.colormode(255) # to prevent bad color error
    scr.bgpic('image(2)(6).jpg')
    scr.title('Snake Game by Nazrin')
    scr.setup(width=1.0, height=1.0)
    scr.tracer(0)
    scr.addshape('apple_00.gif')

    return scr

def move(snake):
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+FORWARD_DST)
    
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-FORWARD_DST)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-FORWARD_DST)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+FORWARD_DST)

def init_segment():
    new_segment = Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color('#021f31')
    new_segment.penup()   

    return new_segment 