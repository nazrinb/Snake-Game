from tkinter import *
from helpers import *
from turtle import *

import tkinter.font as font 
import time
import random


def init_game():
    segments = []
    high_score = 0
    score = 0
    delay = 0.1    
 
    # initialize game resources
    scr = init_screen()
    cherry = init_cherry()
    snake = init_snake()
    pen = init_pen()
    border = draw_border()

    # snake movement functions
    def go_up():
        if snake.direction != "down":
            snake.direction = "up"
    def go_down():
        if snake.direction != "up":
            snake.direction = "down"
    def turn_left():
        if snake.direction != "right":
            snake.direction = "left"
    def turn_right():
        if snake.direction != "left":
            snake.direction = "right"

    # respond to user input
    scr.listen()
    scr.onkeypress(go_up, "Up")
    scr.onkeypress(go_down, "Down")
    scr.onkeypress(turn_left, "Left")
    scr.onkeypress(turn_right, "Right")

    # Main game loop
    while True:
        scr.update()

        # Check for collision 
        if snake.xcor() > 485 or snake.xcor() < -485 or \
           snake.ycor() > 280 or snake.ycor() < -280:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "Stop"

            # hide the old segments:
            for segment in segments:
                segment.goto(2000, 2000)
            segments.clear() #clear old segments 
            
            score = 0 # reset score after hitting border
            delay = 0.1
            pen.clear()
            pen.write("Score: {}        Highest Score: {} ".format(
                      score, high_score), align="center", font=FONT)

        # move the food to a random position on screen 
        if snake.distance(cherry) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            cherry.goto(x, y)

            new_segment = init_segment()
            segments.append(new_segment)
            
            delay -= 0.001
            score += 10
            high_score = max(high_score, score)

            pen.clear()
            pen.write("Score: {}        Highest Score: {} ".format
                     (score, high_score), align="center", font=FONT)

        # make segments follow snake 
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y)
        
        move(snake)

        # segment and snake collision
        for segment in segments:
            if segment.distance(snake) < 15:
                time.sleep(1)
                snake.goto(0,0)
                snake.direction = 'stop'

                for segment in segments:
                    segment.goto(1000,1000)
                segments.clear()

                score = 0
                delay = 0.1

                pen.clear()
                pen.write("Score: {}        Highest Score: {} ".format
                       (score, high_score), align="center", font=FONT)
        time.sleep(delay)
    scr.mainloop()

if __name__ == "__main__":
    init_game()
