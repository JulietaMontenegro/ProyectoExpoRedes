#include <Arduino.h>
#include "FastLED.h"

#if FASTLED_VERSION < 3001000
#error "Requires FastLED 3.1 or later; check github for latest code."
#endif

#define DATA_PIN    27
//#define CLK_PIN   4
#define LED_TYPE    WS2812
#define COLOR_ORDER GRB
#define NUM_LEDS    60
#define BRIGHTNESS  255

CRGB leds[NUM_LEDS];


void setup() {
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS)
    .setCorrection(TypicalLEDStrip)
    .setDither(BRIGHTNESS < 255);

  fill_solid(leds, NUM_LEDS, CRGB:: Black);
  FastLED.show();
  delay(3000);
}

void blaco(){
    for(int indice=0; indice< NUM_LEDS; indice++){
    leds[indice]=CRGB:: White;
  }
  delay(15);
  FastLED.show(); 
}
void apagado(){
  delay(15);
    for(int indice=0; indice< NUM_LEDS; indice++){
    leds[indice]=CRGB:: Black;
  }
  delay(15);
  FastLED.show(); 
}
void rojo(){
    for(int indice=0; indice< NUM_LEDS; indice++){
    leds[indice]=CRGB:: Red;
  }
  delay(1000);
  FastLED.show(); 
}
void azul(){
    for(int indice=0; indice< NUM_LEDS; indice++){
    leds[indice]=CRGB:: Blue;
  }
  delay(1000);
  FastLED.show(); 
}

void relampago(){
  delay(1500);
  apagado();  
  blaco();
  apagado();
  blaco();
  apagado();
}



void loop()
{
  for(int i=0; i<3; i++){
      rojo();
      azul();
  }
  relampago();

}


