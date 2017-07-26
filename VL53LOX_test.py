from VL53LOX import *

snsr = VL553LOX()

print("Revision ID: " + hex(snsr.revision()))
print("Device ID: " + hex(snsr.id()))
val1 = snsr.preRange()
decd = VL53L0X_decode_vcsel_period(val1)
print("Pre-Range Config Period: " + hex(val1) + " decode: " + str(decd))


val2 = snsr.finalRange()
decd2 = VL53L0X_decode_vcsel_period(val2)
print("Final Range Config Period: " + hex(val2) + " decode: " + str(decd2))

print(snsr.distance())
