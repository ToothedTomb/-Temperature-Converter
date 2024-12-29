from PyQt5.QtWidgets import QApplication,QMessageBox, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMenuBar, QAction, QDialog, QVBoxLayout, QTextEdit, QWidget
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
  #  from PyQt5.QtWidgets import 

class TemperatureConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")

        # Heading
        self.heading_label = QLabel("Temperature Converter:", self)
        heading_font = QFont()
        heading_font.setPointSize(15)  # Set the font size
        heading_font.setBold(True)    # Make it bold
        heading_font.setUnderline(True)  # Underline the heading
        self.heading_label.setFont(heading_font)
        self.heading_label.setAlignment(Qt.AlignCenter)  # Center align the heading

        # Create widgets
        self.input_label = QLabel("Enter Temperature:", self)
        self.input_field = QLineEdit(self)

        self.conversion_type = QComboBox(self)
        self.conversion_type.addItems(["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

        self.convert_button = QPushButton("Convert", self)
        self.result_label = QLabel("", self)

        # Layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.heading_label)  # Add the heading label
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.conversion_type)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        self.setCentralWidget(central_widget)

        # Menu bar
        menubar = self.menuBar()
        menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        menu.addAction(about_action)
        about_action.triggered.connect(self.show_about_dialog)

        # Signals
        self.convert_button.clicked.connect(self.convert_temperature)

        # Set the window to be unresizable
        self.setFixedSize(self.sizeHint())

    def show_about_dialog(self):
        about_text = """
        <u><h1>Temperature Converter:</h1></u>
        <h3>Version: 2</h3>
        <h3>Built with PyQt5</h3>
        <h3>Developer: Jonathan Steadman</h3>
        """
        QMessageBox.about(self, "About", about_text)

    def convert_temperature(self):
        try:
            temp = float(self.input_field.text())
            if self.conversion_type.currentText() == "Celsius to Fahrenheit":
                result = (temp * 9/5) + 32
                self.result_label.setText(f"Result: {result:.2f} °F")
            else:
                result = (temp - 32) * 5/9
                self.result_label.setText(f"Result: {result:.2f} °C")
        except ValueError:
            self.result_label.setText("Error code 1: Enter a number.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())
