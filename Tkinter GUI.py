import tkinter as tk
from Adafruit_IO import Client, Feed, RequestError

# Credentials
ADAFRUIT_IO_USERNAME = "Enter your username "
ADAFRUIT_IO_KEY = "Enter your Key"

# Feed names
LED_FEED = "led"
SERVO_FEED = "servo"

# Setup client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create feeds if not exist
def ensure_feed(feed_name):
    try:
        return aio.feeds(feed_name)
    except RequestError:
        return aio.create_feed(Feed(name=feed_name))

led_feed = ensure_feed(LED_FEED)
servo_feed = ensure_feed(SERVO_FEED)

# GUI Functions
def turn_on():
    aio.send(LED_FEED, 1)
    status_label.config(text="LED Status: ON")

def turn_off():
    aio.send(LED_FEED, 0)
    status_label.config(text="LED Status: OFF")

def set_servo_angle(value):
    angle = int(float(value))
    aio.send(SERVO_FEED, angle)
    servo_label.config(text=f"Servo Angle: {angle}°")

def set_angle_0():
    angle_slider.set(0)
    set_servo_angle(0)

def set_angle_90():
    angle_slider.set(90)
    set_servo_angle(90)

def set_angle_180():
    angle_slider.set(180)
    set_servo_angle(180)

# GUI setup
root = tk.Tk()
root.title("ESP8266 LED & Servo Controller")
root.geometry("300x400")

tk.Label(root, text="Control LED via Adafruit IO").pack(pady=10)
tk.Button(root, text="Turn ON", command=turn_on, width=20, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Turn OFF", command=turn_off, width=20, bg="red", fg="white").pack(pady=5)

status_label = tk.Label(root, text="LED Status: Unknown")
status_label.pack(pady=10)

tk.Label(root, text="Control Servo Angle").pack(pady=5)
angle_slider = tk.Scale(root, from_=0, to=180, orient='horizontal', command=set_servo_angle)
angle_slider.pack()

servo_label = tk.Label(root, text="Servo Angle: Unknown")
servo_label.pack(pady=10)

# Angle Control Buttons
tk.Button(root, text="Set 0°", command=set_angle_0, width=10).pack(pady=2)
tk.Button(root, text="Set 90°", command=set_angle_90, width=10).pack(pady=2)
tk.Button(root, text="Set 180°", command=set_angle_180, width=10).pack(pady=2)

root.mainloop()
