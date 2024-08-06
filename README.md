# 🚗 Smart Parking Assistant 🚗

![Smart parking assitant](https://github.com/user-attachments/assets/2f5b9c30-dca9-4eb6-8bda-0e5984f3cf11)

## Overview
Smart Parking Assistant is an IoT-based project that uses Arduino and multiple IR sensors to detect available parking spots and provide real-time recommendations to drivers. This system aims to optimize parking space utilization and reduce the time spent searching for parking spots.

## Project working video link 📷:
![Smart parking assistant working youtube link](https://youtube.com/shorts/WhS6OFOso_8?feature=share)

## Features 🌟
- 📡 Real-time monitoring of up to 10 parking spots
- 🖥️ User-friendly GUI for easy visualization of parking spot availability
- 🤖 Intelligent recommendation system for optimal parking spot selection
- 🔌 Arduino-based sensor network for reliable detection
- 🔧 Customizable and expandable for various parking lot sizes

## Hardware Requirements 🛠️
- Arduino Uno
- 10 IR sensors
- Jumper wires approximately 2 sets of each Male-to-Male, Male-to-Female and Female-to-Female
- 1 Themisto TH-B830 Breadboards (or equivalent)
- USB cable for Arduino connection

## Software Requirements 💻
- Arduino IDE
- Python 3.x
- Required Python libraries:
  - pyserial
  - tkinter
  - Pillow
  - pyinstaller

## Hardware/Electrical connection:
- Basics of arduino uno: [https://www.youtube.com/watch?v=1ENiVwk8idM]
- Hardware usage of arduino uno: [https://youtu.be/bniUECtJkeU?si=gJBngS4IPTkPIYHg]
- How to use breadboard: [https://youtu.be/xXvGHVFpq7c?si=Mbgbi09CIosm5x7H]
- How to connect arduino uno to breadboard: [https://youtu.be/Ia7gkgSor78?si=nyLcDcYufpISQPkN]
- How to connect IR sensors to arduino uno/breadboard: [https://youtu.be/OMZacCLRt9A?si=FCeArz40iKxr-suy] 

## Installation 📝

1. 
A. Clone the repository:
   ```git clone https://github.com/Abhiz2411/smart-parking-assistant```
   
B. Change current working directory:
   ```cd smart-parking-assistant```

2. Set up the Arduino:
- Open the Arduino IDE
- Load the arduino_sketch.ino file
- Upload the sketch to your Arduino Uno

3. Install required Python libraries🐍:
- ```pip install pyserial pillow```
- ```pip install pyinstaller```

4. Configure the serial port: [https://youtu.be/D271p2E2_o4?si=WE6S4_mLvA8MvAFU]
- In parking_assistant.py, update the arduino_port variable with your Arduino's COM port

## Usage 🚀
## A. First use:
1. Ensure the Arduino is connected and the sketch is uploaded
2. Run the Python script: 
```python main.py```
3. The GUI will display the status of each parking spot and provide recommendations

## B. After first use:
1. Change current working directory to dist
2. Simply run `main.exe` executeable file

## Project Structure 📂
- arduino_sketch.ino: Arduino code for reading sensor data
- main.py: Main Python script for GUI and logic
- dist/main.exe: executable file of the project
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
- Project Link: https://github.com/Abhiz2411/smart-parking-assistant

## Acknowledgements 🙏
- Arduino[https://www.arduino.cc/]
- Python[https://www.python.org/]
- Tkinter[https://docs.python.org/3/library/tkinter.html]
- Pillow[https://python-pillow.org/]
