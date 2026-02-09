import turtle
import time
import random
import os
os.system('pip install pyautogui')
import webbrowser
import pyautogui
import threading

wn = turtle.Screen()
wn.title("67")
wn.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
wn.colormode(255)

running = True

def force_fullscreen():
    while running:
        pyautogui.press('f11')
        pyautogui.press('up', presses=10) 
        pyautogui.moveTo(0, 1000)
        time.sleep(0.1)

threading.Thread(target=force_fullscreen, daemon=True).start()


def open_link():
    webbrowser.open_new("https://youtu.be/L7ejl_Hj3A8?si=6YBW660BWeg2texS")
    time.sleep(1)
    pyautogui.press('f11')
    time.sleep(2.5)
    pyautogui.press('f')
    


t = turtle.Turtle()
t.speed(6)
t.pensize(50)
t.ht()


def draw_6():
    t.down()
    t.left(180)
    t.forward(250)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(250)
    t.up()
    t.setheading(0)


def draw_7():
    t.down()
    t.forward(250)
    t.right(90)
    t.forward(600)
    t.left(180)
    t.forward(300)
    t.left(90)
    t.forward(100)
    t.backward(200)
    t.up()
    t.setheading(0)


t.up()
t.goto(-100, 300)
draw_6()

t.up()
t.goto(50, 300)
draw_7()


for i in range(120):
    x = random.randint(-950, 950)
    y = random.randint(-500, 500)
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    t.speed(0)
    t.goto(x, y)
    t.color(c1, c2, c3)
    t.write("67", font=("Arial", 50, "normal"))

open_link()
time.sleep(5)
turtle.bye()
