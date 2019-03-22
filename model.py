import arcade.key

DIR_STILL = 0
DIR_RIGHT = 1
DIR_LEFT = 2

MOVE_SPEED = 5

DIR_OFFSETS = { DIR_STILL: (0,0),
                DIR_RIGHT: (1,0),
                DIR_LEFT: (-1,0),}
class Snake:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_STILL

    def move(self, direction):
        self.x += MOVE_SPEED*DIR_OFFSETS[direction][0]
        self.y += MOVE_SPEED*DIR_OFFSETS[direction][1]

    def update(self, delta):
        self.move(self.direction)


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.snake = Snake(self, width // 2, height // 2)

    def update(self, delta):
        self.snake.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.snake.direction = DIR_LEFT
        if key == arcade.key.RIGHT:
            self.snake.direction = DIR_RIGHT