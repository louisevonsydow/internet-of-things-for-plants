# The Plant Nanny - keep track of your plants using a remote notification system

>Too many times I've been travelling and coming home to dead plants. Sometimes you don't want to disturb your neighbours or friends with asking them to babysit your plants for you, and this is where the Plant Nanny comes in handy. :seedling::hibiscus:
>
> This tutorial serves as a step-by-step guide for creating a plant monitoring system that will notify you when your plant's living conditions are not optimal. This simple IoT system is built with a LoPy4 microcontroller and temperature and moisture sensor. The sensors are connected to the LoPy4, which sends data via Wifi to Pybytes, which in turn forwards the data to Datacake. In Datacake, rules are defined. When a condition of a rule is satisfied, Datacake sends specified messages to Telegram via webhook which enables you getting notifications to your phone.



> :clock1: **Time required for this project:** approx 8 hrs depending on experience (excluding ordering materials)

###### By: `Louise von Sydow (ly222aq)`

## Objective

I chose this project because I wanted to learn how to build a simple IoT system end-to-end, which could easily be advanced with more sensors and back end programming. By storing data from the sensors, this project could be further enhanced by implementing a learning algorithm. Thus, not only using the sensors to monitor the plants based on defined criterias but to also use them to learn what is the optimal living environments for different plants.
## Material

| Devices          | Specification | Buy here     |
| -----------------|-------------|:-------------|
| LoPy4            |A MicroPython-programmable microcontroller.|[:link:][LoPy4]|
| Expansion board 3.0 |Helps to connect the LoPy4 via USB to computer. |[:link:][expboard]  |
| **Sensors**      |             |              |
| MCP9700   |Measuring air temperature.  |[:link:][MCP9700] |
| FC-28   |Measuring soil moisture, by measuring voltage between two capacitors.  |[:link:][FC-28] |
| **Essentials**      |             |              |
| Breadboard      |Helps to hold the electronic components and create circuits easily.|[:link:][breadboard]|
| Jumper wires      |Helps create electrical connecions between sensors and LoPy4.|[:link:][jumpwires]|
| Micro-USB cable      |To connect LoPy4 to computer.|  [:link:][microusb]|
| USB to USB-C adapter      | If you're using Macbook with only USB-C port.     | [:link:][usb-c]             |

:::info
:bulb: **Tip:** You can also buy the whole kit here: [:link:][electrokit](everything above excluding soil moisture sensor and USB-C adapter)
:::

[LoPy4]: 
https://pycom.io/product/lopy4/
[expboard]: 
https://pycom.io/product/expansion-board-3-0/
[MCP9700]: 
https://www.electrokit.com/produkt/mcp9700-e-to-to-92-temperaturgivare/?gclid=CjwKCAjwgISIBhBfEiwALE19SZUtsfu1LBCteToAIidWIJq1q0nx-slwVhckyGspQhImi2D6rTMBNxoCdBsQAvD_BwE
[FC-28]:
https://www.amazon.com/FC-28-C-Moisture-Detection-Control-Humidity/dp/B00MSGM2ZA
[electrokit]:
https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/
[usb-c]:
https://inf.se/usb-c/2134-supersnabb-adapter-usb-c-till-usb-30-svart-7314280039401.html?gclid=CjwKCAjwgISIBhBfEiwALE19SeZQoKcmcn3iV_Qhk4MttnDBYAfEwr8T3keyY6MrXdFTEhVmWrViVRoCSRAQAvD_BwE
[breadboard]:
https://www.amazon.se/AZDelivery-Breadboard-Kit-breadboard-Book/dp/B078JGQKWP/ref=sr_1_2?adgrpid=116085610470&dchild=1&gclid=CjwKCAjwjJmIBhA4EiwAQdCbxms5eVpZWuZW_etlbWXtCIJ5QTleTswqx4aHky8oozadgKq7tW3COhoCXXIQAvD_BwE&hvadid=475474674123&hvdev=c&hvlocphy=1012427&hvnetw=g&hvqmt=b&hvrand=4537760493000767342&hvtargid=kwd-58630210&hydadcr=6117_2165129&keywords=breadboard+kit&qid=1627831936&sr=8-2
[jumpwires]:
https://www.amazon.se/AZDelivery-Breadboard-Kit-breadboard-Book/dp/B078JGQKWP/ref=sr_1_2?adgrpid=116085610470&dchild=1&gclid=CjwKCAjwjJmIBhA4EiwAQdCbxms5eVpZWuZW_etlbWXtCIJ5QTleTswqx4aHky8oozadgKq7tW3COhoCXXIQAvD_BwE&hvadid=475474674123&hvdev=c&hvlocphy=1012427&hvnetw=g&hvqmt=b&hvrand=4537760493000767342&hvtargid=kwd-58630210&hydadcr=6117_2165129&keywords=breadboard+kit&qid=1627831936&sr=8-2
[microusb]:
https://www.amazon.se/AmazonBasics-hane-Micro-B-kabel-Svart/dp/B07232M876/ref=sr_1_4?dchild=1&keywords=Micro+USB+cable&qid=1627832065&sr=8-4



