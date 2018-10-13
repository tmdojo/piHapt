import board
import busio

from micropython import const
import adafruit_bus_device.i2c_device as i2c_device

_DRV2667_ADDRESS = const(0x59)

i2cbus = busio.I2C(board.SCL, board.SDA)
i2c = i2c_device.I2CDevice(i2cbus, _DRV2667_ADDRESS)

def read_register(register, length):
    i2c.write(bytes([register & 0xFF]))
    result = bytearray(length)
    i2c.readinto(result)
    #print("$%02X => %s" % (register, [hex(i) for i in result]))
    return result

def write_register_byte(register, value):
    i2c.write(bytes([register & 0xFF, value & 0xFF]))
    print("$%02X <= 0x%02X" % (register, value))

#Set to analog input mode
write_register_byte(0x02, 0x00) #Take device out of standby mode
write_register_byte(0x02, 0x02) #Set EN_OVERRIDE bit = boost and amplifier active
write_register_byte(0x01, 0x07) #Set to analog input + Gain 0-3 (0x04-0x07 25v-100v)
