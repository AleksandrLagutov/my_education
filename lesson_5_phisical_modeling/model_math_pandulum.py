import graphics as gr
import math as m
# Global variable
SIZE_X = 1000
SIZE_Y = 1000
G = 0.003  # Gravitation
acceleration = G
centr_point = gr. Point(500, 500)  # Центр маятника
lenght = 50  # Длина маятника
beginner_angle = 0  # Угол отклонения
angle = beginner_angle  # вводимим переменную для текущего угла шара
beginner_velocity = gr.Point(2, 2)  # начальная  скорость
beginner_angle_velocity = m.degrees(m.atan((m.sqrt((beginner_velocity.x)**2
                                                   + (beginner_velocity.y)**2))/lenght))  #  начальная угловая   скорость
velocity = beginner_angle_velocity
beginner_bals_coords = gr.Point(centr_point.x + lenght*m.sin(m.radians(beginner_angle)),
                                centr_point.y + lenght*m.cos(m.radians(beginner_angle)))  # Вычесляем координату шара
print(beginner_angle_velocity)
# Creation window form and elements of math pendulum
window = gr.GraphWin("Math M", SIZE_X, SIZE_Y)
bals = gr.Circle(beginner_bals_coords, 10)
bals.setFill('red')
bals.draw(window)
cen = gr.Circle(centr_point, 5)
cen.setFill('green')
cen.draw(window)
# Функция принимает координаты шара и возвращает вектор перемещения в зависимости от угла


def apdate_coord(coords, this_angle):
    x_next = centr_point.x + lenght*m.sin(m.radians(this_angle))
    y_next = centr_point.y + lenght*m.cos(m.radians(this_angle))
    step = gr.Point(x_next - coords.x,
                    y_next - coords.y)
    return step


def update_angle(this_angle, this_velocity):
    this_angle += this_velocity
    # print('Угол',  m.atan((m.sqrt((this_velocity.x)**2 + (this_velocity.y)**2))/lenght))
    #  m.degrees(m.tan(beginner_velocity))
    #  print(m.degrees(m.atan((m.sqrt((beginner_velocity.x)**2 + (beginner_velocity.y)**2))/lenght)))
    return this_angle


def update_velocity(this_velocity, this_acceleration):
    if angle > 180:
        this_velocity = this_velocity*(-1)
    if angle < -180:
        this_velocity = this_velocity * (-1)
    if this_velocity > 0:
        this_velocity -=this_acceleration
    if this_velocity < 0:
        this_velocity += this_acceleration
    return this_velocity


def update_acceleration(this_acceleration):
    return this_acceleration
    pass


while True:
    print(velocity)
    acceleration = update_acceleration(G)
    velocity = update_velocity(velocity, acceleration)
    angle = update_angle(angle, velocity)
    moving = apdate_coord(bals.getCenter(), angle)
    bals.move(moving.x, moving.y)
    gr.time.sleep(0.02)