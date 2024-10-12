import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QColor
from utils.weather_info import get_current_temp


class MorningAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Morning Assistant')
        self.setGeometry(100, 100, 800, 600)

        weather = f"{get_current_temp()}°"
        
        weatherbox = QVBoxLayout()
        weatherbox.addWidget(QLabel(f"Current weather: {weather}"))
        container = QWidget()
        container.setLayout(weatherbox)
        self.setCentralWidget(container)

def main():
    app = QApplication(sys.argv)
    window = MorningAssistant()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
