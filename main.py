from sshkeyboard import listen_keyboard
from picar import front_wheels
from picar import back_wheels

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

back_speed = 40
step_turn = 60
forward_speed = 60
direction = 0


def press(key):
    global step_turn
    global forward_speed
    global direction

    if key == "up":
        if direction == 1 and forward_speed < 100:
            forward_speed += 10
            bw.forward()
            bw.speed = forward_speed
    elif key == "down":
        print('hello')
    elif key == "left":
        step_turn = step_turn - 30
    elif key == "right":
        step_turn = step_turn + 30
    elif key == "w":
        if direction == 0:
            bw.forward()
            direction = 1
            bw.speed = forward_speed
        elif direction < 0:
            direction = 0
            bw.speed = 0
    elif key == "s":
        if direction == 0:
            bw.backward()
            direction = -1
            bw.speed = back_speed
        elif direction > 0:
            direction = 0
            bw.speed = 0
    elif key == "d":
        fw.turn(90 + step_turn)
    elif key == "a":
        fw.turn(90 - step_turn)
    elif key == "r":
        bw.stop()
        fw.turn(90)


def release(key):
    if key == "a" or key == "d":
        fw.turn_straight()


listen_keyboard(
    on_press=press,
    on_release=release
    )


def stop():
    bw.stop()
    fw.turn_straight()


