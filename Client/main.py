import sys
import cv2 
import numpy as np
import os
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QMessageBox, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

from picamera2 import Picamera2
from picamera2.previews.qt import QGlPicamera2

from mainwindow_pyqt5 import Ui_MainWindow
from capture_window_pyqt5 import Ui_Form
from predict_dialog_pyqt5 import Ui_predict_Dialog
from report_dialog_pyqt5 import Ui_report_Dialog
from predict_fruits import predict_fruits

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #---set the window title of the Main Window---#
        self.setWindowTitle("PechayIQ App")

        #---Call the QWidget Ui_Form class---# 
        self.capture_window_object = QWidget(self)                # create a QWidget object
        self.capture_window_ui = Ui_Form()                        # Create an instance of the Ui_Form class 
        self.capture_window_ui.setupUi(self.capture_window_object)
        self.capture_window_object.setWindowTitle("Capture Window")

        #---hide capture window ui_form---#
        self.capture_window_object.hide()

        #---findChild gets a reference to the widget inside a mainwindow---#
        self.vertical_layout = self.capture_window_object.findChild(QVBoxLayout, 'verticalLayout')
        self.cap_button = self.capture_window_object.findChild(QPushButton, 'photocapBtn')
        self.close_button = self.capture_window_object.findChild(QPushButton, 'closeBtn')
        self.piFrame = self.capture_window_object.findChild(QFrame, 'picamera_frame') 

        #---Set the picamera2 and put it in the PyQt application---# 
        self.picam2 = Picamera2() # set the object variable
        self.picam2.configure(self.picam2.create_preview_configuration(main={"size": (self.piFrame.width(),self.piFrame.height())})) # preview config
        self.qpicamera2 = QGlPicamera2(self.picam2, width=self.piFrame.width(), height=self.piFrame.height(), keep_ar=True) # set a Qt object to display the preview
        self.picam2.start() # Important to start the camera

        #---add the picamera preview to the capture window ui_form---#
        self.vertical_layout.addWidget(self.qpicamera2)

        #---Signal and Slots---#
        self.captureBtn.clicked.connect(self.capture_button_clicked)
        self.reportBtn.clicked.connect(self.report_button_clicked)
        self.predictBtn.clicked.connect(self.predict_button_clicked)

    def capture_button_clicked(self):
        #---show capture window ui_form---#
        self.capture_window_object.show()

        #---Signal and Slots---#
        self.close_button.clicked.connect(self.close_picamera_button_clicked)
        self.cap_button.clicked.connect(self.take_photo_button_clicked)

        #---Important it signals when the picamera capture is done---#
        self.qpicamera2.done_signal.connect(self.capture_done)

    def close_picamera_button_clicked(self):
        self.capture_window_object.hide()

    def take_photo_button_clicked(self):
        #---This will make the buttons unclickable---#
        self.cap_button.setEnabled(False)
        self.close_button.setEnabled(False)

        #---creates high resolution still images---#
        cfg = self.picam2.create_still_configuration()
        self.picam2.switch_mode_and_capture_file(cfg, "pehcay_image.jpg", signal_function=self.qpicamera2.signal_done)

    def capture_done(self,job):
        #---wait until the capturing is done---#
        self.picam2.wait(job)

        #----This will make the buttons clickable again---#
        self.close_button.setEnabled(True)
        self.cap_button.setEnabled(True)

        #---When the capture is done load the image to the mainwindow---#
        self.load_image()

    def predict_button_clicked(self):

        self.plant_id_text = self.plant_id_edit.currentText()

        #---if the plant id text box is empty---#
        if not self.plant_id_text:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("Plant ID is empty\n\nInput Plant ID information")
            msgbox.setWindowTitle("Plant ID error")
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()

        else:
            self.load_image()
            self.find_image_path()

            #---Resize the frame, convert to float, normalize and convert to list---#
            if os.path.exists(self.image_path):
                frame = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED) # Returns image with alpha channel (transparency)
                img_cv = cv2.resize(frame, (150, 150)) # Resize the frame. This is a numpy.ndarray
                img_cv = img_cv.astype("float") / 255.0 # numpy.ndarray. Convert dtype to float and normalize it. (Decimals)
                image = img_cv.tolist() # Convert numpy array to list

                #---Get the ip address of the server---#
                ip = self.ip_edit.currentText()

                #---feed the image, ip address and port number to the function---#
                predictions = predict_fruits(self,image,ip)

                #---Note: predictions["prediction"] is a list---#
                preds = np.array(predictions["prediction"])

                #---Call the predict dialog python file---#
                self.predict_dialog_object = QDialog(self)              # create a QDialog object
                self.predict_dialog_ui = Ui_predict_Dialog()            # Create an instance of the Ui_Dialog class 
                self.predict_dialog_ui.setupUi(self.predict_dialog_object)  # Use the setupUI method from the predict_dialog_pyqt5.py file and pass in the dialog object
                
                self.predict_dialog_object.setWindowTitle("Prediction Result")

                #---create a reference to the QLineEdit from the predict dialog---#
                self.pred_edit = self.predict_dialog_object.findChild(QLineEdit, 'pred_edit') # findChild gets a reference to the QLineEdit widget inside a mainwindow
                self.feedback_edit = self.predict_dialog_object.findChild(QLineEdit, 'feedback_edit') # findChild gets a reference to the QLineEdit widget inside a mainwindow

                if preds[0]==np.max(preds):
                    self.pred_edit.setText("Fresh Apple")
                elif preds[1]==np.max(preds):
                    self.pred_edit.setText("Fresh Banana")
                elif preds[2]==np.max(preds):
                    self.pred_edit.setText("Fresh Orange")
                elif preds[3]==np.max(preds):
                    self.pred_edit.setText("Rotten Apple")
                elif preds[4]==np.max(preds):
                    self.pred_edit.setText("Rotten Banana")
                elif preds[5]==np.max(preds):
                    self.pred_edit.setText("Rotten Orange")

                # if preds[0]==np.max(preds):
                #   self.pred_edit.setText("Overall Chlorosis")
                # elif preds[1]==np.max(preds):
                #   self.pred_edit.setText("Intervenial Chlorosis")
                # elif preds[2]==np.max(preds):
                #   self.pred_edit.setText("Purpling")
                # elif preds[3]==np.max(preds):
                #   self.pred_edit.setText("Local Necrosis")

                #---execute the predict dialog---#
                self.predict_dialog_object.exec_()

                #---Get the text of the pred_edit---#
                self.pred_result = self.pred_edit.text() # Accessible to other method due to "self"

                #---put the pred_result in the sqlite3 database---#
                self.add_db()

                #---Uncomment this to set the Plant ID to "" after clicking predict---#
                #self.plant_id_edit.setCurrentIndex(-1)

            else:
                self.cam_feed_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Image Feed</span></p></body></html>")

    def load_image(self):

        #---open and load image in the pyqt5 app---#
        self.find_image_path()

        if os.path.exists(self.image_path):
            img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED) # Returns image with alpha channel (transparency)
            img = cv2.resize(img, (self.cam_feed_label.width(), self.cam_feed_label.height()))
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Set the QImage to the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.cam_feed_label.setPixmap(pixmap)
            
        else:
            self.cam_feed_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Image Feed</span></p></body></html>")


    def find_image_path(self):
        #---create the path for the image---#
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")
            self.image_path = os.path.join(base_path,'pehcay_image.jpg')

    def add_db(self):
        #--create a connection to the sqlite3 database---#
        conn = sqlite3.connect("database.db") # create a .db file and if the db does not exist it will create a new one
        cursor = conn.cursor() # use this cursor to do any kinds of things
        
        #---Create a table named "infos" with column names "plant_id, datetime_utc8 text, and plant_status"---#
        cursor.execute("CREATE TABLE IF NOT EXISTS infos(plant_id text, datetime_utc8 text, plant_status text)") # create table named infos and put column names datetime_utc8 and plant_status
        cursor.execute("INSERT INTO infos VALUES(?, datetime('now','localtime'), ?)", ([self.plant_id_text,self.pred_result])) # square bracket to treat as 2 characters as we have only 2 '?' -> a placeholder

        #---save changes by commit() and then close connection to db---#
        conn.commit()
        conn.close()

    def report_button_clicked(self):
        #---Call the report dialog python file---#
        self.report_dialog_object = QDialog(self)           # create a QDialog object
        self.report_dialog_ui = Ui_report_Dialog()          # Create an instance of the Ui_Dialog class 
        self.report_dialog_ui.setupUi(self.report_dialog_object)    # Use the setupUI method from the report_dialog_pyqt5.py file and pass in the dialog object

        self.report_dialog_object.setWindowTitle("Plant Health Table Report")

        #---create a reference to the QTableWidget from the report dialog---#
        self.tableWidget = self.report_dialog_object.findChild(QTableWidget, 'report_table') # findChild gets a reference to the QTableWidget widget inside a mainwindow
        
        #---create a reference to the QPushButton from the report dialog and then create a signal when it is clicked---#
        self.del_row = self.report_dialog_object.findChild(QPushButton, 'del_Btn') # findChild gets a reference to the QPushButton widget inside a mainwindow
        self.del_row.clicked.connect(self.del_row_DB)

        #---call and load the db in the QTableWidget---#
        self.load_db()

        #---execute the report dialog---#
        self.report_dialog_object.exec_() # Show the dialog

    def load_db(self):
        #--create a connection to the sqlite3 database---#
        conn = sqlite3.connect("database.db") # create a .db file and if the db does not exist it will create a new one
        cursor = conn.cursor() # use this cursor to do any kinds of things

        #---This will delete all entries in the table widget so it will not duplicate when loaded---#
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        
        #---put the database items to the QTableWidget---#
        fetched_data = cursor.execute("SELECT plant_id, date(datetime_utc8), time(datetime_utc8), plant_status FROM infos")

        #---Set the column headers size by pixels---#
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, 75)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 192)
        
        for row_index, row_data in enumerate(fetched_data):
            self.tableWidget.insertRow(row_index) # create an empty row
            for col_index, col_data in enumerate(row_data): # col_index = 0 is date, col_index = 2 is time and col_index =3 is plant_status
                item_table = QTableWidgetItem(col_data)
                item_table.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_index, col_index, item_table)

        #---save changes by commit() and then close connection to db---#
        conn.commit()
        conn.close()

    def del_row_DB(self):
        #--create a connection to the sqlite3 database---#
        conn = sqlite3.connect("database.db") # create a .db file and if the db does not exist it will create a new one
        cursor = conn.cursor() # use this cursor to do any kinds of things

        fetched_data = cursor.execute("SELECT plant_id, date(datetime_utc8), time(datetime_utc8), plant_status FROM infos")

        #---row is all the items in the db since we SELECT "*" and row[0] is all row indexes (because of enumerate())---#
        for row in enumerate(fetched_data):
            if row[0] == self.tableWidget.currentRow():
                plantID = row[1][0]
                fdate = row[1][1]
                ftime = row[1][2]
                status = row[1][3]
                cursor.execute("DELETE FROM infos WHERE plant_id = ? AND date(datetime_utc8)=? AND time(datetime_utc8)=? AND plant_status=?",(plantID,fdate,ftime,status,))
                conn.commit()

        #---save changes by commit() and then close connection to db---#
        conn.commit()
        conn.close()
        self.load_db()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow() #Instantiate the MainWindow class
    window.show()
    sys.exit(app.exec())