
import time
import displayio
import terminalio
from rainbowio import colorwheel
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_macropad import MacroPad

macropad = MacroPad()
last_position = 0

lit_keys = [False] * 12
wheel_offset = 257



def password_entry(top, password):
    new_text = macropad.display_text(title="   {}   ".format(top))
    macropad.pixels[key_event.key_number] = (255, 0, 0)
    macropad.keyboard_layout.write(password)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    new_text[1].text = " Entering Password...  "
    new_text.show()
    time.sleep(1)
    new_text[2].text = "      Successful!     "
    new_text.show()
    return


macropad.encoder_switch_debounced.update()
current_position = macropad.encoder

#Turn off leds
if macropad.encoder_switch_debounced.pressed:
        #macropad.pixels = (0,0,0)
        all_keys = (x for x in range(12))
        for x in all_keys:
            print(x)

# new_text = macropad.display_text(title="      OUTLOOK    ")
while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            lit_keys[key_event.key_number] = not lit_keys[key_event.key_number]

            if key_event.key_number is 0:
                top_text = "OUTLOOK"
                pw = "Password01"
                password_entry(top_text, pw)
            if key_event.key_number is 1:
                top_text = "Microsoft"
                pw = "Password01"
                password_entry(top_text, pw)
            if key_event.key_number is 2:
                top_text = "Google"
                pw = "Password02"
                password_entry(top_text, pw)
            if key_event.key_number is 3:
                top_text = "FaceBook"
                pw = "Password03"
                password_entry(top_text, pw)
            if key_event.key_number is 4:
                top_text = "CoretechsDirect"
                pw = "Password04"
                password_entry(top_text, pw)
            if key_event.key_number is 5:
                top_text = "Buildium"
                pw = "Password05"
                password_entry(top_text, pw)
            if key_event.key_number is 6:
                top_text = "Monster"
                pw = "Password06"
                password_entry(top_text, pw)
            if key_event.key_number is 7:
                top_text = "Empty"
                pw = "Password07"
                password_entry(top_text, pw)
            if key_event.key_number is 8:
                top_text = "Empty"
                pw = "Password08"
                password_entry(top_text, pw)
            if key_event.key_number is 9:
                top_text = "Empty"
                pw = "Password09"
                password_entry(top_text, pw)
            if key_event.key_number is 10:
                top_text = "Empty"
                pw = "Password10"
                password_entry(top_text, pw)
            if key_event.key_number is 11:
                top_text = "Empty"
                pw = "Password11"
                password_entry(top_text, pw)
                time.sleep(0.05)
                macropad.pixels[11] =(10,255,100)

            else:

                macropad.pixels[key_event.key_number] = (10, 255, 100)
        macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:

        all_keys = (x for x in range(12))
        for x in all_keys:
            macropad.pixels[x]= (0,0,0)

    if macropad.encoder < last_position:
        macropad.encoder_switch_debounced.update()
        current_position = macropad.encoder
        macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_DECREMENT
                )
        last_position = current_position

    if macropad.encoder > last_position:
        macropad.encoder_switch_debounced.update()
        current_position = macropad.encoder
        macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_INCREMENT
                )
        last_position = current_position

