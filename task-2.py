import turtle
import argparse

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    parser = argparse.ArgumentParser(description="Draw a Koch snowflake fractal.")
    parser.add_argument("level", type=int, help="Level of recursion for the Koch snowflake.")
    args = parser.parse_args()
    
    level = args.level

    screen = turtle.Screen()
    screen.title("Koch Snowflake Fractal")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    length = 300  # Length of one side of the snowflake
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    draw_koch_snowflake(t, length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
