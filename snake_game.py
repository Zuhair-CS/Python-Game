from tkinter import *
import random
from playsound import playsound
#constants for game setting
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "red"
BG_COLOR = "black"
#basic classes and function defining
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill= SNAKE_COLOR, tag = "snake")
            self.squares.append([square])
class Food:
    def __init__(self):
        self.x = random.randint(0, (int(GAME_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE
        self.y = random.randint(0, (int(GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE
        self.coordinates = [self.x, self.y]
        canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
def nextTurn(snake, food):
    global score
    x, y = snake.coordinates[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if checkCollisions(snake):
        gameOver()
    else:
        root.after(SPEED, nextTurn, snake, food)

def changeDirection(new_direction):
    global direction #accessing the global set direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def checkCollisions(snake):
    x,y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for i in snake.coordinates[1:]:
        if x == i[0] and y == i[1]:
            return True
    return False
def gameOver():
    playsound('Tatatata.mp3')
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ("Ariel Black",80),text = "GAME OVER",fill = "red")
#game code
root = Tk()
root.title("Snake Game")
root.resizable(False,False)
score = 0
direction = 'down'
label = Label(root, text = "Score: {}".format(score),font = ("Arial Black",40))
label.pack()
canvas = Canvas(root, bg = BG_COLOR, height= GAME_HEIGHT, width= GAME_WIDTH)
canvas.pack()
root.bind('<Left>', lambda event: changeDirection('left'))
root.bind('<Right>', lambda event: changeDirection('right'))
root.bind('<Up>', lambda event: changeDirection('up'))
root.bind('<Down>', lambda event: changeDirection('down'))
snake = Snake()
food = Food()
nextTurn(snake,food)
root.mainloop()