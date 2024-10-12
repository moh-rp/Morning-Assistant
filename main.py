import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MorningAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Morning Assistant')
        self.setGeometry(100, 100, 800, 600)

def main():
    app = QApplication(sys.argv)
    window = MorningAssistant()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
