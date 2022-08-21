from turtle import Turtle

START_POSITION = (0, 0)
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = None

    def create_snake(self):
        for i in range(3):
            self.add_segment((START_POSITION[0] - 20 * i, START_POSITION[1]))

    def move(self):
        # follow the head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = None
