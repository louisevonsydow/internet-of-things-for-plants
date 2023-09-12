import pycom
from machine import ADC
import time
pycom.heartbeat(False) # disable the heartbeat LED (to let the controller light up in other colors)

# defines the two pins where we get the analog data from the two sensors (p1 = temp data, p2 = moist data)
pin1 = ADC().channel(pin='P17')
pin2 = ADC().channel(pin='P18', attn = ADC.ATTN_11DB) # setting attention span. Tradeoff (makes  less accurate) The ADC input pins can by default only read input signals between 0-1.1V. With attenuation in the code we can increase this to 0-3.3V. 

#setting parameters 
min_moist = 1500
max_moist = 2500
min_temp = 10
max_temp = 50

while True:
  temp_mv = pin1.voltage() 
  celsius = round(((temp_mv - 500)/10),1) # converting voltage input from sensor to temperature value (in celsius) 
  pybytes.send_signal(0, celsius) #sending signal to pybytes #'temp is {} C°'.format(celsius)
  print(celsius, ' C°') 

  moist_mv = pin2.voltage()
  moisture =   moist_mv #write the correct function
  pybytes.send_signal(1, moisture) #'moist is {} water/area'.format(moisture)
  print(moisture)

  days_left = (int)((2500-moisture)/(celsius*11)) # approximate function where the future moisture depends on current temperature
  if days_left < 0:
    days_left = 0
  pybytes.send_signal(2, days_left)
  print(days_left, "days left")

  if moist_mv < min_moist: # too moist
    pycom.rgbled(0x0004ff)  # Blue
  elif moist_mv > max_moist: #too dry
    pycom.rgbled(0xff0000)  # Red
  else: # good
    pycom.rgbled(0x00ff00)  # Green
  time.sleep(10) # re-reads the values every 10 min (600 sek)