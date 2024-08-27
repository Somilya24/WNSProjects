# Real-Time Object Detection with YOLO

## Project Background

This project demonstrates a real-time object detection application using the YOLO (You Only Look Once) algorithm. The project uses OpenCV and Flask to capture live video from the webcam, perform object detection on each frame, and display the results in a web browser.

YOLO is a state-of-the-art object detection algorithm that can identify objects in images and videos with high accuracy and speed. This project integrates YOLO with a Flask web server to provide a simple and interactive interface for real-time object detection.

## How to Run the Code

### Prerequisites

- Python 3.x
- OpenCV
- Flask
- YOLOv3 weights and configuration files
- COCO dataset names

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Somilya24/WNSProjects.git
   cd Real_Time_Object_Detection

2. **Install Required Python Packages**

   Make sure you have pip installed. Then, install the necessary packages:
      ```bash
      pip install -r requirements.txt
      ```
   If you don't have a requirements.txt file, manually install the required packages:
   
   ```bash
    pip install flask opencv-python-headless numpy
      ```
3. **Download YOLO Weights and Configuration**

Download the `yolov3.weights`, `yolov3.cfg` and `coco.names` files:

- YOLOv3 Weights
- YOLOv3 Configuration
- COCO Names

Save these files in a folder named `yolo` inside your project directory.

4. **Run the Flask Application**

Navigate to your project directory and run the Flask application:

   ```bash
python ObjectDetectionAPI.py
```

5. **Access the Web Application**

Open your web browser and go to `http://127.0.0.1:5000/` to access the real-time object detection interface.

## Post-Run Example Screenshots
Below are some example screenshots of the application in action, along with commentary:

1. Initial Interface
![Screenshot (528)](https://github.com/user-attachments/assets/73475c69-0516-42d4-9c2f-f195bf3706b0)

Description: This is the landing page of the application, where the live feed from the webcam is displayed.

3. Object Detection in Action
![Screenshot (530)](https://github.com/user-attachments/assets/1cdb9f35-ed72-432a-a13c-d00d495fd4ed)

Description: The application detects objects in real-time. Here, it identifies and labels various objects in the frame, such as "person," "chair," etc., with bounding boxes.

## Conclusion
This project showcases how to build a simple yet effective real-time object detection system using YOLO and Flask. The code can be extended for more advanced applications, such as integrating with different cameras, adding more detection classes, or deploying the app on a web server for remote access.
