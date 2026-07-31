from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__students = {}

        self.add_button.clicked.connect(lambda: self.add())
        self.submit_button.clicked.connect(lambda: self.submit())

    def add(self):
        name = self.student_name_text.toPlainText()
        score = self.student_score_text.toPlainText()

        if name.isalpha() == False:
            self.description_label.setText("Name cannot contain numbers")
            return

        elif name == "":
            self.description_label.setText("Name cannot be empty")
            return
        
        elif score == "":
            self.description_label.setText("Score cannot be empty")
            return
        try:
            score = float(score)
            if score < 0 or score > 100:
                self.description_label.setText("Score must be between 0 and 100")
                return
            
        except ValueError:
            self.description_label.setText("Score must be a number")
            return
        

        self.__students[name] = score

        self.student_name_text.clear()
        self.student_score_text.clear()
        self.description_label.setText("Student added successfully")

    def submit(self):
        if not self.__students:
            self.description_label.setText("No students to submit")
            return

        grades = self.def_grades_dict()
        for name, score in self.__students.items():
            if score >= grades["A"]:
                grade = "A"
            elif score >= grades["B"]:
                grade = "B"
            elif score >= grades["C"]:
                grade = "C"
            elif score >= grades["D"]:
                grade = "D"
            else:
                grade = "F"

            self.csv_writer(name, score, grade)

        self.description_label.setText("All students submitted successfully")
        self.__students.clear()
        self.student_name_text.clear()
        self.student_score_text.clear()
        

    def def_grades_dict(self):
        max_value = max(self.__students.values())
        grades = {
            "A": (max_value - 10),
            "B": (max_value - 20),
            "C": (max_value - 30),
            "D": (max_value - 40),      
        }
        return grades
    
    def csv_writer(self, name, score, grade):
        with open("data.csv", "a+", newline="") as file:
            file.write(f"{name},{score},{grade}\n")