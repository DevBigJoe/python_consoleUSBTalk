# ESP Serial Console (Python)

A lightweight Python-based serial console for communicating with an ESP (e.g. ESP32 / ESP8266) over a COM port.
Designed to behave similarly to the Arduino IDE Serial Monitor, but kept minimal and terminal-based.

---

##  Features

* Lists all available serial (COM) ports
* Lets you select the port interactively
* Prompts for custom baud rate (e.g. 9600, 115200)
* Full-duplex communication:

  * Send messages from keyboard
  * Receive data from the ESP in real time
* Simple and clean terminal interface
* Minimal dependencies

---

##  Requirements

* Python 3.x
* `pyserial` (only external dependency)

Install it with:

```bash
pip install pyserial
```

---

##  Usage

1. Connect your ESP device via USB
2. Run the script:

```bash
python serial_console.py
```

3. Follow the prompts:

   * Select a COM port from the list
   * Enter the baud rate (must match your ESP code)

4. Start typing to send data
   Incoming messages from the ESP will appear automatically

---

##  How It Works

The program uses two threads:

* **Reader Thread**

  * Continuously reads incoming serial data
  * Prints it to the console in real time

* **Writer Thread**

  * Waits for user input
  * Sends entered text to the ESP

This allows simultaneous sending and receiving, similar to professional serial monitors.

---

##  Notes

* Baud rate must match the one defined in your ESP firmware (`Serial.begin(...)`)
* Line endings are automatically set to `\\n`
* Works on Windows, Linux, and macOS

---

##  Possible Improvements

* Selectable line endings (CR / LF / CRLF)
* Timestamp display
* Logging output to file
* GUI version (e.g. with Tkinter or PyQt)
* Auto-reconnect on disconnect

---

##  License

Free to use and modify.
