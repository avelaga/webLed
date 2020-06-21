#include <FastLED.h>
#include <Wire.h>

#define NUM_LEDS 5
#define PIN 3

CRGB leds[NUM_LEDS];

int input = 0;
int hue = 150;
int brightness = 0;

void clearLeds() {
  for (int x = 0; x < NUM_LEDS; x++) {
    leds[x] = CHSV(0, 0, 0);
  }
  FastLED.show();
}

void animate() {
  hue = 150;
  brightness = 0;

  // increment hue and brightness for 25 shades
  for (int a = 0; a < 25; a++) {

    for (int b = 0; b < NUM_LEDS; b++) {
      leds[b] = CHSV(hue, 255, brightness);
    }

    delay(25);
    FastLED.show();
    hue -= 2;
    brightness += 10;
  }

  // hold color and brightness
  delay(300);

  // decrement hue for 25 shades
  for (int c = 0; c < 25; c++) {

    for (int d = 0; d < NUM_LEDS; d++) {
      leds[d] = CHSV(hue, 255, brightness);
    }

    delay(25);
    FastLED.show();
    hue += 2;
    brightness -= 10;
  }

  clearLeds();
}

void receiveEvent(int howMany) {
  input = Wire.read(); // receive byte as a character
  animate();
}

void setup() {
  Wire.begin(0x8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent);
  LEDS.addLeds<WS2812, PIN, RGB>(leds, NUM_LEDS);
  LEDS.setBrightness(255);
  clearLeds();
}

void loop() {
}

