const int ENB = 3;  //Motor Pins L298N
const int IN4 = 4;  //Motor Pins L298N
const int IN3 = 5;  //Motor Pins L298N
const int ENA = 9;  //Motor Pins L298N
const int IN1 = 8;  //Motor Pins L298N
const int IN2 = 7;  //Motor Pins L298N
const int Button = 2;  //Button Pins Arduino 
const int LDR_PIN = A0;  //Light Sensor Pin
const int Beep = 12;  //Pietzo Buzzer
const int SOL_PIN = 11;  //Solenoid Pin

int lightThreshold = 600;
const unsigned long RETRACT_MS = 2000;   // wait before firing
const unsigned long EXTEND_MS = 100;     // pulse duration
const unsigned long STATUS_MS = 500;

bool wasDark = false;  //Setting the Light Sensor to fire when it detects "dark"
bool lastButtonState = HIGH;

enum PState { IDLE, WAITING, FIRING };
PState pstate = IDLE;
unsigned long pstateStart = 0;
unsigned long lastStatus = 0;

void setup() {
  pinMode(ENB, OUTPUT);  
  pinMode(IN4, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(Button, INPUT_PULLUP);
  pinMode(Beep, OUTPUT);
  digitalWrite(Beep, LOW);
  pinMode(SOL_PIN, OUTPUT);
  digitalWrite(SOL_PIN, LOW);
  pinMode(LDR_PIN, INPUT);
  Serial.begin(115200);
  Serial.println("System ready");
}

bool isDark() {
  return analogRead(LDR_PIN) < lightThreshold;
}

// ── BUTTON: motors only ──────────────────────────────────────────
void handleButton() {
  int buttonState = digitalRead(Button);

  // beep on press edge
  if (lastButtonState == HIGH && buttonState == LOW) {
    digitalWrite(Beep, HIGH);
    delay(120);
    digitalWrite(Beep, LOW);
  }
  lastButtonState = buttonState;

  // motors run while button held
  if (buttonState == LOW) { 
    digitalWrite(IN4, HIGH);  
    digitalWrite(IN3, LOW);
    analogWrite(ENB, 191);
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    analogWrite(ENA, 191);
  } else {
    analogWrite(ENB, 0);
    analogWrite(ENA, 0);
  }
}

// ── LDR: piston only
void handleLDR() {
  bool darkNow = isDark();

  // trigger only on bright → dark transition
  if (darkNow && !wasDark && pstate == IDLE) {
    pstate = WAITING;           // start retract wait, solenoid stays LOW
    pstateStart = millis();
  }
  wasDark = darkNow;
}

void handlePiston() {
  unsigned long now = millis();

  if (pstate == WAITING) {
    if (now - pstateStart >= RETRACT_MS) {
      digitalWrite(SOL_PIN, HIGH);  // fire solenoid after wait
      pstate = FIRING;
      pstateStart = now;
    }
  }
  else if (pstate == FIRING) {
    if (now - pstateStart >= EXTEND_MS) {
      digitalWrite(SOL_PIN, LOW);   // retract solenoid
      pstate = IDLE;
    }
  }
}

// ── STATUS ────────────────────────────────────────────────────────
void handleStatus() {
  unsigned long now = millis();  //working on this section, attempted to fire the piston when the LDR detected "dark"
  if (now - lastStatus >= STATUS_MS) {
    lastStatus = now;
    Serial.print("light=");
    Serial.print(analogRead(LDR_PIN));
    Serial.print(" piston=");
    Serial.print(pstate == IDLE    ? "IDLE"    :
                 pstate == WAITING ? "WAITING" : "FIRING");
    Serial.print(" motor=");
    Serial.println(digitalRead(Button) == LOW ? "ON" : "OFF");
  }
}

void loop() {
  handleButton();   //cycle all over again
  handleLDR();
  handlePiston();
  handleStatus();
}
