from PySide6.QtCore import QThread, Signal
import numpy as np
import cv2

class WatchThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self, video_path, parent = None):
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

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap:
            print('Error: Could not find video file')
            self._is_Running = False
            return
        while self._is_Running:
            ret, frame = cap.read()
            if not ret:
                print('Error: Could not process frame or end of video')
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            self.change_pixmap_signal.emit(frame)
            self.msleep(self.ms_delay)
        
        cap.release()