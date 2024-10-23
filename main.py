import turtle

# bạn có thể thay đổi tỉ lệ lá cờ bằng cách thay đổi số hạng nhân với flag_height và flag_width
# Kích thước cờ tỉ lệ 2:3
flag_width = 300 * 2
flag_height = 200 * 2

screen = turtle.Screen()
screen.title("Việt Nam - Bảo Minh")
screen.setup(width=flag_height / 2 * 4, height=flag_height / 2 * 3)
screen.bgcolor("white")

flag = turtle.Turtle()
flag.speed(6)  # tốc độ vẽ


# Vẽ hình chữ nhật màu đỏ
def draw_rectangle(width, height):
    flag.penup()
    flag.goto(-width / 2, height / 2)  # Bắt đầu vẽ từ góc trên bên trái
    flag.pendown()
    flag.color("#da251d")
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()


# Vẽ ngôi sao vàng
def draw_star(size, x, y):
    flag.penup()
    flag.goto(x, y)  # bắt đầu vẽ ở đỉnh bên trái
    flag.setheading(0)
    flag.pendown()
    flag.color("#ffff00")
    flag.begin_fill()
    for _ in range(5):
        flag.forward(size)
        flag.right(72)
        flag.forward(size)
        flag.right(144)
    flag.end_fill()


# Vẽ cờ đỏ hình chữ nhật
draw_rectangle(flag_width, flag_height)

flag.speed(10)  # tốc độ vẽ

# Vẽ ngôi sao vàng ở giữa lá cờ
star_size = (2.37 / 10) * flag_width
draw_star(star_size, -0.5706 * flag_height / 2, 0.1854 * flag_height / 2)

flag.hideturtle()
turtle.done()
