import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QPalette, QColor, QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button_layout = QVBoxLayout()
        insert_file_btn = QPushButton('Upload video')
        insert_file_btn.setFixedSize(200, 75)
        insert_file_btn.se
        detector_btn = QPushButton('Analyze')
        detector_btn.setFixedSize(200, 75)
        
        button_layout.addWidget(insert_file_btn)
        button_layout.addWidget(detector_btn)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignVCenter)

        preview = QLabel('Preview of the video')
        preview.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        preview.setPixmap(QPixmap("ai/ai_app_pyqt6/thing.png"))


        main_scrn_layout = QHBoxLayout()

        main_scrn_layout.addWidget(preview)
        main_scrn_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_scrn_layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()