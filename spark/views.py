from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django. contrib.auth.models import User
from django.http import HttpResponse, StreamingHttpResponse
import cv2
import numpy as np
import threading
# Create your views here.

def home(request):
    return render(request, 'home.html')



# bambi/views.py
from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import numpy as np
import threading
import os

# Rutas a YOLO
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEIGHTS_PATH = os.path.join(BASE_DIR, 'yolov3.weights')
CONFIG_PATH = os.path.join(BASE_DIR, 'yolov3.cfg')

# Cargar YOLO
net = cv2.dnn.readNet(WEIGHTS_PATH, CONFIG_PATH)
layer_names = net.getLayerNames()
layer_indices = net.getUnconnectedOutLayers()
output_layers = [layer_names[i - 1] for i in layer_indices.flatten()]

# Variable global para conteo
estudiantes_contados = 0
lock = threading.Lock()

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 640)
        self.video.set(4, 480)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, daemon=True).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global estudiantes_contados
        image = self.frame
        height, width, _ = image.shape

        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        boxes = []
        confidences = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and class_id == 0:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        count = 0
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image, "Estudiante", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                count += 1

        with lock:
            estudiantes_contados = count

        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def home(request):
    global estudiantes_contados
    with lock:
        conteo = estudiantes_contados
    return render(request, 'home.html', {'conteo': conteo})


#control de camrra
from django.http import JsonResponse
def toggle_camera(request):
    if request.method == "POST":
        # Cambiar estado de cámara (activar/desactivar)
        global CAMERA_ACTIVE
        CAMERA_ACTIVE = not CAMERA_ACTIVE
        return JsonResponse({"status": "ok"})