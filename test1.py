import asyncio
import serial

serial0 = '/dev/ttyUSB0'
serial1 = '/dev/ttyUSB1'

async def read_serial(serial_port):
    while True:
        if serial_port.in_waiting:
            data = serial_port.readline().decode().strip()
            print(f"Data from {serial_port.name}: {data}")

async def main():
    # Open the serial ports
    serial_port1 = serial.Serial(serial0, baudrate=9600, timeout=0)
    serial_port2 = serial.Serial(serial1, baudrate=9600, timeout=0)

    # Create tasks to read from each serial port asynchronously
    task1 = asyncio.create_task(read_serial(serial_port1))
    task2 = asyncio.create_task(read_serial(serial_port2))

    # Wait for both tasks to complete
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
