from PySide6.QtCore import QThread, Signal
import numpy as np
import cv2
from .simple_detection import SimpleDetection
from .dataclass.detection_result import DetectionResult
# from .watch_thread import WatchThread
# from .main_window import MainWindow
# self.video_thread.detection_signal.connect(self.update_image)

class DetectionThread(QThread):
    detection_result_signal = Signal(DetectionResult)
    def __init__(self, model_path, video_thread_instance, parent = None):
        super().__init__(parent)
        self.video_thread_instance = video_thread_instance
        self.detection_module = SimpleDetection(model_path)
        self.video_thread_instance.detection_signal.connect(self.run)
        
    def run(self, input_nd_array):
        results = self.detection_module.detect_object_from_nparray(input_nd_array)
        # Process results and filter objects
        self.detection_result_signal.emit(DetectionResult(result=results, frame=input_nd_array))
        return

    def stop(self):
        pass