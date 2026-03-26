import sys
import threading

try:
    import serial
    import serial.tools.list_ports
except ImportError:
    print("Error: pyserial not installed. Try pip install pyserial")
    sys.exit(1)


def list_ports():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No COM-Ports found.")
        return []

    print("\nCOM-Ports:")
    for i, p in enumerate(ports):
        print(f"[{i}] {p.device}")
    return ports


def choose_port(ports):
    while True:
        choice = input("Select Port: ")
        if choice.isdigit() and int(choice) < len(ports):
            return ports[int(choice)].device
        print("Invalid Input")


def choose_baud():
    while True:
        baud = input("Baudrate (e.g. 115200): ")
        if baud.isdigit():
            return int(baud)
        print("Unknown Baudrate")


def reader(ser):
    while True:
        try:
            line = ser.readline()
            if line:
                try:
                    print(line.decode(errors="ignore"), end="")
                except:
                    print(line)
        except:
            break


def writer(ser):
    while True:
        try:
            msg = input()
            ser.write((msg + "\n").encode())
        except:
            break


def main():
    ports = list_ports()
    if not ports:
        return

    port = choose_port(ports)
    baud = choose_baud()

    try:
        ser = serial.Serial(port, baud, timeout=1)
        print(f"Connected with {port} @ {baud}")
    except Exception as e:
        print("Connection Error:", e)
        return

    t1 = threading.Thread(target=reader, args=(ser,), daemon=True)
    t2 = threading.Thread(target=writer, args=(ser,), daemon=True)

    t1.start()
    t2.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nClose")
        ser.close()


if __name__ == "__main__":
    main()
