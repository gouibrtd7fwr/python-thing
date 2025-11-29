from ultralytics import YOLO

class SimpleDetection:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = YOLO(model_path)
    def detect_object_from_image(self, img_path):
        results = self.model(img_path)
        return results
    def detect_object_from_nparray(self, nd_array):
        results = self.model.predict(nd_array)
        print(results)
    