from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QHBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from .watch_thread import WatchThread

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.video_thread = None
        self.setWindowTitle("My App")
        self.button_layout = QVBoxLayout()
        self.insert_file_btn = QPushButton('Upload video')
        self.insert_file_btn.setFixedSize(200, 75)
        self.detector_btn = QPushButton('Analyze')
        self.detector_btn.setFixedSize(200, 75)
        
        self.button_layout.addWidget(self.insert_file_btn)
        self.button_layout.addWidget(self.detector_btn)
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
            self.video_thread = WatchThread(file_path)
            self.video_thread.change_pixmap_signal.connect(self.update_image)
            self.video_thread.start()

    def stop_cur_thread(self):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.terminate()
            self.video_thread.wait()