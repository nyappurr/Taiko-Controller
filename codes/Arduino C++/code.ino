#include <Keyboard.h>

// Pin Map | Change based on your own pinout
const int L_Rim     = A0;
const int L_Surface = A1;
const int R_Surface = A2;
const int R_Rim     = A3;

// HID keys | Insert your own keys characters
const char KEY_L_RIM     = 'w';
const char KEY_L_SURFACE = 'a';
const char KEY_R_SURFACE = 's';
const char KEY_R_RIM     = 'd';

// Thresholds/sensitivity | Higher less sensitive - Lower more sensitive
int threshold_L_Rim     = 50;
int threshold_L_Surface = 50;
int threshold_R_Surface = 50;
int threshold_R_Rim     = 50;

// Minimum time between hits on pad (ms)
unsigned long debounce_ms = 80;

unsigned long last_hit[4] = {0,0,0,0};

void setup() {
  Keyboard.begin();
}

void loop() {
  unsigned long now = millis();

  checkPad(L_Rim,     threshold_L_Rim,     KEY_L_RIM,     0, now);
  checkPad(L_Surface, threshold_L_Surface, KEY_L_SURFACE, 1, now);
  checkPad(R_Surface, threshold_R_Surface, KEY_R_SURFACE, 2, now);
  checkPad(R_Rim,     threshold_R_Rim,     KEY_R_RIM,     3, now);
}

void checkPad(int pin, int threshold, char key, int index, unsigned long now) {
  int val = analogRead(pin);

  if (val > threshold && (now - last_hit[index]) > debounce_ms) {
    Keyboard.press(key);
    delay(10);
    Keyboard.releaseAll();

    last_hit[index] = now;
  }
}
