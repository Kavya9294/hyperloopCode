import time
import board
import busio
import adafruit_tmp006

#Code for sensors communication



#Code for reading from SparkFun IMU Breakout: Sagarika



#Code for Writing to SparkFun IMU Breakout: Sagarika



#Code for Reading from 19MM DIGITAL OUTPUT PRESSURE SENSOR



#Code for Writing to 19MM DIGITAL OUTPUT PRESSURE SENSOR



#Code for Reading from MAX3186: Luiza



#Code for Writing to MAX31865: Luiza



#Code for Reading from TMP006 Contact-less Infrared Thermopile Sensor: Demitri

def get_temp_ncontact():
    # Define a function to convert celsius to fahrenheit.
    def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

    # Create library object using Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tmp006.TMP006(i2c)

    # Initialize communication with the sensor, using the defaul16 samples
    # This is the best accuracy but a little slower at reacting to changes.
    # The first sample will be meaningless
    while True:
        obj_temp = sensor.temperature
        print('Object temperature: {0:0.3F}*C / {1:0.3F}*F'.format(obj_temp, c_to_f(obj_temp)))
        time.sleep(5.0)




#Code to REad from ELEGOO HC-SR04: Alex



#Code to Write to ELEGOO HC-SR04: Alex 



#Code to read from 3202 Mini Spy Camera



#Code to Write to 3202 Mini Spy Camera



#Code to Read from the Pressure Sensor-



#Code to Write to the Pressure Sensor
