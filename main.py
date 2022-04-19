def on_sound_loud():
    led.plot_bar_graph(1, 5)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_logo_touched():
    basic.show_icon(IconNames.SQUARE)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_ab():
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
        MelodyOptions.FOREVER)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_number(input.light_level())
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

input.set_sound_threshold(SoundThreshold.LOUD, 128)

def on_forever():
    pass
basic.forever(on_forever)
