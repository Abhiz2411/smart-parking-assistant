# 🚗 Smart Parking Assistant 🚗

## Overview
Smart Parking Assistant is an IoT-based project that uses Arduino and multiple IR sensors to detect available parking spots and provide real-time recommendations to drivers. This system aims to optimize parking space utilization and reduce the time spent searching for parking spots.

## Features 🌟
- 📡 Real-time monitoring of up to 10 parking spots
- 🖥️ User-friendly GUI for easy visualization of parking spot availability
- 🤖 Intelligent recommendation system for optimal parking spot selection
- 🔌 Arduino-based sensor network for reliable detection
- 🔧 Customizable and expandable for various parking lot sizes

## Hardware Requirements 🛠️
- Arduino Uno
- 10 IR sensors
- Jumper wires
- 2 Themisto TH-B830 Breadboards (or equivalent)
- USB cable for Arduino connection

## Software Requirements 💻
- Arduino IDE
- Python 3.x
- Required Python libraries:
  - pyserial
  - tkinter
  - Pillow

## Installation 📝

1. Clone the repository:
   ```git clone https://github.com/yourusername/smart-parking-assistant.git```
   ```cd smart-parking-assistant```

2. Set up the Arduino:
- Open the Arduino IDE
- Load the arduino_sketch.ino file
- Upload the sketch to your Arduino Uno

3. Install required Python libraries🐍:
- ```pip install pyserial pillow```

4. Configure the serial port:
- In parking_assistant.py, update the arduino_port variable with your Arduino's COM port

## Usage 🚀
1. Ensure the Arduino is connected and the sketch is uploaded
2. Run the Python script: 
```python parking_assistant.py```
3. The GUI will display the status of each parking spot and provide recommendations

## Project Structure 📂
- arduino_sketch.ino: Arduino code for reading sensor data
- parking_assistant.py: Main Python script for GUI and logic
- images/: Directory containing icons and images for the GUI
- README.md: Project documentation

## Contributing 🤝
- Contributions to improve Smart Parking Assistant are welcome. Please follow these steps:
1) Fork the repository
2) Create a new branch (git checkout -b feature/AmazingFeature)
3) Commit your changes (git commit -m 'Add some AmazingFeature')
4) Push to the branch (git push origin feature/AmazingFeature)
5) Open a Pull Request

## License 📜
- Distributed under the MIT License. See LICENSE file for more information.

## Contact 📧
- Abhijit Zende - abhijitzende75@gmail.com
- Project Link: https://github.com/yourusername/smart-parking-assistant

## Acknowledgements 🙏
- Arduino[https://www.arduino.cc/]
- Python[https://www.python.org/]
- Tkinter[https://docs.python.org/3/library/tkinter.html]
- Pillow[https://python-pillow.org/]