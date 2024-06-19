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
        # Check self collision
        for part in self.body[1:]:
            if head.equals(part):
                return True
        return False

    def display(self):
        for part in self.body:
            rect(part.x * scl, part.y * scl, scl, scl)

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

def setup():
    global cols, rows, snake, food
    size(400, 400)
    framerate(10)
    cols = floor(width/scl)
    rows = floor(height/scl)
    reset.game()

def draw():
    global Gamestate
    background(51)

    if gameState == "start":
        draw_start_screen()
    elif gameState == "play":
        if snake.check_collision():
            gameState = "end"
            return
        snake.update():
        if snake.body[0].equals(food.position):
            snake.grow.snake()
            food.pick.location()
        snake.display()
        fill(255, 0, 100)
        food.display()
    elif gameState == "end"
        draw_end_screen_()

