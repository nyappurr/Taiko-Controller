import board
import analogio
import usb_hid
import time

keyboard = usb_hid.devices[0]

# HID keycodes | change keys
KEY_W = 0x1A
KEY_A = 0x04
KEY_S = 0x16
KEY_D = 0x07

# Modifier byte (none for plain letters)
MOD_NONE = 0x00

# Pin map + HID key characters + thresholds | change pin, keys, and threshold sensitivity here
drum_map = {
    "L_RIM":     {"PIN": board.A1, "KEY": KEY_W, "CHAR": "w", "THRESHOLD": 15000},
    "L_SURFACE": {"PIN": board.A2, "KEY": KEY_A, "CHAR": "a", "THRESHOLD": 14000},
    "R_SURFACE": {"PIN": board.A3, "KEY": KEY_S, "CHAR": "s", "THRESHOLD": 16000},
    "R_RIM":     {"PIN": board.A4, "KEY": KEY_D, "CHAR": "d", "THRESHOLD": 15500},
}

inputs = {}
for name, cfg in drum_map.items():
    inputs[name] = analogio.AnalogIn(cfg["PIN"])

def send_keypress(key):
    report = bytearray([MOD_NONE, 0, key, 0, 0, 0, 0, 0])
    keyboard.send_report(report)
    keyboard.send_report(bytearray(8))  

last_hit = {name: 0 for name in drum_map}
# Minimum time between hits on pad (ms)
debounce_ms = 80

while True:
    now = time.monotonic() * 1000
    for name, pin in inputs.items():
        val = pin.value 
        if val > drum_map[name]["THRESHOLD"] and (now - last_hit[name]) > debounce_ms:
            send_keypress(drum_map[name]["KEY"])
            
            print(f"{name} {drum_map[name]['CHAR']} {drum_map[name]['THRESHOLD']}")
            
            last_hit[name] = now
    time.sleep(0.05)
