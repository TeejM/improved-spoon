 #include <Servo.h>
 Servo  leftservo;
 Servo  rightservo;

void setup() {
 pinMode(2, OUTPUT);
 rightservo.attach(2);
 pinMode(3, OUTPUT);
 leftservo.attach(3);
}

void loop() {
 if (analogRead(4) >= 1000) {rotate();}
 else if (analogRead(1) >= 1000) {still(); delay(1000);}
}

void rotate() {
                rightservo.writeMicroseconds(1670);
                leftservo.writeMicroseconds(1450);
               }
void still() {
                rightservo.writeMicroseconds(1500);
                leftservo.writeMicroseconds(1500);
              }

