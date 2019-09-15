import pygame as py
import random as ran
import sys

main_menu_image_path = "./image/"

class Point:
    '''
    The class stores the postion of the head so that it won't be changed out side the class.
    '''
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


def gen_food(row,col,head,snakes):
    '''
    The function generates the position of the food. It makes sure
    the food will not collide with the snake.
    '''
    while True:
        pos = Point(ran.randrange(2,row-2),ran.randrange(2,col-2))
        # Make sure you will not collide with the head.
        collide = False
        if head.row == pos.row and head.col == pos.col:
            collide = True
        # Make sure you will not collide with the body.
        for item in snakes:
            if item.row == pos.row and item.col == pos.col:
                collide = True
        # If not collide, the position is valid.
        if not collide:
            break
    return pos


def rect(point,color,row,col,window,W,H):
    '''
    This function draws the body,the snake's head and the food.
    '''
    each_width = W/col
    each_height = H/row
    left = point.col*(W/col)
    top = point.row*(H/row)
    # The process of drawing
    py.draw.rect(window,color,(left,top,each_width,each_height))



def main(fff):
    '''
    This is the main body of the game. The parameter 'fff' represents the
    frame rate(difficulty) of the game.
    '''
    # Global the score so that it can be used in menu.py
    global score
    py.init()
    W = 1280
    H = 720
    row = int(H / 20)
    col = int(W / 20)
    size = (W, H)
    window = py.display.set_mode(size)
    py.display.set_caption("Snake Game!")
    # define the coordinates of initial head position
    head = Point(int(row / 2), int(col / 2))
    head_color = (0, 255, 0)
    # The 'Snake' list represents the position of the snake's body.
    snakes = [Point(row=head.row, col=head.col + 1),
              Point(row=head.row, col=head.col + 2),
              Point(row=head.row, col=head.col + 3)]
    # Here it generates the position of the first food.
    food = gen_food(row,col,head,snakes)
    choice = [(225, 200, 1), (255, 20, 147), (128, 128, 255), (255, 69, 0)]
    food_color = choice[ran.randrange(0, 3)]
    # The initial direction of the snake is left.
    direction = 'left'

    # game loop
    keepgoing = True
    frame_rate = py.time.Clock()
    score = 0
    while keepgoing:
        # Here we insert the background image.
        background = py.image.load(main_menu_image_path + 'forest.jpg').convert()
        window.blit(background, (0, 0))
        for event in py.event.get():
            # Defines the situation that the game quits.
            if event.type == py.QUIT:
                keepgoing = False
                py.quit()
                sys.exit()
            # Defines how the snake moves.
            elif event.type == py.KEYDOWN:
                if event.key == 273 or event.key == 119:
                    if direction != 'down':
                        direction = 'up'
                elif event.key == 274 or event.key == 115:
                    if direction != 'up':
                        direction = 'down'
                elif event.key == 276 or event.key == 97:
                    if direction != 'right':
                        direction = 'left'
                elif event.key == 275 or event.key == 100:
                    if direction != 'left':
                        direction = 'right'

        # Inserts the head to the body list
        snakes.insert(0, head.copy())
        # Defines when the food is considered eaten by the snake.
        if not (head.row == food.row and head.col == food.col):
            snakes.pop()
        else:
            score += 1
            # Generate new food in here.
            food = gen_food(row,col,head,snakes)
            choice = [(225, 200, 1), (255, 20, 147), (128, 128, 255), (255, 69, 0)]
            food_color = choice[ran.randrange(0, 3)]

        # Draw the food and snake's body.
        rect(food, food_color,row,col,window,W,H)
        for item in snakes:
            rect(item, (220, 20, 60),row,col,window,W,H)
        # Define each direction
        if direction == 'left':
            head.col -= 1
        elif direction == 'right':
            head.col += 1
        elif direction == 'up':
            head.row -= 1
        elif direction == 'down':
            head.row += 1

        # Draw head
        rect(head, head_color,row,col,window,W,H)

        # Define the situation for the snake to be dead.
        dead = False
        # Hit the wall
        if head.col < 0 or head.row < 0 or head.col >= col or head.row >= row:
            dead = True
        # Hit itself
        for item in snakes:
            if head.col == item.col and head.row == item.row:
                dead = True
        if dead:
            # If dead, the game quits.
            keepgoing = False

        py.display.update()
        frame_rate.tick(fff)
    


