"""
A simple script to turn on/off a WS2812 LED strip based on the state of a slotted opto-coupler
mounted on a door.

Here is the specific model:
    https://www.amazon.com/dp/B08977QFK5?psc=1&ref=ppx_yo2ov_dt_b_product_details

Truth table:
    State           Opto-Coupler Value              Boolean Value
    ---------       --------------------------      -------------
    Door Open       Unblocked (light detected)      True
    Door Closed     Blocked (no light detected)     False
"""
import neopixel
from machine import Pin

# Pin configuration
optocoupler_pin = Pin(4, Pin.IN, Pin.PULL_UP)  # GPIO4 (D2) for the optocoupler
led_strip_pin = Pin(5)  # GPIO5 (D1) for the WS2812 LED strip

# Number of WS2812 LEDs in the strip
num_leds = 55

# Initialize the WS2812 LED strip
led_strip = neopixel.NeoPixel(led_strip_pin, num_leds)

OFF = (0, 0, 0)
ON = (255, 255, 255)


# Function to control the LED strip based on optocoupler state
def control_led_strip(optocoupler_state):
    """
    Take the state value of an Opto-Coupler and set LED strip values accordingly

    :param optocoupler_state: Either True or False
    :type optocoupler_state: bool
    :return: Nothing
    :rtype: None
    """
    if optocoupler_state:
        # Door open - Unblocked, light detected
        led_strip.fill(ON)
    else:
        # Door closed - Blocked, no light detected
        led_strip.fill(OFF)

    # Update the LED strip
    led_strip.write()


# Main loop
while True:
    # Read the state of the optocoupler
    state = bool(optocoupler_pin.value())

    # Control the LED strip based on the optocoupler state
    control_led_strip(state)
