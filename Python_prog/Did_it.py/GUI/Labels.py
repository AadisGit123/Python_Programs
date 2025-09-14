import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import  QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700, 300, 500, 500)#(x-coordinate, y-coordinate, width, height)

    label = QLabel("Hello", self)
    label.setFont(QFont("Arial", 30))
    label.setGeometry(0, 0, 500, 100)
    label.setStyleSheet("color: blue;"
                        "background-color: red;"
                        "font-weight: bold;"
                        "font-style: italic;"
                        "text-decoration: underline;")
    
    # label.setAlignment(Qt.AlignTop)#Vertical Top
    # label.setAlignment(Qt.AlignBottom)#Vertical Bottom
    # label.setAlignment(Qt.AlignVCenter)#Vertical Center
    
    # label.setAlignment(Qt.AlignRight)#Horizontal Right
    # label.setAlignment(Qt.AlignLeft)#Horizontal Left
    # label.setAlignment(Qt.AlignHCenter)#Horizontal Center
    label.setAlignment(Qt.AlignCenter)#Center Align

    
    # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)#CENTER & TOP
    # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)#CENTER & BOTTOM
    # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    
def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()