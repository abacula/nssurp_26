
/// @file    NSpikeShoe.ino
/// @brief   Get data from an accelerometer and make a chain of LEDs on the shoe respond


#include <FastLED.h>

#define DATA_PIN 2


// How many leds in your strip?
#define NUM_LEDS 30



//Global timers for keeping track of loop things
unsigned long g_timer_0 = 0;

float duration, distance;
int wait = 100;
int color_base = 0;
int color;
int sat;
int bright;
int spin_base = 0;


// Cycle for LED blinking
#define CYCLE_TIME 100


// Define the array of leds
CRGB leds[NUM_LEDS];


void setup() { 
 
  Serial.begin(115200);
  Serial.println("Starting up...");

  // Set up LEDs
  FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);

  // Set LEDs to white on start
  for(int i = 0; i < NUM_LEDS; i = i + 1) {

        color = 0;
        sat = 255;
        bright = 0;
        wait = 50; // in milliseconds
        leds[i] = CHSV(color, sat, bright);
        delay(wait);
       
      }
      FastLED.show();
      delay(wait);
 
}



void loop() { 

  // Write LEDs
  color_base = 0;

  //instant(192); // Needs a color int
  //rainbow(); // Doesn't need variables
  facing(NUM_LEDS, 1, 160, 0); // Needs a place to change color at, distance to change color around, default color, and secondary color

//  Terminal output
//    Serial.print("LED loop: ");
//    Serial.println(color);
//    Serial.println(color);
//    Serial.println(wait);
    FastLED.show();
    wait = 10;
    delay(wait);
}

// Instant color change
void instant(int instantColor)
{
  color = instantColor;
  sat = 255;
  bright = 255;
  wait = 10;
  
  for(int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CHSV(color, sat, bright);
    delay(wait);
  }
  FastLED.show();
}

// Rainbow of color around the strip, conforms to strip length
void rainbow() {
  
  for(int i = 0; i < NUM_LEDS; i = i + 1) {
   color = round(((float)i)/NUM_LEDS * 255);
   sat = 255;
   bright = 255;
   wait = 10; // in milliseconds
   
   bright = 255;
   leds[i] = CHSV(color, sat, bright);
   FastLED.show();
   delay(wait);
   
  }
}

// Changes color around 'place' in the array
void facing(int place, int distance, int defaultColor, int faceColor) {
  for(int i = 0; i < NUM_LEDS; i++)
  {
    sat = 255;
    bright = 255;
    wait = 10;
    
    if (abs(place-i) <= distance)
      color = faceColor;
    else
      color = defaultColor;

    leds[i] = CHSV(color, sat, bright);
    FastLED.show();
    delay(wait);
  }
  //FastLED.show();
}

// Spins an area of 'size' leds of 'spinColor' along the background of'baseColor'
void spin(int size, int spinColor, int baseColor)
{
  sat = 255;
  bright = 255;
  wait = 10;

  // for ~~~

}
