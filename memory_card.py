from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle, randint

app = QApplication([])




btn_ok = QPushButton('Ответить')
Lb_Question = QLabel('')

RafdioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('1 Октебря')
rbtn_2 = QRadioButton('1 Сентября')
rbtn_3 = QRadioButton('8 Марты')
rbtn_4 = QRadioButton('31 Декабря')
message_res = QMessageBox()


Radigrup = QButtonGroup()
Radigrup.addButton(rbtn_1)
Radigrup.addButton(rbtn_2)
Radigrup.addButton(rbtn_3)
Radigrup.addButton(rbtn_4)

layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()
layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RafdioGroupBox.setLayout(layout_1)

AnsGruopBox = QGroupBox('Результaты теста:')
lb_Result = QLabel('')
Lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGruopBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(Lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RafdioGroupBox)
layout_line2.addWidget(AnsGruopBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

Layout_card = QVBoxLayout()

Layout_card.addLayout(layout_line1, stretch=2)
Layout_card.addLayout(layout_line2, stretch=8)
Layout_card.addStretch(1)
Layout_card.addLayout(layout_line3, stretch=1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
