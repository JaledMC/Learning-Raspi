from RPLCD.i2c import CharLCD
from time import sleep
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4)

lcd.clear()
lcd.write_string('Hello world')
lcd.cursor_pos = (2, 0)
sleep(2)
lcd.clear()


