# Taiko-Controller
Create a Taiko Drum Controller to be played on PC for [OpenTaiko](https://opentaiko.wiki.gg/) and [Taiko no Tatsujin: Rythym Festival](https://store.steampowered.com/app/2288630/Taiko_no_Tatsujin_Rhythm_Festival/). Bare bone project, beginner friendly!


Planned
- Controller Support
- Switch Support
- Bluetooth Support
- 44cm Arcade Size Templates


# ❯❯❯❯ Start Here ❮❮❮❮
Look over this page and choose your microcontroller. Instructions, circuit diagrams and helpful links will be in MCU Guides under its relevant microcontroller name. 

For physical construction of the Taiko Drum Pads, they can be found on my Instructables **here** (WIP)

# Microcontroller

Any microcontroller will work fine as long as it has...
- miniumum 4 analog pins
- USB HID support

You can get a board that doesn't have 4 analog pins and attach an ADC module(ADS1115) to it. I haven't tested that out but an  ADS1115 + Raspberry Pi Pico should theoretically work. There are so many boards you can get for this project that I wouldn't be able to include them all here. Regardless, I've listed a few affordable ones just so you can have an idea of what to get.

The wiring for the Taiko should be similar across the same chips. So wiring the Seeed Studio XIAO RP2040 should be the same as the Adafruit QT Py RP2040. Granted there are a few outliers in board construction :)


## Recommended boards around $10
### Atmega32U4
- [Adafruit ItsyBitsy 32u4 5V](https://www.adafruit.com/product/3677)
- [KEYESTUDIO Leonardo R3](https://a.co/d/aMHsjTD)

### RP2040
- [SparkFun Pro Micro RP2040](https://www.sparkfun.com/sparkfun-pro-micro-rp2040.html)
- [Adafruit QT Py RP2040](https://www.adafruit.com/product/4900)
- [Seeed Studio XIAO RP2040](https://a.co/d/2wXBoZE)

### SAMD21
- [Seeed Studio XIAO SAMD21(Seeeduino XIAO)](https://www.seeedstudio.com/Seeeduino-XIAO-Arduino-Microcontroller-SAMD21-Cortex-M0+-p-4426.html)
- [Adafruit QT Py SAMD21](https://www.adafruit.com/product/4600)

### ESP32
- [waveshare ESP32-S3 Mini Development Board](https://www.waveshare.com/product/mcu-tools/development-boards/esp32/esp32-s3-zero.htm?sku=25517)
- [HiLetgo ESP-WROOM-32 ESP32 Development Board](https://a.co/d/cvBCRye)

# Customizing
Here are some things you can edit to your personal needs.

### Pin Mapping
All default pins are set to A0, A1, A2, A3 

    L_Rim A0
    L_Surface A1
    R_Surface A2
    R_Rim A3

Just change the pins based on your wiring. 

### HID Key Characters
The default key characters is set to w, a, s, d

    L_Rim 'w'
    L_Surface 'a'
    R_Surface 's'
    R_Rim 'd'

 You can change the key's to whatever characters you want in **Arduino C++** [**code.ino**](https://github.com/nyappurr/Taiko-Controller/blob/d1ce79c2ca52bc04288bb2e107308d22ba68b459/codes/code.ino).

For **CircuitPython** [**code.py**](https://github.com/nyappurr/Taiko-Controller/blob/d026a6ac500cebf908fd98388d6a15320e91dff7/codes/code.py) use MightyPork's [usb_hid_keys.h](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2) as a guide.

### Threshold

Treshold measures the sensitivity of a hit. Higher threshold means less sensitive to hits, lower threshold means more sensitive to hits.

### Debounce

Marks the minimum time between hits and defaults to milliseconds. Helps if you are getting false triggers.

# Circuit Diagrams

Included in the folder of each MCU will be the circuit diagrams. BB and schematics diagram will possibly be added in the future

# Templates
For more savy users, I've included SVG's. You can decide how to use the template yourself. PNG's are also included. Simply print them out at 100% and then mirror to get the other side of the template.

# Acknowledgements
[ShikyC](https://github.com/ShikyC/Taiko-Drum-Controller-Arduino) - Much of the wiring is based on a schematic from his repo. They also have an extremely useful Signal Visualizer Tool that couls help you with debugging and for finding the sensitivity that best fits your needs. 

[MightyPork](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2) 
List of relevant HID keys crucial if you don't want to use the default key characters.

[kasashiki3](https://github.com/kasasiki3/HIDtaiko) Kasashiki provides 3D files and a video guide. They also have wiring instructions not used here but are nonetheless helpful if you decide to use their version.

Thank you to all of you. ദ്ദി/ᐠ｡‸｡ᐟ\

## Remarks
I wanted to create a Taiko Drum Controller because I really like Taiko no Tatsujin Arcade but I'm really not very good at it and didn't want to go frequent Round 1 to play on the Taiko drums. Currently, this version only works with PC as I don't have the braincells to test controller support. I will implement that sometime soon though. I designed the guide to be plug & play...but I wanted it to still be easily customizable for people of all skill levels. I documented as much as a could with whatever I thought would be relevsant but in a way that isn't too overwhelming. Anyways, this is my first GitHub repo and I'm just learning how commits and everything works. The formatting may be strange but I did the best I could.

Thanks for reading ~

/ᐠ˵- ᴗ -˵マ ᶻ 𝗓 Z