#Named variables for motor pins
const int ENB = 3;   # Enable pin B
const int IN4 = 4;   # Input 4
const int IN3 = 5;   # Input 3
const int ENA = 9;   # Enable pin A 
const int IN1 = 8;   # Input 1
const int IN2 = 7;   # Input 2 

#Named variables for button and buzzer pins
const int Button = 1;  # Button with INPUT_PULLUP
const int Beep   = 12; # Buzzer pin

const int SOL_PIN = 11; # Solenoid driver input

const unsigned long RETRACT_MS = 400;
const unsigned long EXTEND_MS  = 250;
const unsigned long DEBOUNCE_MS = 20;
const unsigned long BEEP_MS = 200;
const unsigned long STATUS_MS = 500;

int lastRaw = HIGH;
unsigned long lastDebounceTime = 0;
int debouncedButton = HIGH; # debounced current reading
int lastButtonState = HIGH; # for edge detection

unsigned long beepStart = 0;
bool beeping = false;

enum PState { IDLE, RETRACTING, EXTENDING };
PState pstate = IDLE;
unsigned long pstateStart = 0;
unsigned long lastStatus = 0;

void setup() {
  # Motor pins functions to arduino board
  pinMode(ENB, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  # Button and Buzzer functions to arduino board
  pinMode(Button, INPUT_PULLUP);
  pinMode(Beep, OUTPUT);
  noTone(Beep);

  # Piston functions to arduino board 
  pinMode(SOL_PIN, OUTPUT);
  digitalWrite(SOL_PIN, LOW);

  Serial.begin(115200);
  while (!Serial) { /* wait on some boards */ }
  Serial.println("Combined sketch (fixed) started");
}

void loop() {
  unsigned long now = millis();

  # Read + debounce button (button -> GND when pressed)
  int raw = digitalRead(Button);
  if (raw != lastRaw) {
    lastDebounceTime = now;
    lastRaw = raw;
  }
  if (now - lastDebounceTime > DEBOUNCE_MS) {
    if (raw != debouncedButton) {
      debouncedButton = raw;

      # edge detection for beep
      if (lastButtonState == HIGH && debouncedButton == LOW) startBeep();
      else if (lastButtonState == LOW && debouncedButton == HIGH) startBeep();

      # trigger piston on press if idle
      if (debouncedButton == LOW && pstate == IDLE) startRetractThenExtend();
    }
  }

  # update lastButtonState AFTER handling edges
  lastButtonState = debouncedButton;

  # Stop beep when time elapsed
  if (beeping && (now - beepStart >= BEEP_MS)) {
    noTone(Beep);
    beeping = false;
  }

  # Motor control
  if (debouncedButton == LOW) {
    digitalWrite(IN4, HIGH);
    digitalWrite(IN3, LOW);
    analogWrite(ENB, 191); // 75%

    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 191); // 75%
  } else {
    analogWrite(ENB, 0);
    analogWrite(ENA, 0);
  }

  # Piston state machine (timed)
  if (pstate == RETRACTING) {
    if (now - pstateStart >= RETRACT_MS) {
      Serial.println("Retract wait done — firing extend pulse");
      digitalWrite(SOL_PIN, HIGH);
      pstate = EXTENDING;
      pstateStart = now;
      Serial.println("EXTEND pulse started");
    }
  } else if (pstate == EXTENDING) {
    if (now - pstateStart >= EXTEND_MS) {
      digitalWrite(SOL_PIN, LOW);
      pstate = IDLE;
      Serial.println("EXTEND complete, solenoid OFF");
    }
  }

  # Reading back status
  if (now - lastStatus >= STATUS_MS) {
    lastStatus = now;
    Serial.print("t="); Serial.print(now);
    Serial.print(" state="); Serial.print(pstate == IDLE ? "IDLE" : pstate == RETRACTING ? "RETRACTING" : "EXTENDING");
    Serial.print(" sol="); Serial.print(digitalRead(SOL_PIN));
    Serial.print(" btn="); Serial.println(debouncedButton == LOW ? "PRESSED" : "RELEASED");
  }
}

void startBeep() {
  tone(Beep, 1000);
  beeping = true;
  beepStart = millis();
}

void startRetractThenExtend() {
  digitalWrite(SOL_PIN, LOW);
  pstate = RETRACTING;
  pstateStart = millis();
  Serial.println("Start retracting (solenoid OFF)");
}
