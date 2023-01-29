from sshkeyboard import listen_keyboard
from picar import front_wheels
from picar import back_wheels

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

speed_step = 20
back_speed = 40
step_turn = 60
forward_speed = 60

def press(key):
    global step_turn
    global forward_speed

    if key == "up":
        bw.forward()
        bw.speed = forward_speed + speed_step
        x = bw.speed
        print(x)
    elif key == "down":
        bw.forward()
        bw.speed = forward_speed - speed_step
        x = bw.speed
        print(x)
    elif key == "left":
        step_turn = step_turn - 30
        y = step_turn
        print(y)
    elif key == "right":
        step_turn = step_turn + 30
        y = step_turn
        print(y)
    elif key == "w":
        bw.forward()
        bw.speed = forward_speed
        x = bw.speed
        print(x)
    elif key == "s":
        if bw.speed == 0:
            bw.backward()
            bw.speed = back_speed
        elif bw.speed >= 0:
            bw.stop()
        else:
            bw.backward()
            bw.speed = back_speed
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


