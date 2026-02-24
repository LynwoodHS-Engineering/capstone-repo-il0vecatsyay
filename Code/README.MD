# Named variables for motor pins

const int ENB = 3;   # Enable pin B
const int IN4 = 4;   # Input 4
const int IN3 = 5;   # Input 3
const int ENA = 9;   # Enable pin A
const int IN1 = 8;   # Input 1
const int IN2 = 7;   # Input 2

# Named variables for button and buzzer pins

const int Button = 2;  # Button with INPUT_PULLUP
const int Beep   = 12; # Buzzer pin

int lastButtonState = HIGH; # INPUT_PULLUP (not pressed = HIGH)

void setup() {
  # Motor pins connection to the Arduino board

  pinMode(ENB, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  # Button and Buzzer connection to the Arduino board

  pinMode(Button, INPUT_PULLUP);
  pinMode(Beep, OUTPUT);
}

void beepOnce() {
  tone(Beep, 1000); # 1000 Hz beep
  delay(200);       # 0.2 s
  noTone(Beep);
}

void loop() {
  int buttonState = digitalRead(Button);


  if (lastButtonState == HIGH && buttonState == LOW) {
    beepOnce(); # beep when button is pressed
  }
  if (lastButtonState == LOW && buttonState == HIGH) {
    beepOnce();  # beep when button is released
  }

  # Motor control
  if (buttonState == LOW) {       # button pressed -> motors on
    digitalWrite(IN4, HIGH);
    digitalWrite(IN3, LOW);
    analogWrite(ENB, 191);         # motors on 75% speed

    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 191);       # 75% speed
  } else {                       # button released -> motors off
    analogWrite(ENB, 0);
    analogWrite(ENA, 0);
  }

  lastButtonState = buttonState; # update button state
}


