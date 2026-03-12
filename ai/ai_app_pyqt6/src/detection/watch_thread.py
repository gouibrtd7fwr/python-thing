from PySide6.QtCore import QThread, Signal
import numpy as np
import cv2
from .detection_thread import DetectionThread
from ultralytics.utils.plotting import Annotator
from src.detection.dataclass.detection_result import DetectionResult
from src.utils.email import EmailThread
import time
from datetime import datetime

# self.video_thread.detection_signal.connect(self.update_image)

class WatchThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    detection_signal = Signal(np.ndarray)
    def __init__(self, video_path, main_window_instance, parent = None):
        super().__init__(parent)
        self.video_path = video_path
        self._is_Running = True

        cap = cv2.VideoCapture(self.video_path)
        if not cap:
            print('Error: Could not find video file')
            self._is_Running = False
            return
        
        self.fps = int(cap.get(cv2.CAP_PROP_FPS))
        self.ms_delay = int(1000/self.fps) if self.fps > 0 else 33
        cap.release()

        self.detection_thread = DetectionThread('models/yolo11m.pt', self)
        self.detection_thread.detection_result_signal.connect(self.trigger)

        self.main_window_instance = main_window_instance
        self.main_window_instance.filter_detection_signal.connect(self.filter_detection_data)
        self.main_window_instance.email_info_signal.connect(self.update_email_data)
        self.detection_filter = list()



        self.send = "truongminh3107@gmail.com"
        self.receiver = "truongminh9a7@gmail.com"
        self.app_password = "awrb fpat nbbt jvwm"
        self.email_data = [self.send, self.receiver, self.app_password]

        self.email_thread = None
        self.last_email_time = 0
        self.email_cooldown = 30

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap:
            print('Error: Could not find video file')
            self._is_Running = False
            return
        counter = 0
        while self._is_Running:
            ret, frame = cap.read()
            if not ret:
                print('Error: Could not process frame or end of video')
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            self.change_pixmap_signal.emit(frame)
            if counter >= self.fps * self.email_cooldown:
                self.detection_signal.emit(frame)
                counter = 0
            
            self.msleep(self.ms_delay)
            counter += 1
        cap.release()

    def stop(self):
        self._is_Running = False
        self.wait()

    def trigger(self, results: DetectionResult):
        detected_objects = []
        frame_modified = False

        for result in results.result:
            annotator = Annotator(results.frame)
            for box in result.boxes:
                if int(box.cls) in self.detection_filter:
                    coords = box.xyxy[0]
                    label = result.names[int(box.cls)]
                    annotator.box_label(coords, label)

                    detected_objects.append(label)
                    frame_modified = True

        if frame_modified:
            final_frame = annotator.result()
            time_stamp = datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d_%H-%M-%S")
            save_path = f'DetectionResults_{time_stamp}.png'
            
            cv2.imwrite(save_path, final_frame)

            current_time = time.time()
            if (current_time - self.last_email_time) > self.email_cooldown:
                self.send_email_notification(save_path, ','.join(set(detected_objects)), self.email_data)
                self.last_email_time = current_time

    def send_email_notification(self, image_path, labels, final_email_data: list):
        self.email_thread = EmailThread(image_path, labels, final_email_data[0], final_email_data[1], final_email_data[2])
        self.email_thread.finished_signal.connect(self.on_email_finished)
        self.email_thread.start()

    def on_email_finished(self, success, message):
        if success:
            print(f'Email sent successfully: {message}')
        else:
            print(f'Email failed to send: {message}')

    def filter_detection_data(self, data: list):
        self.detection_filter = data

    def update_email_data(self, data):
        self.email_data = data
        print("Email data stored:", self.email_data)