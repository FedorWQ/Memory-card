from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle, choice
class Question():
    def __init__(self,question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
question = []
question.append(Question('Кто я?', 
                        'Утка',
                        'Фрукт',
                        'Камень',
                        'Человек'))
question.append(Question('Из какого мяса делают пожарские котлеты?',
                        'Курица',
                        'Свинина',
                        'Говядина',
                        'Баранина'))
question.append(Question('Какой философ первым ввёл понятие "пессимизм"?',
                        'Шопенгауэр',
                        'Ницше',
                        'Кант',
                        'Юн'))
question.append(Question('Как называется новорожденный детеныш нерпы?',
                        'Белек',
                        'Пыжик',
                        'Детва',
                        'Умка'))
app = QApplication([])
main_win = QWidget()
main_win.score = 0
main_win.total = 0
main_win.setWindowTitle('Memory Card')
main_win.resize(400,400)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    pbtn.setText('Следующий вопрос')
    print('Статистика:')
    print('-Всего вопросов:',main_win.total)
    print('-Правильных ответов:',main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100, '%')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    pbtn.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)
def star_text():
    if pbtn.text() == 'Ответить':
        check_answer()
    else:
        next_questions()
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    r.setText(q.question)
    p.setText(q.right_answer)
    show_question()
def check_answer():
    if buttons[0].isChecked():
        pn.setText('Правильно')
        main_win.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        pn.setText('Неправильно')
        show_result()
def next_questions():
    main_win.total += 1
    rand_q = choice(question)
    ask(rand_q)
r = QLabel('Вопрос')
p = QLabel('Правильный ответ')
pn = QLabel('Правильно/Неправильно')
btn1 = QRadioButton('1')
btn2 = QRadioButton('2')
btn3 = QRadioButton('3')
btn4 = QRadioButton('4')
buttons = [btn1, btn2, btn3,btn4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

pbtn = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
v_line2.addWidget(btn1)
v_line2.addWidget(btn2)
v_line3.addWidget(btn3)
v_line3.addWidget(btn4)
h_line4.addLayout(v_line2)
h_line4.addLayout(v_line3)
RadioGroupBox.setLayout(h_line4)
h_line2.addWidget(RadioGroupBox)
h_line1.addWidget(r)
h_line3.addWidget(pbtn)
v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)
v_line1.addLayout(h_line3)
main_win.setLayout(v_line1)
AnsGroupBox = QGroupBox('Варианты ответов')
AnsGroupBox.hide()
v_line4 = QVBoxLayout()
v_line4.addWidget(pn)
v_line4.addWidget(p)
AnsGroupBox.setLayout(v_line4)
h_line2.addWidget(AnsGroupBox)
pbtn.clicked.connect(star_text)
next_questions()

main_win.show()
app.exec_()