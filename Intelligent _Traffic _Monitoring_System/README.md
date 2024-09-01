# Traffic Monitoring and License Plate Recognition

## Project Background

This project is a Python-based application that uses the YOLOv5 model for real-time object detection, specifically focusing on vehicles in a traffic video. It integrates EasyOCR to recognize and extract license plate text from detected vehicles. The application is capable of detecting objects such as cars, trucks, buses, and motorbikes, and highlights license plates within the detected regions.

### Features
- **Real-time Object Detection:** Utilizes the YOLOv5 model to detect vehicles and other objects in video frames.
- **License Plate Recognition:** Uses EasyOCR to read and display text from detected license plates.
- **Customizable:** Easily modify the classes to detect and recognize other objects or text.

## How to Run the Code

### Prerequisites
- Python 3.x
- PyTorch with CUDA support (optional for GPU acceleration)
- OpenCV
- EasyOCR
- YOLOv5 weights and `coco.names` file for class labels

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Somilya24/WNSProjects.git
   cd Intelligent_Traffic_Monitoring_System
2. **Install Required Packages:**
Install the required Python libraries using pip:

    ```bash
    pip install torch torchvision opencv-python easyocr
3. **Download YOLOv5 Weights:**
The YOLOv5 model weights are loaded automatically using Torch Hub, but make sure your environment is properly configured to access the `ultralytics/yolov5` repository.

4. **Prepare coco.names:**
Ensure you have the `coco.names` file in your project directory, which contains the class labels.

5. **Run the Application:**
Execute the script using Python:

    ```bash
    python Traffic_Management_System.py

## Usage
1. **Process Video Feed:**
By default, the application processes a video file (`traffic_video2.mp4`). Replace this with `0` in `cv2.VideoCapture()` to use a webcam feed.
The application will detect objects every `skip_frames` frames and display the video with bounding boxes and recognized license plates.

2. **Customize Classes:**
You can add or modify the object classes for which you want to enable license plate recognition by editing the `label` check in the `draw_labels` function.

## Code Overview

### 1. Imports

- **`cv2`**: OpenCV library for video capture and image processing.
- **`torch`**: PyTorch library for deep learning, used to load the YOLOv5 model.
- **`numpy`**: Library for numerical operations and handling arrays.
- **`easyocr`**: Library for Optical Character Recognition (OCR), used to read text from detected objects (e.g., license plates).

### 2. Model and Device Initialization

- **`device`**: Determines if GPU (`cuda`) or CPU should be used for model inference.
- **`model`**: Loads the YOLOv5 model from PyTorch Hub and moves it to the selected device.
- **`reader`**: Initializes EasyOCR for English (`en`) to perform OCR on detected objects.

### 3. Loading Classes

- **`classes`**: Loads class names from the `coco.names` file, allowing the application to map detected object IDs to labels.

### 4. Functions

- **`detect_objects(frame)`**:
  - **Purpose**: Detects objects in a video frame using YOLOv5.
  - **Parameters**: `frame` - The current video frame.
  - **Operation**:
    - Performs detection on the frame.
    - Extracts and returns bounding boxes, confidence scores, and class IDs.

- **`draw_labels(boxes, confidences, class_ids, frame)`**:
  - **Purpose**: Draws bounding boxes and labels on detected objects.
  - **Parameters**: `boxes`, `confidences`, `class_ids`, `frame`.
  - **Operation**:
    - Draws bounding boxes and labels for each detected object.
    - If the object is a vehicle, extracts the region and runs OCR to identify text (e.g., license plates).
    - Returns the frame with drawn labels and OCR results.

### 5. Video Processing

- **`cap`**: Captures video from a file or webcam using OpenCV.
- **Frame Processing Loop**:
  - Reads and resizes frames for faster processing.
  - Detects objects every few frames.
  - Draws labels and OCR results.
  - Displays the processed frame.
  - Exits on 'q' key press.

### 6. Cleanup

- Releases the video capture object and closes all OpenCV windows upon application exit.


## Example Screenshots
1. Object Detection and License Plate Recognition
This screenshot shows the application detecting vehicles and license plate in a traffic video and drawing bounding boxes around them.

![Screenshot (523)](https://github.com/user-attachments/assets/868bb235-cde7-4e17-b803-d0166952f313)

## Important Notes
1. **Performance:** For real-time performance, it is recommended to use a GPU-enabled environment with CUDA support.
2. **Video Processing:** Adjust skip_frames and resize_factor based on your hardware capabilities and processing requirements.

## Conclusion
This application provides an efficient solution for monitoring traffic and recognizing license plates in real-time. It leverages state-of-the-art object detection and OCR technologies, making it a valuable tool for traffic analysis and surveillance.
