#import RPi.GPIO as GPIO
import time

#This .py initializes the gpio pins (all inputs) and prints its values to the terminal
#It also saves the value of each pin in a dictionary with the format [GPIOXX:'0' OR '1'] where XX is the GPIOXX number

GPIOValuesDict = {"GPIO17":[],"GPIO27":[],"GPIO22":[],"GPIO5":[],"GPIO6":[],"GPIO13":[],"GPIO19":[],"GPIO26":[],"GPIO18":[],
"GPIO23":[],"GPIO24":[],"GPIO25":[],"GPIO8":[],"GPIO7":[],"GPIO12":[],"GPIO16":[],"GPIO20":[],"GPIO21":[]};

#SECONDARY DICTIONARY to know what each pin does mean in the sense of the project

GPIONamesDict = {"GPIO17":["SORTIDA COMPROVADOR 11-16V"],
                 "GPIO27":[""],
                 "GPIO22":[""],
                 "GPIO5":[""],
                 "GPIO6":[""],
                 "GPIO13":[""],
                 "GPIO19":[""],
                 "GPIO26":[""],
                 "GPIO18":[""],
                 "GPIO23":[""],
                 "GPIO24":[""],
                 "GPIO25":[""],
                 "GPIO8":[""],
                 "GPIO7":[""],
                 "GPIO12":[""],
                 "GPIO16":[""],
                 "GPIO20":[""],
                 "GPIO21":[""]};

def setup_gpio():
    GPIO.setmode(GPIO.BCM)  # Set the mode to use GPIO numbers
    gpio_pins = [17, 27, 22, 5, 6, 13, 19, 26, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
    #14, 15 are rx & tx of canhat (could be used if necessary)
    #physical pins[GP17-> 11] [GP27-> 13] [GP22-> 15]      [GPIOPIN -> PHYSICAL PIN ON THE RASPBERRY]
    # ODDS        [GP5-> 29] [GP6-> 31] [GP13-> 33]
    #             [GP19-> 35] [GP26-> 37] 
    #            
    # EVENS       [GP18-> 12]
    #             [GP23-> 16] [GP24-> 18] [GP25-> 22]
    #             [GP8-> 24] [GP7-> 26] [GP12-> 32]
    #             [GP16-> 36] [GP20-> 38] [GP21-> 40]
   
    for pin in gpio_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return gpio_pins

def check_gpio_states(gpio_pins):
    for pin in gpio_pins:
        input_state = GPIO.input(pin)
        GPIOValuesDict[f"GPIO{pin}"].append(input_state)  #We write the GPIO value to its corresponding key-value pair 
        if input_state:
            print(f"Pin {pin} is HIGH,")
        else:
            print(f"Pin {pin} is LOW")

    
gpio_pins_setup = setup_gpio()

try:
    while True:
        check_gpio_states(gpio_pins_setup)
        time.sleep(10)  # Sleep for 10 seconds

except KeyboardInterrupt:  # Stop the loop with Ctrl+C
    print("\nExiting...")
    GPIO.cleanup()