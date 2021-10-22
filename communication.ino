
// potentiometer.ino
// reads a potentiometer sensor and sends the reading over serial

int sensorPin = A0; // the potentiometer is connected to analog pin 0
int ledPin = 13; // the LED is connected to digital pin 13
int sensorValue; // an integer variable to store the potentiometer reading


void setup() { // this function runs once when the sketch starts up
  pinMode (ledPin, OUTPUT);
  // initialize serial communication 
  Serial.begin(9600);
}


void loop() { // this loop runs repeatedly after setup() finishes
  sensorValue = analogRead(sensorPin); // read the sensor
  Serial.println(sensorValue); // output reading to the serial line
  if (sensorValue < 500){
    digitalWrite(ledPin , LOW );} // turn the LED off
  else {
    digitalWrite(ledPin , HIGH );} // keep the LED on
  delay (100); // Pause in milliseconds before next reading
}
