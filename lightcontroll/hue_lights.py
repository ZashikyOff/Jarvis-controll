from phue import Bridge
# from ip_adress import bridge_ip_adress
import time

bridge_ip_adress = '192.168.0.36'
b = Bridge(bridge_ip_adress)





def access_lights(bridge_ip_adress):
    b = Bridge(bridge_ip_adress)
    light_names_list = b.get_light_objects('name')
    return light_names_list

def film_lights(hue):
    lights = access_lights(bridge_ip_adress)
    for light in lights:
        lights[light].on = True
        lights[light].hue = hue
        lights[light].brightness = 254
        lights[light].saturation = 254

def danger_mod():
    lights = access_lights(bridge_ip_adress)
    while True:
        time.sleep(1)
        for light in lights:
            lights[light].on = True
            lights[light].hue = 180
            lights[light].brightness = 254
            lights[light].saturation = 254
        time.sleep(1)
        for light in lights:
            lights[light].on = True
            lights[light].hue = 7000
            lights[light].brightness = 254
            lights[light].saturation = 254

def rainbow():
    lights = access_lights(bridge_ip_adress)
    totalTime = 30 # in seconds
    transitionTime = 1 # in seconds
    maxHue = 65535
    hueIncrement = maxHue / totalTime
    for light in lights:
        lights[light].on = True # uncomment to turn all lights on
        lights[light].transitiontime = transitionTime * 10
        lights[light].brightness = 254
        lights[light].saturation = 254

    hue = 0
    while True:
        for light in lights:
            lights[light].hue = hue

        hue = (hue + hueIncrement) % maxHue
        print(hue)
        time.sleep(transitionTime)

def bycolor(color):
    if color == "bleu":
        blue = 45000
        film_lights(blue)
    if color == "rouge":
        red = 63000
        film_lights(red)
    if color == "verte":
        green = 25000
        film_lights(green)
    if color == "violet":
        purple = 51000
        film_lights(purple)

if __name__ == "__main__":
    rainbow()