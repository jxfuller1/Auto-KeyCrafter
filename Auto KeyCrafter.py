import sys
import time
from typing import Dict, List
import keyboard
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QHBoxLayout, QApplication, QMainWindow, QDoubleSpinBox, \
    QLabel, QLineEdit, QPushButton, QLayout, QMessageBox, QAction, QDialog, QTabWidget


class Howtohotkey(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hotkey Help")

        layout = QVBoxLayout()

        myfont = QFont()
        myfont.setBold(True)
        myfont.setPointSize(12)
        howto_label = QLabel("How To Setup Hotkeys")
        howto_label.setFont(myfont)

        layout.addWidget(howto_label, alignment=Qt.AlignHCenter)
        layout.addSpacing(25)

        label1_examples = QLabel("<b>Hotkey Examples:</b>&nbsp;&nbsp;&nbsp;&nbsp;    shift+r, ctrl+d, ctrl+alt+c, tab+ctrl+d, f+g, space+left ctrl")

        myfont.setPointSize(10)
        label2_options = QLabel("Available keys for setting up hotkeys")
        label2_options.setFont(myfont)

        layout.addWidget(label1_examples, alignment=Qt.AlignHCenter)
        layout.addSpacing(10)
        layout.addWidget(label2_options, alignment=Qt.AlignHCenter)

        hlayout = QHBoxLayout()
        keys1 = QLabel("backspace\n"
                        "tab\n"
                        "enter\n"
                        "shift\n"
                        "ctrl\n"
                        "alt\n"
                        "pause\n"
                        "caps lock\n"
                        "esc\n"
                        "space\n"
                        "page up\n"
                        "page down\n"
                        "end\n"
                        "home\n"
                        "left\n"
                        "up\n"
                        "right\n"
                        "down\n"
                        "print screen\n"
                        "insert\n"
                        "delete\n"
                        "cmd\n"
                        "win\n"
                        "apps\n"
                        "menu\n"
                        "scroll lock\n"
                        "pause\n"
                        "num lock\n"
                        "clear\n"
                        "sleep")

        keys2 = QLabel("0 to 9\n"
                        "a to z\n"
                        "numpad 0 to numpad 9\n"
                        "multiply\n"
                        "add\n"
                        "separator\n"
                        "subtract\n"
                        "decimal\n"
                        "divide\n"
                        "f1 to f24\n"
                        "num lock\n"
                        "scroll lock\n"
                        "backtick (the ` key)\n"
                        "minus\n"
                        "equals\n"
                        "left bracket\n"
                        "right bracket\n"
                        "backslash\n"
                        "semicolon\n"
                        "apostrophe\n"
                        "comma\n"
                        "period\n"
                        "slash\n"
                        "grave accent (same as backtick)\n"
                        "backspace\n"
                        "return\n"
                        "caps lock\n"
                        "left shift\n"
                        "right shift\n"
                        "shift")

        keys3 = QLabel("left ctrl\n"
                        "right ctrl\n"
                        "ctrl\n"
                        "left alt\n"
                        "right alt\n"
                        "alt\n"
                        "left command\n"
                        "right command\n"
                        "command\n"
                        "left win\n"
                        "right win\n"
                        "win\n"
                        "left apps\n"
                        "right apps\n"
                        "apps\n"
                        "escape\n"
                        "spacebar\n"
                        "page up\n"
                        "page down\n"
                        "end\n"
                        "home\n"
                        "left arrow\n"
                        "up arrow\n"
                        "right arrow\n"
                        "down arrow\n"
                        "insert\n"
                        "delete\n"
                        "help\n"
                        "print screen\n"
                        "pause")

        hlayout.addWidget(keys1, alignment=Qt.AlignHCenter)
        hlayout.addWidget(keys2, alignment=Qt.AlignHCenter)
        hlayout.addWidget(keys3, alignment=Qt.AlignHCenter)

        layout.addLayout(hlayout)
        layout.addSpacing(25)

        self.setLayout(layout)


class limitations(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Limitations")

        layout = QVBoxLayout()

        myfont = QFont()
        myfont.setBold(True)
        myfont.setPointSize(12)
        howto_label = QLabel("Information")
        howto_label.setFont(myfont)

        layout.addWidget(howto_label, alignment=Qt.AlignHCenter)
        layout.addSpacing(25)

        limit_label = QLabel()
        limit_label.setText("For the 'Autohit Keys' and 'Autocast Keys', at this time, the only keys that will work are individual character keys. \n"
                            "For Example, keys like ctrl or alt won't work.\n\n"
                            "They can't hit mouse buttons either.")

        layout.addWidget(limit_label)
        layout.addSpacing(25)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto KeyCraft")

        self.message_box_open = False
        self.hotkeys_enabled = False
        self.castkeys_enabled = False
        self.cast_hotkey_enabled = False
        self.castkey_listener = None

        # Create a menu bar
        menubar = self.menuBar()

        # File menu
        instruct_menu = menubar.addMenu('Instructions')

        # actions
        hot_action = QAction('Hotkey Help', self)
        hot_action.triggered.connect(self.openinstructDialog)
        instruct_menu.addAction(hot_action)

        limit_action = QAction('Limitations', self)
        limit_action.triggered.connect(self.limitDialog)
        instruct_menu.addAction(limit_action)

        self.tab_widget = QTabWidget()
        self.setup_tab1()
        self.setup_tab2()

        self.setCentralWidget(self.tab_widget)  # Set the QTableView as the central widget

        self.created_label = QLabel("By Jason Fuller  --   jxfuller2@gmail.com")
        self.created_label.setAlignment(Qt.AlignLeft)
        self.v_status_label = QLabel("Version 0.11")
        self.v_status_label.setAlignment(Qt.AlignRight)

        self.statusBar().addPermanentWidget(self.created_label, stretch=1)
        self.statusBar().addPermanentWidget(self.v_status_label, stretch=1)

    def setup_tab1(self):
        self.tab1 = QWidget()
        self.main_layout = QVBoxLayout()

        myfont = QFont()
        myfont.setBold(True)
        myfont.setPointSize(10)

        self.main_label = QLabel("Create Autohit Keys")
        self.main_label.setFont(myfont)

        self.mid_horizontal_layout = QHBoxLayout()

        myfont.setPointSize(8)

        self.hotkey_layout = QVBoxLayout()
        self.hotkey_layout_label = QLabel("Hotkeys")
        self.hotkey_layout_label.setFont(myfont)
        self.hotkey_layout.addWidget(self.hotkey_layout_label, alignment=Qt.AlignHCenter)

        self.keys_tohit_layout = QVBoxLayout()
        self.keys_tohit_label = QLabel("Keys To Hit")
        self.keys_tohit_label.setFont(myfont)
        self.keys_tohit_layout.addWidget(self.keys_tohit_label, alignment=Qt.AlignHCenter)

        self.time_interval_layout = QVBoxLayout()
        self.time_interval_layout_label = QLabel("Key Interval")
        self.time_interval_layout_label.setFont(myfont)
        self.time_interval_layout.addWidget(self.time_interval_layout_label, alignment=Qt.AlignHCenter)

        number_of_base_hotkeys = 5
        for i in range(number_of_base_hotkeys):
            self.create_tab1_widgets()

        self.all_key_interval_layouts = [self.hotkey_layout, self.keys_tohit_layout, self.time_interval_layout]

        self.mid_horizontal_layout.addLayout(self.hotkey_layout)
        self.mid_horizontal_layout.addLayout(self.keys_tohit_layout)
        self.mid_horizontal_layout.addLayout(self.time_interval_layout)

        self.horizontal_enable = QHBoxLayout()
        self.enable_button = QPushButton("Enable Hotkeys")
        self.enable_button.clicked.connect(self.enable_hotkeys)

        self.horizontal_enable.addStretch()
        self.horizontal_enable.addWidget(self.enable_button)
        self.horizontal_enable.addStretch()

        self.main_layout.addWidget(self.main_label, alignment=Qt.AlignHCenter)
        self.main_layout.addSpacing(15)
        self.main_layout.addLayout(self.mid_horizontal_layout)
        self.main_layout.addLayout(self.horizontal_enable)
        self.main_layout.addStretch()

        self.tab1.setLayout(self.main_layout)
        self.tab_widget.addTab(self.tab1, "Autohit Keys")

    def setup_tab2(self):
        self.tab2_widget = QWidget()

        self.tab2_upper_layout = QVBoxLayout()

        myfont = QFont()
        myfont.setBold(True)
        myfont.setPointSize(10)

        self.tab2_label = QLabel("Create Autocast Keys")
        self.tab2_label.setFont(myfont)

        self.midtab2_horizontal_layout = QHBoxLayout()

        myfont.setPointSize(8)

        self.castkey_layout = QVBoxLayout()
        self.castkey_layout_label = QLabel("Cast key")
        self.castkey_layout_label.setFont(myfont)
        self.castkey_layout.addWidget(self.castkey_layout_label, alignment=Qt.AlignHCenter)

        self.cast_interval_layout = QVBoxLayout()
        self.cast_interval_label = QLabel("Time Interval")
        self.cast_interval_label.setFont(myfont)
        self.cast_interval_layout.addWidget(self.cast_interval_label, alignment=Qt.AlignHCenter)

        number_of_base_castkeys = 5
        for i in range(number_of_base_castkeys):
            self.create_tab2_widgets()

        self.all_castkey_interval_layouts = [self.castkey_layout, self.cast_interval_layout]

        self.midtab2_horizontal_layout.addLayout(self.castkey_layout)
        self.midtab2_horizontal_layout.addLayout(self.cast_interval_layout)

        self.horizontal_tab2_hotkey_layout = QHBoxLayout()
        self.tab2_hotkey = QLabel("Start/Stop Hotkey")
        self.tab2_hotkey.setFont(myfont)

        self.tab2_hotkey_edit = QLineEdit()

        self.horizontal_tab2_hotkey_layout.addStretch()
        self.horizontal_tab2_hotkey_layout.addWidget(self.tab2_hotkey)
        self.horizontal_tab2_hotkey_layout.addWidget(self.tab2_hotkey_edit)
        self.horizontal_tab2_hotkey_layout.addStretch()

        self.horizontal_tab2_enable_layout = QHBoxLayout()
        self.enable_cast = QPushButton("Enable Autocast")
        self.enable_cast.clicked.connect(self.enable_castkeys)

        self.horizontal_tab2_enable_layout.addStretch()
        self.horizontal_tab2_enable_layout.addWidget(self.enable_cast)
        self.horizontal_tab2_enable_layout.addStretch()

        self.tab2_upper_layout.addWidget(self.tab2_label, alignment=Qt.AlignHCenter)
        self.tab2_upper_layout.addSpacing(15)
        self.tab2_upper_layout.addLayout(self.midtab2_horizontal_layout)
        self.tab2_upper_layout.addLayout(self.horizontal_tab2_hotkey_layout)
        self.tab2_upper_layout.addSpacing(10)
        self.tab2_upper_layout.addLayout(self.horizontal_tab2_enable_layout)
        self.tab2_upper_layout.addStretch()

        self.tab2_widget.setLayout(self.tab2_upper_layout)

        self.tab_widget.addTab(self.tab2_widget, "Autocast Keys")

    def openinstructDialog(self):
        save_dialog = Howtohotkey(self)
        save_dialog.exec_()

    def limitDialog(self):
        limit_dialog = limitations(self)
        limit_dialog.exec_()

    def create_tab2_widgets(self):
        combo_box = QComboBox()
        # get only base characters on keyboard
        characters = [chr(i) for i in range(33, 127) if not chr(i).isspace() and not chr(i).isupper() and chr(i) not in '"~!@#$%^&*()_+{}:?><|']
        characters.insert(0, "None")
        combo_box.addItems(characters)

        time_spinbox = QDoubleSpinBox()
        time_spinbox.setDecimals(2)

        self.castkey_layout.addWidget(combo_box)
        self.cast_interval_layout.addWidget(time_spinbox)

    def create_tab1_widgets(self):
        hotkey_edit = QLineEdit()
        keys_tohit_edit = QLineEdit()

        time_spinbox = QDoubleSpinBox()
        time_spinbox.setDecimals(2)

        self.hotkey_layout.addWidget(hotkey_edit)
        self.keys_tohit_layout.addWidget(keys_tohit_edit)
        self.time_interval_layout.addWidget(time_spinbox)

    def enable_castkeys(self):
        if self.castkeys_enabled:
            self.enable_cast.setText("Enable Autocast")
            self.castkeys_enabled = False
            self.cast_hotkey_enabled = False
            try:
                keyboard.remove_hotkey(self.castinghotkey)
                if self.castkey_listener:
                    self.castkey_listener.worker.stop_timer()
            except:
                pass
        else:
            self.enable_cast.setText("Disable Autocast")
            self.castkeys_enabled = True
            self.cast_hotkey_enabled = True

            self.castinghotkey = self.tab2_hotkey_edit.text()
            self.castinghotkey = self.castinghotkey.replace(" ", "")

            try:
                keyboard.add_hotkey(self.castinghotkey, self.stop_start_autocasting)
            except:
                self.error_message("ERROR", "Hotkey for autocasting is invalid! See Instructions Menu", "castkeys")

    def stop_start_autocasting(self):
        if self.cast_hotkey_enabled:
            self.cast_hotkey_enabled = False

            keys = self.gather_keys_and_values(self.all_castkey_interval_layouts)
            self.castkey_listener = CastkeyListener(keys)
            self.castkey_listener.start()
        else:
            self.cast_hotkey_enabled = True
            self.castkey_listener.worker.stop_timer()

    def enable_hotkeys(self):
        if self.hotkeys_enabled:
            self.enable_button.setText("Enable Hotkeys")
            self.hotkeys_enabled = False
            self.hotkey_listener.stop_listener()
        else:
            self.enable_button.setText("Disable Hotkeys")
            self.hotkeys_enabled = True

            keys = self.gather_keys_and_values(self.all_key_interval_layouts)

            self.hotkey_listener = HotkeyListener(keys)
            self.hotkey_listener.onError.connect(self.error_message)
            self.hotkey_listener.start()

    def gather_keys_and_values(self, layouts: List[QLayout]) -> dict:
        """
        layouts: list of layouts that you want to collect values from the widgets
        must_have_values:  which layouts from the layouts list must have values in their corresponding widgets
        return: Dictionary.  The widgets for the first layout provided will be the key for the dict, with the rest
        of the widget values in the other layouts being the value as a list for the dictionary
        """
        values_dict = {}

        for total_widgets in range(layouts[0].count()):
            key = ""
            values = []

            for index in range(len(layouts)):
                item = layouts[index].itemAt(total_widgets)

                if item.widget():
                    widget = item.widget()
                    value = ""

                    if isinstance(widget, QLineEdit):
                        value = widget.text()
                        value = value.replace(" ", "")

                    if isinstance(widget, QComboBox):
                        combotext = widget.currentText()
                        if combotext != "None":
                            value = combotext

                    if isinstance(widget, QDoubleSpinBox):
                        value = str(widget.value())

                    if index == 0:
                        key = value
                    else:
                        values.append(value)

            values_dict[key] = values

        # drop any keys that are ''
        for key in list(values_dict.keys()):
            if key == '':
                del values_dict[key]

        # drop any values that are blank
        for key, values in list(values_dict.items()):
            blank_value = False
            for value in values:
                if value == '':
                    blank_value = True

            if blank_value:
                del values_dict[key]

        return values_dict

    def error_message(self, title, msg, reset):
        if reset == "hotkeys":
            self.enable_button.setText("Enable Hotkeys")
            self.hotkeys_enabled = False

        if reset == "castkeys":
            self.enable_cast.setText("Enable Autocast")
            self.castkeys_enabled = False
            self.cast_hotkey_enabled = False
            try:
                keyboard.remove_hotkey(self.castinghotkey)
                if self.castkey_listener:
                    self.castkey_listener.worker.stop_timer()
            except:
                pass

        if not self.message_box_open:
            self.message_box_open = True
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(msg)
            msgBox.setWindowTitle(title)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

            # below code for making sure i don't have more than 1 of the same type of messagebox open
            # this can happen because im using multiple qthreads for the cast keys QThreads
            msgBox.finished.connect(self.message_box_closed)

    def message_box_closed(self):
        self.message_box_open = False


class Worker(QObject):
    def __init__(self, keys):
        super().__init__()
        self.keys = keys

        # append a start time to the key values
        for key, value in self.keys.items():
            value[0] = float(value[0])
            value.append(time.time())

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)

    def start_timer(self):
        self.timer.start(10)  # 10 milliseconds

    def stop_timer(self):
        self.timer.stop()

    def timer_timeout(self):
        for key, value in self.keys.items():
            end = time.time()   
            if end - value[1] > value[0]:
                keyboard.press_and_release(key)
                value[1] = time.time()


class CastkeyListener(QThread):
    timeout_signal = pyqtSignal()

    def __init__(self, keys):
        super().__init__()
        self.keys = keys

    def run(self):
        self.worker = Worker(self.keys)
        self.worker.moveToThread(self)
        self.worker.start_timer()
        self.exec_()


class HotkeyListener(QThread):
    onError = pyqtSignal(str, str, str)

    def __init__(self, hotkeys_and_values, parent=None):
        super(HotkeyListener, self).__init__(parent)
        self.hotkeys_and_values = hotkeys_and_values

        self.hotkeys, self.buttons, self.interval = self.hotkey_buttons_interval(self.hotkeys_and_values)

    def run(self):
        try:
            for key, value in self.hotkeys.items():
                keyboard.add_hotkey(key, value)
        except:
            self.onError.emit("ERROR", "One of the hotkeys is invalid! See Instructions Menu", "hotkeys")

    def hotkey_buttons_interval(self, hotkeys_values) -> [Dict[str, object], Dict[str, List[str]], Dict[str, float]]:
        hotkey_function = {}
        buttons_to_hit = {}
        time_intervals = {}

        for key, values in hotkeys_values.items():
            buttons = list(values[0])
            time_interval = float(values[1])

            buttons_to_hit[key] = buttons
            time_intervals[key] = time_interval
            hotkey_function[key] = lambda k=key: self.function_1(k)

        return hotkey_function, buttons_to_hit, time_intervals

    def function_1(self, hotkey):
        buttons = self.buttons[hotkey]
        interval = self.interval[hotkey]
        for button in buttons:
            keyboard.press_and_release(button)
            time.sleep(interval)

        # example of hitting a keyboard combination, not using this, but keeping code here
        # in case i add this functionality
        # key_controller.tap(keyboard.Key.ctrl, [keyboard.Key.alt, 'h'])

    def stop_listener(self):
        for key, value in self.hotkeys.items():
            keyboard.remove_hotkey(key)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = MainWindow()
    viewer.show()
    sys.exit(app.exec_())
