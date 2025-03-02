# ch 4.4.1 main.py
import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication

def main():
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()