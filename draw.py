
from tttlogicclass import *
from turtle import *
from tkinter import *


#draw out the board 

def draw():
    penup()
    speed(0)
    pensize(4)
    setposition(-100,300)
    pendown()
    right (90)
    fd (600)
    penup()
    left(90)
    fd(200)
    left(90)
    pendown()
    fd(600)
    penup()
    right(180)
    fd(200)
    left(90)
    fd(200)
    right(180)
    pendown()
    fd(600)
    penup()
    left(90)
    fd(200)
    left(90)
    pendown()
    fd(600)
    hideturtle()

draw()

game = ttt_logic()

game.currentplayer = 'X' 

canvas = getcanvas()

#pointing strings of locations to coordinates on board

def point_to_square(x, y):
    click = None
    if x > -300 and x < -100 and y > 100 and y < 300:
        print ('NorthWest')
        click = 'NorthWest'
    elif x > -100 and x < 100 and y > 100 and y < 300:
        print ('North')
        click = 'North'
    elif  x > 100 and x < 300 and y > 100 and y < 300:
        print ('NorthEast')
        click = 'NorthEast'
    elif x > -300 and x < -100 and y > -100  and y < 100:
        print ('West')
        click = 'West'
    elif x > -100 and x < 100 and y > -100  and y < 100:
        print ('Center')
        click = 'Center'
    elif  x > 100 and x < 300 and y > -100  and y < 100:
        print ('East')
        click = 'East'
    elif  x > -300 and x < -100 and y > -300 and y < -100:
        print ('SouthWest')
        click = 'SouthWest'
    elif  x > -100 and x < 100 and y > -300 and y < -100:
        print ('South')
        click = 'South'
    elif x > 100 and x < 300 and y > -300 and y < -100:
        print('SouthEast')
        click = 'SouthEast'
    else:
        print ('Do not click here')
        click = None
    return click

#finding the center coordinates to each of the locations 

def square_to_point(direction):
    if direction == 'NorthWest':
        x = -200
        y = 200
    elif direction == 'North':
        x = 0 
        y = 200
    elif direction == 'NorthEast':
        x = 200
        y = 200
    elif direction == 'West':
        x = -200
        y = 0
    elif direction == 'Center':
        x = 0
        y = 0
    elif direction == 'East':
        x = 200
        y = 0
    elif direction == 'SouthWest':
        x = -200
        y = -200
    elif direction == 'South':
        x = 0
        y = -200
    elif direction == 'SouthEast':
        x = 200
        y = -200
    else:
        x = None
        y = None
    return (x,y)

#place location of O

def drawO(direction):
    d = square_to_point(direction)
    if d != (None,None):        
        penup()
        setposition(square_to_point(direction))
        setheading(-90)
        forward(60)
        setheading(0)
        pendown()
        circle(60)
    else:
        pass

#place location of x

def drawX(direction):
    d = square_to_point(direction)
    if d != (None,None):     
        penup()
        setposition(square_to_point(direction))
        pendown()
        setheading(0)
        rt(45)
        fd(100)
        bk(200)
        fd(100)
        rt(90)
        fd(100)
        bk(200)
        fd(100)
    else:
        pass

def mouseclick(x,y):
    square = point_to_square(x,y)
    print ('X=',x,'Y=',y)
    location = point_to_square(x,y)
    check = game.look(location)
    who = game.current_player()
    if check != None:
        messagebox.showerror("Error", "This is an illigal move")
    
    else:
        if who == 'X':
            drawX(location)
            game.move(location)
        elif who == 'O':
            drawO(location)
            game.move(location)
        drawline()
            
def turnX():
   
    game.currentplayer = 'X'
    canvas.config(cursor = "X_cursor")
    title("Tic-Tac-Toe || Current Player X")

def turnO():    
    game.currentplayer = 'O'
    canvas.config(cursor = "circle")
    title("Tic-Tac-Toe || Current Player O")

def drawline():
    winner, place = game.check_status()
    
    if place == 'Win_NW_NE':
        pencolor('red')
        penup()
        goto(square_to_point('NorthWest'))
        down()
        goto(square_to_point('NorthEast'))
        Winner()

    if place == 'Win_NW_SW':
        pencolor('red')
        penup()
        goto(square_to_point('NorthWest'))
        down()
        goto(square_to_point('SouthWest'))
        Winner()     

    if place == 'Win_NW_SE':
        pencolor('red')
        penup()
        goto(square_to_point('NorthWest'))
        down()
        goto(square_to_point('SouthEast'))
        Winner()     

    if place == 'Win_N_S':
        pencolor('red')
        penup()
        goto(square_to_point('North'))
        down()
        goto(square_to_point('South'))
        Winner()   

    if place == 'Win_NE_SW':
        pencolor('red')
        penup()
        goto(square_to_point('NorthEast'))
        down()
        goto(square_to_point('SouthWest'))
        Winner()

    if place == 'Win_NE_SE':
        pencolor('red')
        penup()
        goto(square_to_point('NorthEast'))
        down()
        goto(square_to_point('SouthEast'))
        Winner()

    if place == 'Win_W_E':
        pencolor('red')
        penup()
        goto(square_to_point('East'))
        down()
        goto(square_to_point('West'))
        Winner()

    if place == 'Win_SW_SE':
        pencolor('red')
        penup()
        goto(square_to_point('SouthWest'))
        down()
        goto(square_to_point('SouthEast'))
        Winner()
        
    if place == 'Draw':
        messagebox.showinfo('No winner', 'Draw')


def Winner():
    messagebox.showinfo('winner'+'Wins', 'Congrats')
    keep_playing = messagebox.askyesno('Good Job','Do you want to keep playing')
    if keep_playing:
        clearscreen()
        game.initialize_board()
        draw()
        onscreenclick(mouseclick)
    else:
        bye()


onkeyrelease(turnX,'X')
onkeyrelease(turnO,'O')
listen()
onscreenclick(mouseclick)
mainloop()
