#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 7, 6, 5, 4, 3);

String data;

int button = 9;
int button2 = 10;
int button3 = 11;

int sum = 0;
int sum2 = 0;
int sum3 = 0;

void setup() 
{

  pinMode(button, INPUT);
        
  Serial.begin(9600);
  lcd.begin(16, 2);
        
}

void loop() 
{
  
  if (Serial.available() > 0) 
  {
    data = Serial.readString();
    lcd.clear();
    lcd.home();
    lcd.print(data);
    delay(20);
  }

  sum = digitalRead(button);
  if (sum == HIGH)
  {
    sum = digitalRead(button);
    Serial.println("Buton1'e basildi");
    while (sum == HIGH)
    {
      sum = digitalRead(button);
    }
    
  }
  sum2 = digitalRead(button2);
  if (sum2 == HIGH)
  {
    sum2 = digitalRead(button2);
    Serial.println("Buton2'e basildi");
    while (sum2 == HIGH)
    {
      sum2 = digitalRead(button2);
    }
    
  }
  sum3 = digitalRead(button3);
  if (sum3 == HIGH)
  {
    sum3 = digitalRead(button3);
    Serial.println("Buton3'e basildi");
    while (sum3 == HIGH)
    {
      sum3 = digitalRead(button3);
    }
    
  }
  
}
