import socketpool
import neopixel
import board
import wifi
import time
import ssl
import sys

#API TCP Server and WIFI settings
TIMEOUT = None
HOST = "tcp.alerts.com.ua"
PORT = 1024
WIFI_SSID = "WIFI_SSID"
WIFI_PASSWORD = "WIFI_PASS"

#Connecting Pi Pico to WIFI, initializing socketpool
try:
    wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connected to WiFi")

except Exception as e:    
    print("Failed to connect.")
    print("Error:\n", str(e))
    sys.exit()
    
pool = socketpool.SocketPool(wifi.radio)


#Initializaton of GPIO pin(PWM), responsible for sending signal into the RGB LED strip
#Setting parameters for neopixel library and assigning it into a variable,
#so there is no need to set them every time the function is being called
pixel_pin = board.GP27
num_pixels = 200
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
red = (255,5,5)
green = (20,255,20)
blue = (0,0,255)
dark_red = (255,5,5)


#A dictionary with keys as an ID of a district returned by API(example: 13 - Lviv)
#and values as current state of airstrike("on"/"off") and ID of every LED on map, attached to it's own district(0-148)
led = {
'0':           [0,1,2,3,4,5,6,7],
'20':          [8,9,10,65,66,67],
'7':           [11,12,13,59,60,61],
'4':           [14,15,16,56,57,58],
'11':          [17,18,19,20,21,22,53,54,55],
'19':          [23,24,25,50,51,52],
'17':          [26,27,28,41,42,43],
'24':          [29,30,31,32,33,34],
'9':           [35,36,37,92,93,94],
'15':          [38,39,40,44,45,46],
'3':           [47,48,49,62,63,64],
'13':          [68,69,70,74,75,76],
'14':          [71,72,73,110,111,112,113,114,115],
'10':          [77,78,79,80,81,82],
'22':          [83,84,85,86,87,88],
'1':           [89,90,91,107,108,109],
'5':           [95,96,97,101,102,103],
'16':          [98,99,100,137,138],
'21':          [104,105,106,149,150],
'23':          [116,117,118],
'8':           [119,120,121,144,145,146],
'6':           [122,123,124,125,126,127],
'12':          [128,129,130,139,140,141],
'2':           [131,132,133,134,135,136],
'18':          [142,143,147,148]
}
#Crimea(The API doesn't provide any information about the status of an airstrike in Crimea,
#so it's status is always assumed to be "on".)
for diod in led["0"]:
        pixels[diod] = dark_red


#Showing updated status of district on map, by turning on the coresponding LEDs.
#Delay is needed because of the neopixel's library speed limitation.
def statusShow(district_id, status):
    district_id = str(district_id)
    status = str(status)
    for diod in led[district_id]:
        if status == 1:
            pixels[diod] = red
            pixels.show()
        if status == 0:
            pixels[diod] = green
            pixels.show()
      

#Creating TCP pool, setting it`s timeout, connecting to API server
print("Creating Socket")
with pool.socket(pool.AF_INET, pool.SOCK_STREAM) as s:
    s.settimeout(TIMEOUT)
    print("Connecting")
    s.connect((HOST, PORT))
    print("Sending")
    #Sending API key to a server(it`s the only one packet being sent from Pi Pico) 
    sent = s.send("API_KEY")
    print("Recieving")
    #Buffer variable to recieve packets
    buff = bytearray(128)
    while True:
        #Recieving packets from a server(first response is always an auth-packet, as a proof, that your API is valid)
        numbytes = s.recv_into(buff)
        text = buff.decode("utf-8")
        #If status of airstrike changes - server sends you a packet, with district's ID(1-24) and it's status(0/1)
        #Example: Lviv, airstrike on(s:13 = 1)
        #For every iteration(i), if i == district ID, then it's status and ID itself are being sent into stautsShow()
        if "s:" in text:           
            for i in range(1,25):                
                if f"s:{i}=" in text:
                    #(Sometimes server sends status of multiple districts in one packet simultaneously, so split() is needed)
                    district=text[text.find(f"s:{i}=")+2:].split()[0]
                    status=dsitrict[-1:]
                    print(f"Found: id={i}; status={status}")
                    statusShow(i, status)
            

