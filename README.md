# Physical Map of airstrikes in Ukraine
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/17.jpg?raw=true)
## Introduction
This project is made on Raspberry Pi Pico, using Cicruit Python

Capabilities:
- Changes color of each district, depending on it's state of airstrike
- Doesn't have any delay with realtime online maps
- Works from a simple outlet
  
Features:
- Doesn't use polling (only recieves alerts from API server)
- Code is not proprietary(only WIFI, API_KEYS, and etc.)
- It's open source! Feel free to fork the project!
*API: https://alerts.com.ua/*

## Making process
This whole project was a challange for me, which inspired me and made me learn a lot.
Originally, this project was meant to be working on Arduino, but it turned out not to be as efficient and cheap.
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/2.jpg?raw=true)
Later on, when Pi Pico was chosen for it's compactness, it turned out that it's GPIO pins output only 3.3V of current, while LED strip needs 5V input for signal,
so i had to use a logic-gate converter. Learning how it works was a lot of fun!
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/3.jpg?raw=true)
The plastic backbone on which Pi Pico and logic-gate converter are placed on were drawn in SolidWorks,
so it matches the dimensions of the box, where it will be stored alongside with a Power supply.
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/4.jpg?raw=true)
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/5.jpg?raw=true)
After that, the map and every district were designed in CorelDraw and prepared for a cut in RDWorks. A laser cutting machine was used, because of its power, managing to slice trough the needed material and it's speed.
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/8.jpg?raw=true)
Then, it was time to glue the map together with a plywood frame, and start the LED compounding process(the hardest, and so most interesting part).
I had to design compounding of the signal and power cords, so i don't loose track of where i am and make the most efficient compounding. The signal is connected consecutively, but the power had to be connected in a "tree" shape, so there is no voltage drop anywhere(Yellow - LEDs, Red and orange - Power, the rest - signal(it's a one big cord, but i had to use few colors after every cross, so i don't go worng way by mistake).
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/10.jpg?raw=true)
Every district had 6~7 LEDs(~3 LEDs in front of every side of it's name, so the backlighting was spread evenly).
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/14.jpg?raw=true)
After the map was gripped to the wall - the best part came. Coding time!

*P.S: There was also a small hole milled in the box for a USB cable, so the code can be modified without disassembling the box.*
![alt text](https://github.com/MoonLighTingPY/airstrike_map_Ukraine/blob/main/images/12.jpg?raw=true)
## And finally, after trial and error, the project was finally finished!
*But it's not polished yet, so feel free to add new functional by forking the repository!* Thanks!




