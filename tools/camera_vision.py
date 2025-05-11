from ultralytics import YOLO
import cv2
import numpy as np
import colorsys
import os

def analyze_object_colors(image, xmin, ymin, xmax, ymax):
    object_region = image[int(ymin):int(ymax), int(xmin):int(xmax)]
    average_color = np.mean(object_region, axis=(0, 1))
    b, g, r = average_color
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return f"Ortalama BGR ({b:.2f}, {g:.2f}, {r:.2f}), HSV ({h:.2f}, {s:.2f}, {v:.2f})"

def camera_vision() -> str:
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Kamera açılamadı."

    ret, frame = cap.read()
    if not ret:
        return "Görüntü alınamadı."

    cv2.imwrite("camera_capture.jpg", frame)
    results = model(frame)

    object_info = ""
    for result in results[0].boxes.data:
        xmin, ymin, xmax, ymax, confidence, class_id = result
        label = results[0].names[int(class_id)]
        color_analysis = analyze_object_colors(frame, xmin, ymin, xmax, ymax)
        object_info += f"Nesne: {label} | Konum: ({xmin:.2f}, {ymin:.2f}) - ({xmax:.2f}, {ymax:.2f})\n"
        object_info += f"Renk Analizi: {color_analysis}\n\n"

    return object_info if object_info else "Nesne tespit edilmedi."