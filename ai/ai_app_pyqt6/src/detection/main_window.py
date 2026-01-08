from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QHBoxLayout, QFileDialog
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QImage
from .components.checkable_combo_box import CheckableComboBox
from .watch_thread import WatchThread
import json
import itertools

class MainWindow(QMainWindow):
    filter_detection_signal = Signal(list)
    def __init__(self):
        super().__init__()

        self.video_thread = None
        self.setWindowTitle("My App")
        self.button_layout = QVBoxLayout()
        self.insert_file_btn = QPushButton('Upload video')
        self.insert_file_btn.setFixedSize(200, 75)
      
        self.button_layout.addWidget(self.insert_file_btn)

        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignVCenter)

        self.preview = QLabel('Preview of the video')
        self.preview.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.preview.setPixmap(QPixmap("ai/ai_app_pyqt6/thing.png"))

        main_scrn_layout = QHBoxLayout()

        main_scrn_layout.addWidget(self.preview)
        main_scrn_layout.addLayout(self.button_layout)

        widget = QWidget()
        widget.setLayout(main_scrn_layout)
        self.setCentralWidget(widget)

        # connections
        self.insert_file_btn.clicked.connect(self.open_file)

        self.load_from_json('/home/tommy/Documents/GitHub/python-thing/ai/ai_app_pyqt6/src/data/detection_module.json')
        check_combobox_layout = self.update_combo_box()
        self.button_layout.addLayout(check_combobox_layout)

        self.check_filter = QPushButton('Filter')
        self.check_filter.clicked.connect(self.collect_category_data)
        self.button_layout.addWidget(self.check_filter)


    def update_image(self, image):
        h, w, ch = image.shape
        bytes_per_line = ch * w
        qt_image = QImage(image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        qt_pixmap = QPixmap.fromImage(qt_image)

        scale_pixmap = qt_pixmap.scaled(self.preview.size(),
                                         Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
        self.preview.setPixmap(scale_pixmap)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
    "Open Video", "", "Video Files (*.mp4 *.mov *.avi *.wmv *.mkv)")
        if file_path:
            self.stop_cur_thread()
            self.video_thread = WatchThread(file_path, self)
            self.video_thread.change_pixmap_signal.connect(self.update_image)
            self.video_thread.start()

    def stop_cur_thread(self):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.terminate()
            self.video_thread.wait()

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf8') as file:
                data = json.load(file)
            self.detection_categories = data
        except Exception as e:
            print(e)

    def update_combo_box(self):
        return_layout = QVBoxLayout()
        self.combo_box_instances = []
        for key, val in self.detection_categories.items():
            module_name = str(key).replace("_", " ")
            module_name = module_name.capitalize()

            tmp_combo_box = CheckableComboBox()
            tmp_text_box = QLabel(text=module_name)
            tmp_layout = QHBoxLayout()

            tmp_layout.addWidget(tmp_text_box)
            tmp_layout.addWidget(tmp_combo_box)

            return_layout.addLayout(tmp_layout)

            list_of_names = list(val.keys())
            list_of_values = list(val.values())
            tmp_combo_box.addItems(list_of_names, list_of_values)

            self.combo_box_instances.append(tmp_combo_box)
        return return_layout
    
    def collect_category_data(self):
        tmp_category_value = []

        for instance in self.combo_box_instances:
            tmp_category_value.append(instance.currentData())
        filters = return_category_value = list(itertools.chain.from_iterable(tmp_category_value))
        print(filters)
        self.filter_detection_signal.emit(filters)
        return return_category_value
