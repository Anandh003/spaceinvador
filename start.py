import os
import sys
import turtle
import time
import math
import threading
from random import randint



turtle.register_shape('assets/bg.gif')
turtle.register_shape("assets/ship.gif")
turtle.register_shape("assets/invador.gif")
turtle.title('Space Invador')

def moveRight():
    x = player.xcor()
    x += 10
    player.setx(x)

def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx(x)

def moveDown():
    y = player.ycor()
    y -= 10
    player.sety(y)

def moveUp():
    y = player.ycor()
    y += 10
    player.sety(y)

def firebullet():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollosion(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 35:
        return True

    return False

def update_score(score):
    score_obj.clear()
    score_obj.color('white')
    score_obj.penup()
    score_obj.setposition(-300, 280)
    score_obj.write('your Score is {}'.format(score), move=False, align='left', font=('Arial', 18, 'normal'))
    score_obj.hideturtle()
    

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(2,2)
bullet.hideturtle()
bullet_speed = 50
bullet_state = 'ready'

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.setposition(-300,300)
writer.pendown()

wn = turtle.Screen()
wn.listen()
wn.bgpic('assets/bg.gif')


wn.onkey(moveRight, 'd')
wn.onkey(moveLeft, 'a')
wn.onkey(moveUp, 'w')
wn.onkey(moveDown, 's')
wn.onkey(firebullet, 'space')

for x in range(3):
    writer.forward(600)
    writer.right(90)
writer.forward(600)

player = turtle.Turtle()
player.setposition(0, -200)
player.shape('assets/ship.gif')
player.penup()

enemies = []
score = 0
isGameOver = False
score_obj = turtle.Turtle()
update_score(score)

for x in range(50):
    enemies.append(turtle.Turtle())

for row in range(5):
    for col in range(10):
        indx = (row * 10) + col
        x = -250 + col * 50
        y = 250 - row * 50   
        enemies[indx].speed(0)
        enemies[indx].shape('assets/invador.gif')
        enemies[indx].penup()
        enemies[indx].setposition(x, y)
        # enemies.append(enemy)

while True:
    for enemy in enemies:
        if isCollosion(enemy, bullet) and bullet_state =='fire':
            bullet.hideturtle()
            bullet_state = 'ready'
            enemy.clear()
            enemy.ht()
            enemies.remove(enemy)
            score += 1
            update_score(score)

        if enemy.xcor() > 270:
            enemy.speed(0)
            enemy.setx(-270)
            y = enemy.ycor()
            enemy.sety(y-40)

        if enemy.ycor() < -260:
            enemy.speed(0)
            enemy.sety(300)

        if isCollosion(player, enemy):
            player.hideturtle()  
            turtle.color('red')
            turtle.penup()
            turtle.setposition(0, 0)
            turtle.hideturtle()
            turtle.write("Game Over!", move=False, align="center", font=("Arial", 35, "normal"))
            turtle.setposition(0, -50)      
            turtle.write("Your score is: {}".format(score), move=False, align="center", font=("Arial", 35, "normal"))
            isGameOver = True
            break

        x = enemy.xcor()
        x += 30
        enemy.setx(x)

    if len(enemies) == 0:
        turtle.color('green')
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.hideturtle()
        turtle.write("Game completed!!", move=False, align="center", font=("Arial", 35, "normal"))
        break
    elif isGameOver:
        break

    if player.xcor() > 260:
        player.speed(0)
        player.setx(-260)
    if player.xcor() < -260:
        player.speed(0)
        player.setx(260)
    if player.ycor() < -260:
        player.sety(-260)
    if bullet_state == 'fire':
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > 270:
            bullet_state = 'ready'
            bullet.hideturtle()
    


time.sleep(5)
turtle.clear()
turtle.color('red')
turtle.penup()
turtle.setposition(0, 0)
turtle.hideturtle()
turtle.write("Thanks for Playing!!", move=False, align="center", font=("Arial", 35, "normal"))
time.sleep(3)
turtle.bye()
# turtle.close()



#triangle
# writer.pendown()
# writer.forward(100)
# writer.left(90)
# writer.forward(100)
# writer.left(135)
# writer.forward(141)
# time.sleep(5)

#Square
# writer.color('green')
# writer.pendown()
# for x in range(3):
#     writer.forward(100)
#     writer.right(90)
# writer.forward(100)
# time.sleep(2)