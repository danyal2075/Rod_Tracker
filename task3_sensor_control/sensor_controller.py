try:
    from .fake_gpio import GPIO  # For running app
except ImportError:
    from fake_gpio import GPIO  # For running main
#import RPi.GPIO as GPIO # For testing in Raspberry Pi


import statistics
import time
import numpy as np
from statistics import median


class SensorController:

    def __init__(self):
        self.PIN_TRIGGER = 18  # do not change
        self.PIN_ECHO = 24  # do not change
        self.distance = None
        self.med = 0
        #self.arr_20 = np.zeros(20)
        self.color_from_distance = [False, False, False]
        print('Sensor controller initiated')

    def track_rod(self):
        for i in range(50):
           # print("experiment number....",i)
            arr_20 = np.zeros(20)
            counter = 0
            #print("counter....",counter)
            while (counter!=20):
                GPIO.setmode(GPIO.BCM)
                # SETUP PINS AS INPUT AND OUTPUT
                GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
                GPIO.setup(self.PIN_ECHO, GPIO.IN)
                # settling the sensor
                GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
                time.sleep(2)

        # triggering the sensor
                GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

                pulse_start_time = 0
                pulse_end_time = 0
       

                while GPIO.input(self.PIN_ECHO) == 0:
                    pulse_start_time = time.time()
                while GPIO.input(self.PIN_ECHO) == 1:
                    pulse_end_time = time.time()
        # Calculating the time
                pulse_duration = pulse_end_time - pulse_start_time
               # print("pulse duration---", pulse_duration)
                d = round(pulse_duration * 17150, 2)
                #print("d.....", d)
            
            
                arr_20[counter]=d
            
                counter = counter+1
                #print("arr=", arr_20)
            # arr.append(d)
                
                if (counter==20):
                    med=statistics.median(arr_20)
                   # print("median.....",med)
                    self.distance = med
                    print("Distance:", self.distance, "cm")
        return self.distance    
        # print('Monitoring')

    def get_distance(self):
        return self.distance

    def get_color_from_distance(self):
        med_value=self.distance
        if (med_value>=14 and med_value<=20):
            self.color_from_distance = [True, False, False]
        elif (med_value>=9 and med_value<=14):
            self.color_from_distance = [False, True, False]
        elif (med_value>=4 and med_value<=9):
            self.color_from_distance = [False, False, True]
        elif (med_value>=8 and  med_value<=10):
            self.color_from_distance = [False, True, True]
        elif (med_value>=13 and med_value<=15):
            self.color_from_distance = [True, True, False]
        
        
        return self.color_from_distance

 
