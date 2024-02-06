#include <DmxSimple.h>

void setup() {
  Serial.begin(9600);
  Serial.println("SerialToDmx Transmission Initiated!");
  Serial.println("Syntax:");
  Serial.println("<channel no>-<value>");
  Serial.println();
  DmxSimple.usePin(3);
}

int dmxValue = 0;
int dmxChannel;

void loop() {
  if (Serial.available()){
    char buff[50];
    String serInput = Serial.readStringUntil('\n');
    int splitPoint = serInput.indexOf("-");

    if (splitPoint != -1 && splitPoint != 0 && splitPoint != serInput.length() - 1){
      char indexZero = serInput.charAt(0);
      String value = serInput.substring(splitPoint+1);
      char valCheck = value.charAt(0);
      if (indexZero >= '1' && indexZero <= '9' && valCheck >= '1' && valCheck <= '9'){
        dmxChannel = serInput.substring(0, splitPoint).toInt();
        dmxValue = value.toInt();
        if (dmxValue <= 255){
          int valPerc = map(dmxValue, 0, 225, 0, 100);
          DmxSimple.write(dmxChannel, dmxValue);
          sprintf(buff, "channel %d set to -> %d perc", dmxChannel, valPerc);
          Serial.println(buff);
        }
        else {
          Serial.println("ValueError: value should be in range 0-225");
        }
      }
      else {
        Serial.println("Invalid Expression!");
      }
    }
    else {
      Serial.println("Invalid input format! Please use <channel no>-<value> format.");
    }
  }
}
