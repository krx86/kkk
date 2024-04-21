def on_button_pressed_a():
    robit.servo(robit.Servos.S1, 54)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
