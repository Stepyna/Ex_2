import sys
import io
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.FileIO("Ui.ui")
        uic.loadUi(f, self)
        self.setMouseTracking(True)
        self.run()

    def run(self):
        self.setFixedSize(800, 500)
        self.pushButton.clicked.connect(self.button_is_pushed)
        self.do_paint = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.do_paint:
            coordx = random.uniform(100, 700)
            coordy = random.uniform(100, 300)
            side = random.uniform(20, 200)
            r = 255
            g = 255
            b = 0
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(QPointF(coordx, coordy), side, side)
            self.do_paint = False
        self.do_paint = False
        qp.end()

    def button_is_pushed(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())