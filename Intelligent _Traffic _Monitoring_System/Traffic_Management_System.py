import cv2
import torch
import numpy as np
import easyocr

# Load YOLOv5 model from torch hub with CUDA if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = torch.hub.load('ultralytics/yolov5', 'yolov5s').to(device)

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Load classes
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

def detect_objects(frame):
    results = model(frame)
    boxes = results.xyxy[0].cpu().numpy()  # x1, y1, x2, y2, confidence, class
    class_ids = boxes[:, 5].astype(int)
    confidences = boxes[:, 4]
    boxes = boxes[:, :4].astype(int)
    return boxes, confidences, class_ids

def draw_labels(boxes, confidences, class_ids, frame):
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        x1, y1, x2, y2 = box
        label = str(classes[class_id])
        color = (0, 255, 0)  # Green for detection
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Extract the detected object and run EasyOCR for license plate recognition
        if label in ["car", "truck", "bus", "motorbike"]:  # You can add other vehicle types if needed
            detected_object = frame[y1:y2, x1:x2]
            results = reader.readtext(detected_object)
            for (bbox, text, prob) in results:
                (top_left, top_right, bottom_right, bottom_left) = bbox

                # Adjust OCR coordinates to the original frame coordinates
                top_left = (int(top_left[0] + x1), int(top_left[1] + y1))
                bottom_right = (int(bottom_right[0] + x1), int(bottom_right[1] + y1))

                cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)
                cv2.putText(frame, f"Plate: {text} ({prob:.2f})", (top_left[0], top_left[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame

# Process video feed
cap = cv2.VideoCapture("traffic_video2.mp4")  # Replace with 0 for webcam

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
skip_frames = 30  # Number of frames to skip
resize_factor = 0.5  # Factor to resize the frame for faster processing

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (int(frame.shape[1] * resize_factor), int(frame.shape[0] * resize_factor)))

    # Perform detection every skip_frames frames
    if frame_count % skip_frames == 0:
        boxes, confidences, class_ids = detect_objects(frame)
    frame = draw_labels(boxes, confidences, class_ids, frame)

    cv2.imshow("Traffic Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
