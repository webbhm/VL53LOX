# VL53LOX
Python code to read the VL53LOX time-of-flight laser distance sensor

This code provides an object that reads the I2C sensor in pure Python code.  ID, Revision and range configuration information is available as attributes, along with distance (in mm units).

smbus and time need to be imported to support this code.

This code works with the sensor from Adafruit and similar clones.
