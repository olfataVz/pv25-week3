import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt, QPoint

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Week 3 - F1D022057-Lalu Olfata Vedora Zurji")
        self.setGeometry(100, 100, 450, 300)
        
        self.label = QLabel("x: 0, y: 0", self)
        self.label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.label.move(50, 50)
        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.NoButton:
            x, y = event.position().toPoint().x(), event.position().toPoint().y()
            self.label.setText(f"x: {x}, y: {y}")
    
    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == event.Type.Enter:
            self.moveLabelRandomly()
        return super().eventFilter(obj, event)
    
    def moveLabelRandomly(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(QPoint(new_x, new_y))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.label.installEventFilter(window)
    window.show()
    sys.exit(app.exec())

