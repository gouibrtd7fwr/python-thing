from PySide6.QtCore import QThread, Signal
import numpy as np
import cv2
from .simple_detection import SimpleDetection
# self.video_thread.detection_signal.connect(self.update_image)

class DetectionThread(QThread):
    detection_result_signal = Signal(list)
    def __init__(self, model_path, video_thread_instance, parent = None):
        super().__init__(parent)
        self.video_thread_instance = video_thread_instance
        self.detection_module = SimpleDetection(model_path)
        self.video_thread_instance.detection_signal.connect(self.run)
        
    def run(self, input_nd_array):
        result = self.detection_module.detect_object_from_nparray(input_nd_array)
        self.detection_result_signal.emit(result)
        return

    def stop(self):
        pass