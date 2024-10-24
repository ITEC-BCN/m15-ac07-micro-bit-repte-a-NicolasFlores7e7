mano = 0

def on_button_pressed_a():
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global mano
    mano = randint(0, 2)
    if mano == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif mano == 1:
        basic.show_icon(IconNames.SQUARE)
    elif mano == 2:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)