## Computer setup

### Connect hardware

1. Insert the LoPy4 into the expansion board. Note: The RGB LED in the LoPy4 should be above the USB connector as shown below.
![](https://i.imgur.com/cHwn5zx.jpg)


2. Connect the USB cable to the micro USB port and your computer's serial port.

### Update firmware
1. Update the firmware of the device, follow instructions [here](https://docs.pycom.io/updatefirmware/device/). Note: The device has to be connected to the computer while doing this.

### Install software
The following guide is for **MacOS**, if you are using **Windows** follow this
[step-by-step guide for Windows](https://hackmd.io/@lnu-iot/rk4qNlajd).

1. Install Node.js [here](https://nodejs.org/en/).
2. Install an IDE, I'm using VSCode. To install VSCode on MacOS, follow instructions [here](https://code.visualstudio.com/docs/setup/mac).
3. Setup Pymakr for VSCode by following instructions [here](https://docs.pycom.io/gettingstarted/software/vscode/).

Guide for how to use Pymakr: https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr

### Create project

You’ve already installed Pymakr in your IDE, and you’ve established a connection to the port.

1. When inside Pymakr console: create a new folder if you already aren’t in a blank folder and name it what you like (I named it "IoT").
2. Add a new folder called `lib`
3. Add a new file called `library.py` inside of the lib folder.
4. Add a new file called `main.py` outside of the lib folder.
5. Add a new file called `boot.py` outside of the lib folder.

![](https://i.imgur.com/YNKjNGh.png)



### Try out your device
Time to write some code!

1. Inside `main.py`, paste following code snippet:
```javascript=16
import pycom
pycom.heartbeat(False) #Disable heartbeat LED (to enable other colors)
while True: #Forever loop
    pycom.rgbled(0xFF0000)  #Red
```
    
Now press `upload` in the Pymakr REPL.
![](https://i.imgur.com/iya0yT6.png)
If the LED lamp on the LoPy4 lights up red, your set up works!


## Putting everything together

The temperature sensor is a basic analog sensor with 3 pins; one is connected to current (3.3V or 5V), one is connected to ground (GND) and one is connected to the output (ADC-pin).

Following image is an example of how to connect the temperature sensor to the LoPy4 via a breadboard:
![](https://i.imgur.com/PDOMcm2.jpg)
:::info
:exclamation: **Obs:** The temperature sensor have a flat and a curved face, make sure it is connected as above.
:::



The soil moisture sensor has 4 pins that is labled A0 (should connect to ADC-pin), D0 (for digital output), GND (should connect to GND), and VCC (should connect to 3V3 (3.3V) or VIN (which is 5V from USB)).

### Circuit diagram
The following diagram shows how I have connected the sensors:
![](https://i.imgur.com/SMaMioU.jpg)

1. 3V3 (3.3V) in expansionboard is connected to **+** power rail in breadboard (with red wire)
2. GND in expansionboard is connected to **-** power rail in breadboard (with blue wire)
3. Temperature sensor (MCP9700) is connected to P17.
4. Soil moisture sensor (FC-28) is connected to P18.

You could connect the sensors to other ADC-pins, but P17 and P18 worked for me. See this [schematic](https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf) to see which other pins you could use.

My setup finally looked like this:
![](https://i.imgur.com/hyplf2X.jpg)


## Platforms

This project is using the platforms [Pybytes](https://pybytes.pycom.io/), [Datacake](https://datacake.co/), and [Telegram](https://telegram.org/). 
![](https://i.imgur.com/oBEN7ab.png)


Firstly, the data is transmitted to Pybytes via Wifi connection. Pybytes is used because it is built for Pycom devices and is simple to use. Pybytes stores the data (up to 1 MB) and offers data visualization and integrations with external services.

Secondly, Pybytes is integrated with Datacake. The reason for this is that Datacake is easy to integrate with Telegram, and Telegram is the platform I want to use to send notifications to my phone.

If you want to scale up your IoT system: 
Firstly, Pybytes only offers 1MB of data storage. Secondly, Datacake only offers 2 connected devices for free. However, both of the platforms offers paid subscription services if you want to use more devices or store more data, which make them suitable to use if you want to scale up your system.

For instructions on how to set up the platforms and integrate them with each other, see [Transmitting the data](#Transmitting-the-data).


## The code

Here's the code in `main.py`:
```javascript=16
import pycom
from machine import ADC
import time
pycom.heartbeat(False) #Disable heartbeat LED (to enable other colors)

#1 Define the ADC-pins
pin1 = ADC().channel(pin='P17')
pin2 = ADC().channel(pin='P18', attn = ADC.ATTN_11DB) # setting attention span. Tradeoff (makes  less accurate) The ADC input pins can by default only read input signals between 0-1.1V. With attenuation in the code we can increase this to 0-3.3V. 

#2 Setting the parameters 
min_moist = 1400
max_moist = 2500
min_temp = 10
max_temp = 50

while True:
#3 Calculating temperature
  temp_mv = pin1.voltage() 
  celsius = (temp_mv - 500.0) / 10.0

#4 Get soil moisture
  moisture = pin2.voltage()

#5 Calculate days left until plant needs watering
  days_left = (int)((2500-moisture)/(celsius*11))
  if days_left < 0:
    days_left = 0
  
#6 Send data to Pybytes  
    pybytes.send_signal(0, celsius)
    pybytes.send_signal(1, moisture)
    pybytes.send_signal(2, days_left)
    
#7 Setting up LED-lamp
  if moist_mv < min_moist: # Too moist
    pycom.rgbled(0x0004ff)  # Blue
  elif moist_mv > max_moist: # Too dry
    pycom.rgbled(0xFF0000)  # Red
  else: # good
    pycom.rgbled(0x00FF00)  # Green

#8 Define sleep interval  
  time.sleep(600) # Re-reads the values every 10 min
```

Explanation of the code:

**#1 Define the ADC-pins:** defining the two pins where we get the analog data from the two sensors (p1 = temp data, p2 = moisture data). The `attn = ADC.ATTN_11DB` was needed to correct the input from the moisture sensor, because the ADC input pins can by default only read input signals between 0-1.1V. With attenuation set to 11DB in the code we can increase this to approximately 3.6V.

**#2 Setting the parameters:** By calibrating the sensors (seeing what values the sensors give in water/air/desirable soil moisture) a desirable moisture interval is defined

**#3 Calculating temperature:** The voltage from the temp sensor is converted to celsius using the formula `(millivolts - 500) / 10`.

**#4 Get soil moisture:** Read the input value from the ADC-pin.

**#5 Calculate days left until plant needs watering:** An approximate function where the future moisture depends on current temperature.

**#6 Send data to Pybytes:** Sending 3 different signals to pybytes (each one is 8 bytes) 

**#7 Setting up LED-lamp:** So that it lights up red if it's too dry, green if it's within the optimal interval, and blue if it's overwatered.

**#8 Define sleep interval:** Datacake only stores 500 datapoints per day, which is why I set up the frequency to once every 10 minutes (which satisfies the purpose of this project). With three signals, this results in approximately `3*6*24=432` datapoints per day. 


## Transmitting the data

The plant is assumed to be inside the home, and a WiFi connection is enough to satisfy the range requirements for this project. Therefore, I chose to transmit the data via Wi-Fi to Pybytes. Furthermore, the data is only sent once every 10 min to save data storage and energy consumption.   

### Setting up Pybytes connection

1. To set up the connection to Pybytes, follow [these instructions](https://hackmd.io/@lnu-iot/r1bGPUOhu)

### Integrate Pybytes with Datacake

1. ![](https://i.imgur.com/WIW9TB4.png)
2. ![](https://i.imgur.com/Yffgor8.png)
3. ![](https://i.imgur.com/vas5UPn.png)
4. In the webhook integration, you first need to enter the URL. You find this in Datacake by clicking on Devices > Your Device > Configuration and scroll down to "HTTP Endpoint URL"  ![](https://i.imgur.com/7FYNWpb.png) 

HOWEVER: Pybytes has a bug which removes trailing slashes, so append some extra text in the end of the URL, for example "/pybytes", "/yourname" etc, like this:

![](https://i.imgur.com/il8nM90.png)
5. Customize your settings (default settings worked fine for me), select your device and click "Create". 


### Integrate Datacake with Telegram

1. Download [Telegram for computer and phone](https://telegram.org/).

3. To create rules in Datacake and send notifications via Telegram, follow [this instruction](https://docs.datacake.de/device/rule-engine/sending-notifications-via-telegram).

:::info
Note: If clicking the "Send message" button to Push More Bot doesn't automatically send a message in the Telegram app, try copying the URL instead and send it as a new message in the Telegram app, and it should work.
:::


## Presenting the data

### Visualization
I chose to visualize my data in a dashboard in Datacake like this:
![](https://i.imgur.com/6H3QXfN.png)
The data is saved 6 times/hr (as often as I send signals to Pybytes). 

To do this in Datacake:
1. Click on your device: ![](https://i.imgur.com/ZKPRoDC.png)

2. Press the button on the far right to enter edit mode:  ![](https://i.imgur.com/hup7ZyX.png)

3. Add and edit widgets as you wish

### Notifications

I set up following rules in Telegram:

:thermometer::snowflake: Too hot/too cold: message "Temperature alert! Current temperature is `[current temp]` degrees. Preferrable temperature is between `[min-temp]`-`[max-temp]` degrees." 
:fallen_leaf: Too dry: "It's time to water your plant!"
:sweat_drops: Too wet: "Your plant is overwatered. "
Only 1 day left: "Heads up! It's 1 day left until you need to water your plant."

![](https://i.imgur.com/iEtGIs1.jpg)



## Finalizing the design

Showing how the LED-lamp changes color in different conditions (Red = Too dry, Blue = Too wet, Green = Good):
{%youtube Cxj0m1jJr3o %}


Explanation of IoT system end-to-end:
{%youtube TSsLiQhRNv8 %}


Notifications from Telegram:
{%youtube I95ozamGuxQ %}

 
I think this project work as a proof of concept for how LoPy4 microcontroller together with sensors can be used to create a remote notification system.

The next step would be to let the microcontroller be battery powered instead so it could actually work as it's supposed to, where it doesn't need to be connected to a computer. Or even better, use a microcontroller with cellular connection so it works when the computer is not within the Wi-Fi area, for example when you're abroad. 