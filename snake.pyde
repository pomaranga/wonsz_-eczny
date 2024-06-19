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
