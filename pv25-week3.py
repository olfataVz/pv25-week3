import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Week 3 - F1D022057-Lalu Olfata Vedora Zurji")
        self.setGeometry(100, 100, 450, 300)
        
        self.label = QLabel("x: 0, y: 0", self)
        self.label.move(50, 50)
        self.label.setStyleSheet("font-size: 14px;")
        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
    
    def mouseMoveEvent(self, event):
        x, y = event.position().x(), event.position().y()
        self.label.setText(f"x: {int(x)}, y: {int(y)}")
    
    def enterEvent(self, event):
        self.moveLabelRandomly()
    
    def moveLabelRandomly(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec())
