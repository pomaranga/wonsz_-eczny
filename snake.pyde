#Wiczka
class Snake:
    def __init__(self):
        self.body = [PVector(0, 0)]
        self.dir = PVector(1, 0)
        self.grow = False
        
    def update(self):
        head = self.body[0].copy()
        head.add(self.dir)
        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        self.grow = False

    def change_dir(self, x, y):
        new_dir = PVector(x, y)
        if len(self.body) > 1 and new_dir.equals(self.body[0] - self.body[1]):
            return
        self.dir = new_dir

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        head = self.body[0]
        if head.x < 0 or head.x >= cols or head.y < 0 or head.y >= rows:
            return True
        for part in self.body[1:]:
            if head.equals(part):
                return True
        return False

    def display(self):
        for part in self.body:
            rect(part.x * scl, part.y * scl, scl, scl)

#Iza
class Food:
    def __init__(self):
        self.position = PVector(floor(random(cols)), floor(random(rows)))
    
    def pick_location(self):
        self.position = PVector(floor(random(cols)), floor(random(rows)))

    def display(self):
        rect(self.position.x * scl, self.position.y * scl, scl, scl)

scl = 20
cols = 0
rows = 0
snake = None
food = None
gameState = "start"
score = 0

#Karo
def setup():
    global cols, rows, snake, food
    size(400, 400)
    frameRate(10)
    cols = floor(width / scl)
    rows = floor(height / scl)
    reset_game()

def draw():
    global gameState
    background(51)
    
    if gameState == "start":
        draw_start_screen()
    elif gameState == "play":
        if snake.check_collision():
            gameState = "end"
            return
        snake.update()
        if snake.body[0].equals(food.position):
            snake.grow_snake()
            food.pick_location()
            update_score()
        snake.display()
        fill(255, 0, 100)
        food.display()
        display_score()
    elif gameState == "end":
        draw_end_screen()

def update_score():
    global score
    score += 1

def display_score():
    fill(255)
    textSize(16)
    textAlign(LEFT)
    text("Score: " + str(score), 10, 20)

#Bibi
def draw_start_screen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(32)
    text("Snake Game", width / 2, height / 2 - 20)
    textSize(24)
    text("ENTER to start", width / 2, height / 2 + 20)
    textSize(16)
    text("ARROWS to control Snake", width / 2, height / 2 + 40)

def draw_end_screen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(32)
    text("Game Over", width / 2, height / 2 - 40)
    textSize(24)
    text("Score: " + str(score), width / 2, height / 2 - 10)
    text("ENTER to retry", width / 2, height / 2)
    text("ESC to quit", width / 2, height / 2 + 25)

#Ola, Sandra
def keyReleased():
    global gameState
    
    if gameState == "start" and key == ENTER:
        gameState = "play"
    elif gameState == "end":
        if key == ENTER:
            reset_game()
            gameState = "play"
        elif key == ESC:
            exit()
    elif gameState == "play":
        if keyCode == UP and snake.dir.y == 0:
            snake.change_dir(0, -1)
        elif keyCode == DOWN and snake.dir.y == 0:
            snake.change_dir(0, 1)
        elif keyCode == RIGHT and snake.dir.x == 0:
            snake.change_dir(1, 0)
        elif keyCode == LEFT and snake.dir.x == 0:
            snake.change_dir(-1, 0)

def reset_game():
    global snake, food, score
    snake = Snake()
    food = Food()
    food.pick_location()
    score = 0
