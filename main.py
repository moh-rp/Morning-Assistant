import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QColor, QPalette, QIcon
from PyQt6.QtCore import Qt
from utils.weather_info import get_current_temp

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morning Assistant")
        self.setFixedSize(1280, 720)

        # Set color palette
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#070F2B"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#9290C3"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#1B1A55"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#9290C3"))
        self.setPalette(palette)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel("Morning Assistant")
        header.setStyleSheet("font-size: 48px; font-weight: bold; color: #9290C3; margin-bottom: 20px;")
        header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(header)

        # Boxes layout
        boxes_layout = QHBoxLayout()
        boxes_layout.setSpacing(20)

        # Wardrobe section
        wardrobe_section = QVBoxLayout()
        wardrobe_label = QLabel("Wardrobe")
        wardrobe_label.setStyleSheet("font-size: 24px; color: #9290C3; margin-bottom: 10px;")
        wardrobe_section.addWidget(wardrobe_label)

        wardrobe_widget = QWidget()
        wardrobe_widget.setStyleSheet("""
            background-color: #1B1A55;
            border-radius: 15px;
            padding: 20px;
        """)
        wardrobe_widget.setFixedHeight(500)
        wardrobe_layout = QVBoxLayout(wardrobe_widget)

        # Improved Add button
        add_button = QPushButton("Manage")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #535C91;
                color: #9290C3;
                border-radius: 20px;
                font-size: 18px;
                font-weight: bold;
                padding: 0px;
                width: 40px;
                height: 40px;
            }
            QPushButton:hover {
                background-color: #9290C3;
                color: #535C91;
            }
            QPushButton:pressed {
                background-color: #070F2B;
                color: #9290C3;
            }
        """)

        add_button.setFixedSize(120, 40)
        add_button.clicked.connect(self.on_add_clicked)
        wardrobe_layout.addWidget(add_button, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        wardrobe_section.addWidget(wardrobe_widget)
        boxes_layout.addLayout(wardrobe_section)

        # Weather and Outfit Recommendations section
        weather_outfit_section = QVBoxLayout()
        
        # Weather subsection
        weather_label = QLabel("Weather")
        weather_label.setStyleSheet("font-size: 24px; color: #9290C3; margin-bottom: 10px;")
        weather_outfit_section.addWidget(weather_label)

        weather_widget = QWidget()
        weather_widget.setStyleSheet("""
            background-color: #1B1A55;
            border-radius: 15px;
            padding: 20px;
        """)
        weather_widget.setFixedHeight(150)
        weather_outfit_section.addWidget(weather_widget)

        # Outfit Recommendations subsection
        outfit_label = QLabel("Outfit Recommendations")
        outfit_label.setStyleSheet("font-size: 24px; color: #9290C3; margin-bottom: 10px; margin-top: 20px;")
        weather_outfit_section.addWidget(outfit_label)

        outfit_widget = QWidget()
        outfit_widget.setStyleSheet("""
            background-color: #1B1A55;
            border-radius: 15px;
            padding: 20px;
        """)
        outfit_widget.setFixedHeight(250)
        weather_outfit_section.addWidget(outfit_widget)

        # Add a spacer to push the weather and outfit boxes to the top
        weather_outfit_section.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        boxes_layout.addLayout(weather_outfit_section)

        main_layout.addLayout(boxes_layout)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_add_clicked(self):
        print("Add button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())