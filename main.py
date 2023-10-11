from machine import Pin
import neopixel

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
    if optocoupler_state:  # Door open - Light detected on OptoCoupler
        led_strip.fill(ON)
    else:
        led_strip.fill(OFF)  # Door closed - No light detected on OptoCoupler

    # Update the LED strip
    led_strip.write()


# Main loop
while True:
    # Read the state of the optocoupler
    state = bool(optocoupler_pin.value())

    # Control the LED strip based on the optocoupler state
    control_led_strip(state)
