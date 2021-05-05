import graphics as gr

#Global variable

SIZE_X = 1000
SIZE_Y = 1000


def draw_cirle(name_circle, coords_centr, size, color):
    name_circle = gr.Circle(coords_centr, size)
    name_circle.setFill(color)
    name_circle.draw(window)
    return name_circle

# Function move ball and return new coords
def move_ball(moving_balls,speed_moving):
    d_x = speed_moving.x
    d_y = speed_moving.y
    moving_balls.move(d_x, d_y)
# Функция проверки координат и изменения направления 
def check_coords(coords,velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x
    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y
    return velocity
# Функция изменения скорости
def update_velocity(speed, acceleration):
    speed.x += acceleration.x
    speed.y += acceleration.y
    return speed

def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point

def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 800

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

    


    


# Creation window form
window = gr.GraphWin("Sular system", SIZE_X, SIZE_Y)

#main
acceleration = gr.Point(0, 0)
velocity = gr.Point(1.6, 0)
ball_coords = gr.Point(500, 300)

sun = draw_cirle('sun', gr.Point(500, 500), 30, 'yellow')
ball_1 = draw_cirle('ball_1', ball_coords , 20, 'red')


while  True:
    move_ball(ball_1, velocity)
    acceleration = update_acceleration(ball_1.getCenter(), gr.Point(500, 500))

    update_velocity(velocity, acceleration)
    check_coords(ball_1.getCenter(), velocity)
    gr.time.sleep(0.02)
   

window.getMouse()
window.close()

