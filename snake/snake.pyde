1#Wiczka
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
        fill(0, 255, 0)  # Paulina
        for part in self.body:
            rect(part.x * scl, part.y * scl, scl, scl)
# Paulina
    def increase_speed(self): 
        self.speed += 5 

#Iza
class Food:
    def __init__(self):
        self.position = PVector(floor(random(cols)), floor(random(rows)))
    
    def pick_location(self):
        self.position = PVector(floor(random(cols)), floor(random(rows)))

    def display(self):
        fill(255, 0, 100)  # Paulina
        rect(self.position.x * scl, self.position.y * scl, scl, scl)

scl = 20
cols = 0
rows = 0
snake = None
food = None
gameState = "start"
score = 0
current_difficulty = 2  # Paulina

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
            if score % 10 == 0 and score > 0: # Paulina
                snake.increase_speed() # Paulina
                frameRate(snake.speed) # Paulina
        snake.display()
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
    text("Score: " + str(score), 10, 30)

#Bibi
def draw_start_screen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(32)
    text("Snake Game", width / 2, height / 2 - 20)
    textSize(24)
    text("Press 1 for Easy (slower)", width / 2, height / 2 + 20) # Paulina 
    text("Press 2 for Hard (faster)", width / 2, height / 2 + 40) # Paulina

def draw_end_screen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(32)
    text("Game Over", width / 2, height / 2 - 40)
    textSize(24)
    text("Score: " + str(score), width / 2, height / 2 - 20)
    text("Press ENTER to retry", width / 2, height / 2) # Paulina
    text("Press ESC to quit", width / 2, height / 2 + 25) # Paulina

# Ola, Sandra, zmienione przez # Paulina
def keyPressed(): 
    global gameState, current_difficulty 
    
    if gameState == "start":
        if key == '1':
            current_difficulty = 1 
            start_game()
        elif key == '2':
            current_difficulty = 2  
            start_game()

    elif gameState == "end":
        if key == ENTER:
            reset_game()
            start_game()
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
    global snake, food, score, current_difficulty
    gameState = "start"
    snake = Snake()
    food = Food()
    score = 0
    if current_difficulty == 1: # tylko na reset a za pierwszym odpaleniem nie bierze pod uwagę
        snake.speed = 5  
    elif current_difficulty == 2:
        snake.speed = 10  
    frameRate(snake.speed)

def start_game():
    global gameState
    gameState = "play"
    frameRate(snake.speed) 
