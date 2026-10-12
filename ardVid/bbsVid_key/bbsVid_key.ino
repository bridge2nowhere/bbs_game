#include <TVout.h>
#include <fontALL.h>
#include "TVOlogo.h"
#include "glyph.h"
#include <pollserial.h>
#include "MatrixKeypad.h"
#include <stdint.h>

const uint8_t rown = 4; //4 rows
const uint8_t coln = 3; //3 columns
uint8_t rowPins[rown] = {A0, A1, A2, A3}; //frist row is connect to pin 10, second to 9...
uint8_t colPins[coln] = {6, 5, 4}; //frist column is connect to pin 6, second to 5...
char keymap[rown][coln] = 
  {{'1','2','3'}, //key of the frist row frist column is '1', frist row second column column is '2'
   {'4','5','6'}, //key of the second row frist column is '4', second row second column column is '5'
   {'7','8','9'},
   {'*','0','#'}};
MatrixKeypad_t *keypad; //keypad is the variable that you will need to pass to the other functions

char key;


TVout TV;
pollserial pserial;

bool receiving = false;
uint8_t idleFrames = 0;
const uint8_t TIMEOUT_FRAMES = 6;  // ~100 ms of silence = end of message

void setup() {
  keypad = MatrixKeypad_create((char*)keymap /* don't forget to do this cast */, rowPins, colPins, rown, coln); //creates the keypad object

  
  TV.begin(NTSC,120,96);
  TV.select_font(font4x6);
  intro();
  TV.set_hbi_hook(pserial.begin(1200));

  
  // TV.select_font(font4x6);
  // TV.select_font(font6x8);
  // TV.select_font(font8x8);

  
  TV.clear_screen();

  reboot();
}

void loop() {
  MatrixKeypad_scan(keypad); //scans for a key press event
	if(MatrixKeypad_hasKey(keypad)){ //if a key was pressed
		key = MatrixKeypad_getKey(keypad); //get the key
		if (key == '#') {
      TV.println();
      TV.print('>');
    }
    else TV.print(key); //prints the pressed key to the serial output
    Serial.print(key);
	}
  
  
  if (pserial.available()) {
    while (pserial.available()) {
      char c = (char)pserial.read();
      if (c == '~') {
        printGlyph();
      } else {
        TV.print(c);
      }
    }
    receiving = true;
    idleFrames = 0;
  } else if (receiving) {
    idleFrames++;
    if (idleFrames >= TIMEOUT_FRAMES) {
      TV.print("> ");
      receiving = false;
    }
  }

  TV.delay_frame(1);
}

void intro() {
unsigned char w,l,wb;
  int index;
  w = pgm_read_byte(TVOlogo);
  l = pgm_read_byte(TVOlogo+1);
  if (w&7)
    wb = w/8 + 1;
  else
    wb = w/8;
  index = wb*(l-1) + 2;
  for ( unsigned char i = 1; i < l; i++ ) {
    TV.bitmap((TV.hres() - w)/2,0,TVOlogo,index,w,i);
    index-= wb;
    TV.delay(50);
  }
  for (unsigned char i = 0; i < (TV.vres() - l)/2; i++) {
    TV.bitmap((TV.hres() - w)/2,i,TVOlogo);
    TV.delay(50);
  }
  TV.delay(3000);
  TV.clear_screen();
}

void reboot() {
  TV.select_font(font4x6);
  TV.println(0,0,"=Marktek Delta 6502=");
  TV.println("PREPARING TERMINAL");
  TV.delay(1500);
  TV.println("READY");
  TV.print("> ");
}

void printGlyph() {
  TV.bitmap(0,0,glyph);
  TV.delay(3000);
  TV.clear_screen();  // replace with whatever puppy() should do
}