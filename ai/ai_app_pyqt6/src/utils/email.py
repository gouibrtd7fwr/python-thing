import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PySide6.QtCore import QThread, Signal

smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_gmail = "your_mail@gmail.com"
sender_password = "your_password_here" # -> google account -> app passwords
receiver_gmail = "receiver_mail@gmail.com"

class EmailThread(QThread):
    finished_signal = Signal(bool, str)

    def __init__(self, image_path, detection_info, parent = None):
        super().__init__(parent)
        self.image_path = image_path
        self.detection_info = detection_info
    
    def run(self):
        if not os.path.exists(self.image_path):
            self.finished_signal.emit(False, "Image file not found")
            return
        
        try:
            msg = MIMEMultipart()
            msg['Subject'] = "Alert from Python"
            msg['From'] = sender_gmail
            msg['To'] = receiver_gmail

            body_text = f"Python has detected unusual activities on your feed. Object detected: {self.detection_info}"
            msg.attach(MIMEText(body_text, 'plain'))

            with open(self.image_path, 'rb') as f:
                img_data = f.read()
                image = MIMEImage(img_data, name=os.path.basename(self.image_path))
                msg.attach(image)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(sender_gmail, sender_password)
                server.send_message(msg)

            self.finished_signal = (True, 'Email sent successfully.')

        except Exception as e:
            self.finished_signal = (False, f'Email failed. Exception: {e}')