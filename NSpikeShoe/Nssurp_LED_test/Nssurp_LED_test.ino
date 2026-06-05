/// @file    NSpikeShoe.ino
/// @brief   Get data from an accelerometer and make a chain of LEDs on the shoe respond

// GLOBAL VARIABLES
uint8_t gHue = 10;

#include <FastLED.h>

#define DATA_PIN 2


// How many leds in your strip?
#define NUM_LEDS 32



//Global timers for keeping track of loop things
unsigned long g_timer_0 = 0;

float duration, distance;
int wait = 100;
int flag;
int color;
int sat;
int bright;
int bright2;
float prev_dist;
int pot = 30;
// Cycle for LED blinking
#define CYCLE_TIME 100


// Define the array of leds
CRGB leds[NUM_LEDS];


void setup() { 
 
  Serial.begin(115200);
  Serial.println("Starting up...");

  // Set up LEDs
  FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
 
}



void loop() { 


  // Write LEDs
 
    uint8_t hue = gHue;

  for(int whiteLed = 0; whiteLed < NUM_LEDS; whiteLed = whiteLed + 1) {
    
        sat = 255;
        bright = 150;
        wait = 900; // in milliseconds
        
        if (true) {
          color = 96;
          leds[whiteLed] = CHSV(color, sat, bright);
        }
        else {
          color = 160;
          leds[whiteLed] = CHSV(color, sat, bright);
        }
        Serial.print("LED loop: ");
//      Serial.println(color);
       
      }


//      Serial.println(color);
//      Serial.println(wait);
      FastLED.show();
      delay(wait);
      


}
