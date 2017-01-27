/*
 * IRremote: IRsendDemo - demonstrates sending IR codes with IRsend
 * An IR LED must be connected to Arduino PWM pin 3.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */


#include <IRremote.h>

IRsend irsend;

byte data_buffer[100];

void setup(){
  Serial.begin(9600);
}

void loop() {
	if(Serial.available() > 0){
    byte head = Serial.read();
    if(head != 0xAA){
      return;
    }
    while(Serial.available() < 4){
    }
    int readed = Serial.readBytes(data_buffer, 4);
    irsend.sendNEC(*((long*)data_buffer), 32);
	}
}
