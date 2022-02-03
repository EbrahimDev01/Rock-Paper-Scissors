import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from GUIs.rock_paper_scissors_ui import Ui_MainWindow
from random import choice


class RockPaperScissorsWindow(QMainWindow):
    def __init__(self):
        super(RockPaperScissorsWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()
        self.switch = False
        self.modes = ('scissors', 'paper', 'rock')
        self.won = 0
        self.lost = 0
        self.draw = 0

    def setup(self):
        icon_scissors = QIcon(QPixmap("../Image/scissors.jpg"))
        self.ui.btn_scissors_choice.setIcon(icon_scissors)

        icon_paper = QIcon(QPixmap("../Image/paper.jpg"))
        self.ui.btn_paper_choice.setIcon(icon_paper)

        icon_rock = QIcon(QPixmap("../Image/rock.jpg"))
        self.ui.btn_rock_choice.setIcon(icon_rock)

        self.hide_answer()
        self.setup_events()

    def setup_events(self):
        self.ui.btn_scissors_choice.clicked.connect(lambda: self.select_user_mode('scissors'))
        self.ui.btn_paper_choice.clicked.connect(lambda: self.select_user_mode('paper'))
        self.ui.btn_rock_choice.clicked.connect(lambda: self.select_user_mode('rock'))
        self.ui.btn_try_again.clicked.connect(self.hide_answer)

    def hide_answer(self):
        self.ui.label_show_computer_choice.hide()
        self.ui.label_show_user_choice.hide()
        self.ui.btn_scissors_choice.show()
        self.ui.btn_paper_choice.show()
        self.ui.btn_rock_choice.show()
        self.ui.btn_try_again.hide()
        self.ui.label_result_game.hide()

    def show_answer(self):
        self.ui.label_show_computer_choice.show()
        self.ui.label_show_user_choice.show()
        self.ui.btn_try_again.show()
        self.ui.label_result_game.show()
        self.ui.btn_scissors_choice.hide()
        self.ui.btn_paper_choice.hide()
        self.ui.btn_rock_choice.hide()

    def select_user_mode(self, user_choice):
        self.show_answer()
        computer_choice = self.select_computer_mode()
        result = self.game_logic(user_choice, computer_choice)
        self.ui.label_result_game.setText(result)
        self.show_select_mode(user_choice, computer_choice)

    def show_select_mode(self, user_choice, computer_choice):
        self.ui.label_show_user_choice.setPixmap(QPixmap(f'../image/{user_choice}.jpg'))
        self.ui.label_show_computer_choice.setPixmap(QPixmap(f'../image/{computer_choice}.jpg'))

    def select_computer_mode(self):
        return choice(self.modes)

    def game_logic(self, user_choice, computer_choice):
        if (user_choice == 'scissors' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'paper') or \
                (user_choice == 'rock' and computer_choice == 'rock'):
            self.draw += 1
            self.ui.label_draw_points.setText(str(self.draw))
            return 'You Draw'
        elif (user_choice == 'scissors' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'rock' and computer_choice == 'scissors'):
            self.won += 1
            self.ui.label_won_points.setText(str(self.won))
            return 'You Won'
        elif (user_choice == 'paper' and computer_choice == 'scissors') or \
                (user_choice == 'rock' and computer_choice == 'paper') or \
                (user_choice == 'scissors' and computer_choice == 'rock'):
            self.lost += 1
            self.ui.label_lost_points.setText(str(self.lost))
            return 'You Lost'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RockPaperScissorsWindow()
    window.show()
    sys.exit(app.exec_())
