from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class RibbonFileMenu(QWidget):
    def __init__(self):
        super().__init__()
        # Create a horizontal layout for the entire file menu
        main_layout = QHBoxLayout(self)
        
        # Create a vertical layout for the sidebar buttons
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Placeholder buttons with larger touch-friendly size
        buttons = [
            "New", "Open", "Save", "Save As", 
            "Print", "Close", "Exit"
        ]
        
        # Create buttons in the sidebar with touch-optimized styling
        for button_text in buttons:
            btn = QPushButton(button_text)
            btn.setMinimumHeight(50)  # Larger touch target
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding-left: 10px;
                    border: none;
                    border-bottom: 1px solid #e0e0e0;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            sidebar_layout.addWidget(btn)
        
        # Create an empty widget for the right side
        empty_widget = QWidget()
        
        # Add sidebar layout and empty widget to main layout
        main_layout.addLayout(sidebar_layout)
        main_layout.addWidget(empty_widget)
        
        # Set stretch factors to give more space to the empty widget
        main_layout.setStretchFactor(sidebar_layout, 1)
        main_layout.setStretchFactor(empty_widget, 3)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabbed Window")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        
        # Create tab widget with fixed height
        self.tabs = QTabWidget()
        self.tabs.setFixedHeight(75)
        
        # Create main section
        self.main_section = QWidget()
        main_section_layout = QVBoxLayout(self.main_section)
        main_section_layout.addWidget(QLabel("Main Section"))

        # Add widgets to main layout
        main_layout.addWidget(self.tabs)
        main_layout.addWidget(self.main_section)
        
        # Set central widget
        self.setCentralWidget(central_widget)

        # Disable tab rearranging and closing
        self.tabs.setMovable(False)
        self.tabs.setTabsClosable(False)

        # Create tabs
        self.file_menu = RibbonFileMenu()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs to tab widget
        self.tabs.addTab(self.file_menu, "File")
        self.tabs.addTab(self.tab1, "Home")
        self.tabs.addTab(self.tab2, "Insert")
        
        # Set default tab
        self.tabs.setCurrentIndex(1)

        # Connect tab change event
        self.tabs.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        # If "File" tab is selected, make it take up entire window
        if self.tabs.tabText(index) == "File":
            self.tabs.setFixedHeight(self.height())
        else:
            self.tabs.setFixedHeight(75)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
