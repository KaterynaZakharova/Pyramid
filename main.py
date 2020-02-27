import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import *
import random as rnd
from functools import partial


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


ui = Ui_MainWindow()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui.setupUi(MainWindow)
_translate = QtCore.QCoreApplication.translate
card_list = [('2♠', 2), ('3♠', 3), ('4♠', 4), ('5♠', 5), ('6♠', 6), ('7♠', 7), ('8♠', 8), ('9♠', 9), 
             ('10♠', 10), ('J♠', 11), ('Q♠', 12), ('K♠', 13), ('A♠', 1), ('2♥', 2), ('3♥', 3), ('4♥', 4),
             ('5♥', 5), ('6♥', 6), ('7♥', 7), ('8♥', 8), ('9♥', 9), ('10♥', 10), ('J♥', 11), ('Q♥', 12), ('K♥', 13),
             ('A♥', 1), ('2♦', 2), ('3♦', 3), ('4♦', 4), ('5♦', 5), ('6♦', 6), ('7♦', 7), ('8♦', 8), ('9♦', 9), 
             ('10♦', 10), ('J♦', 11), ('Q♦', 12), ('K♦', 13), ('A♦', 1), ('2♣', 2), ('3♣', 3), ('4♣', 4), ('5♣', 5),
             ('6♣', 6), ('7♣', 7), ('8♣', 8), ('9♣', 9),  ('10♣', 10), ('J♣', 11), ('Q♣', 12), ('K♣', 13), ('A♣', 1)]
rnd.shuffle(card_list)
button_list = [ui.Card1_1, ui.Card2_1, ui.Card2_2, ui.Card3_1, ui.Card3_2, ui.Card3_3,
               ui.Card4_1, ui.Card4_2, ui.Card4_3, ui.Card4_4, ui.Card5_1, ui.Card5_2,
               ui.Card5_3, ui.Card5_4, ui.Card5_5, ui.Card6_1, ui.Card6_2, ui.Card6_3,
               ui.Card6_4, ui.Card6_5, ui.Card6_6, ui.Card7_1, ui.Card7_2, ui.Card7_3,
               ui.Card7_4, ui.Card7_5, ui.Card7_6, ui.Card7_7]
stack = card_list[28:]
pyramid_cards_list = {}
click_on_stack = 0
current_score = 0 
total_score = 0
hold_cards = 0
max_click = 23
step = 0


class Cards:
    def stack_func(self, *args, **kwargs):
        """ Stack.

            Function creates an unchanged queue order in the stack. It hides the stack if it is empty.
            It sets text and colors to cards.
            :param args:
            :param kwargs:
        """
        global click_on_stack
        if len(stack) == 1:
            ui.Stack_card_close.hide()
        if click_on_stack > max_click:
            click_on_stack = 0
        ui.Stack_card_open.setText(_translate("MainWindow", stack[click_on_stack][0]))
        if not ui.mode:
            if '♥' in stack[click_on_stack][0]:
                ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
            elif '♦' in stack[click_on_stack][0]:
                ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
            else:
                ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
        else:
            if '♥' in stack[click_on_stack][0]:
                ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
            elif '♦' in stack[click_on_stack][0]:
                ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
            else:
                ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(0, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
        click_on_stack += 1

    def pyramid(self, button_list, card_list, *args, **kwargs):
        """ Pyramid of cards.

            Function creates a pyramid of unique cards. It sets the text and colors to cards.
            It writes down the button and its card and a value of cards to the pyramid_cards_list.
            :param button_list:
            :param card_list:
            :param args:
            :param kwargs:
        """
        for i in range(28):
            button_list[i].setText(_translate("MainWindow", card_list[i][0]))
            if '♥' in card_list[i][0]:
                button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
            elif '♦' in card_list[i][0]:
                button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
            else:
                button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")
            pyramid_cards_list[str(button_list[i])] = (card_list[i])

    def score(self, clicked_button, *args, **kwargs):
        """ Count score.

            Function counts a current score, a total score and show them. It also shows a hint (how many points
            the player has and how many points left). It delete an collected card from the stack.
            :param clicked_button:
            :param args:
            :param kwargs:
        """
        global current_score, hold_cards, click_on_stack, total_score, max_click
        if ui.Stack_card_open.isCheckable():
            ui.Stack_card_open.setCheckable(False)
            current_score = 0
        if clicked_button == ui.Stack_card_open:
            if current_score == stack[click_on_stack - 1][1]:
                current_score = 0
                hold_cards = 0
            if hold_cards == 0:
                clicked_button.setCheckable(True)
                hold_cards += 1
                current_score += stack[click_on_stack - 1][1]
                if not ui.mode:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                else:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#d3d3d3;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))

                if current_score == 13:
                    clicked_button.setCheckable(False)
                    clicked_button.hide()
                    del stack[click_on_stack - 1]
                    click_on_stack -= 1
                    max_click -= 1
                    hold_cards = 0
                    current_score = 0
                    total_score += 13
                    if not ui.mode:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#ffffff;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                    else:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#d3d3d3;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
            elif hold_cards == 1:
                clicked_button.setCheckable(True)
                current_score += stack[click_on_stack - 1][1]
                if not ui.mode:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                else:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#d3d3d3;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                if current_score == 13:
                    for i in button_list:
                        if i.isCheckable():
                            i.setCheckable(False)
                            i.hide()
                    clicked_button.hide()
                    del stack[click_on_stack - 1]
                    click_on_stack -= 1
                    max_click -= 1
                    total_score += 13
                    if not ui.mode:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#ffffff;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                    else:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#d3d3d3;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                else:
                    for i in button_list:
                        if i.isCheckable():
                            i.setCheckable(False)
                hold_cards = 0
                current_score = 0
        else:
            if current_score == pyramid_cards_list[str(clicked_button)][1]:
                current_score = 0
                hold_cards = 0
            if hold_cards == 0:
                clicked_button.setCheckable(True)
                hold_cards += 1
                current_score += pyramid_cards_list[str(clicked_button)][1]
                if not ui.mode:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                else:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#d3d3d3;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                if current_score == 13:
                    clicked_button.hide()
                    hold_cards = 0
                    current_score = 0
                    total_score += 13
                    if not ui.mode:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#ffffff;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                    else:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#d3d3d3;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
            elif hold_cards == 1:
                clicked_button.setCheckable(True)
                current_score += pyramid_cards_list[str(clicked_button)][1]
                if not ui.mode:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                else:
                    ui.Hint.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#d3d3d3;\">"
                                                            f"You have {current_score} point(s). {13 - current_score}"
                                                            f" point(s) left.</span></p></body></html>"))
                if current_score == 13:
                    total_score += 13
                    if not ui.mode:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#ffffff;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                    else:
                        ui.Score_number.setText(_translate("MainWindow", f"<html><head/><body><p>"
                                                                     f"<span style=\" color:#d3d3d3;\">"
                                                                     f"{str(total_score)}</span></p></body></html>"))
                    for i in button_list:
                        if i.isCheckable():
                            i.hide()
                    if ui.Stack_card_open.isCheckable():
                        ui.Stack_card_open.hide()
                else:
                    for i in button_list:
                        if i.isCheckable():
                            i.setCheckable(False)
                    if ui.Stack_card_open.isCheckable():
                        ui.Stack_card_open.setCheckable(False)
                hold_cards = 0
                current_score = 0
        if total_score == 364:
            ui.Winner.show()


class Pyramid:
    def locked(self, button_list, card_list, *args, **kwargs):
        """ Locked cards.

            Function locks unavailable cards.
            :param button_list:
            :param card_list:
            :param args:
            :param kwargs:
        """
        for i in range(len(button_list[:21])):
            button_list[i].setEnabled(False)
            if '♥' in card_list[i][0]:
                button_list[i].setStyleSheet("background-color: grey;\n" "color: rgb(170, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
            elif '♦' in card_list[i][0]:
                button_list[i].setStyleSheet("background-color: grey;\n" "color: rgb(170, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
            else:
                button_list[i].setStyleSheet("background-color: grey;\n" "color: rgb(0, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")

    def unlocked(self, button_list, *args, **kwargs):
        """ Unlocked cards.

            Function unlocks now available cards.
            :param button_list:
            :param args:
            :param kwargs:
        """
        global step
        for i in range(21):
            if i == 0:
                step = 1
            elif i == 1:
                step = 2
            elif i == 3:
                step = 3
            elif i == 6:
                step = 4
            elif i == 10:
                step = 5
            elif i == 15:
                step = 6
            if not button_list[i].isEnabled():
                if button_list[i + step].isHidden() and button_list[i + step + 1].isHidden():
                    button_list[i].setEnabled(True)
                    if not ui.mode:
                        if '♥' in card_list[i][0]:
                            button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                                         "font: 20pt \"MS Shell Dlg 2\";")
                        elif '♦' in card_list[i][0]:
                            button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                                         "font: 20pt \"MS Shell Dlg 2\";")
                        else:
                            button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n" 
                                                         "font: 20pt \"MS Shell Dlg 2\";")
                    else:
                        if '♥' in card_list[i][0]:
                            button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n"
                                                         "font: 20pt \"MS Shell Dlg 2\";")
                        elif '♦' in card_list[i][0]:
                            button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n"
                                                         "font: 20pt \"MS Shell Dlg 2\";")
                        else:
                            button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(0, 0, 0);\n" 
                                                         "font: 20pt \"MS Shell Dlg 2\";")

    def new_game(self, *args, **kwargs):
        """ New game.

            Function starts new game. It updates a pyramid of cards and a stack.
            :param args:
            :param kwargs:
        """
        global current_score, total_score, click_on_stack, hold_cards, max_click, step, stack
        current_score, total_score, click_on_stack, hold_cards, max_click, step = 0, 0, 0, 0, 23, 0
        rnd.shuffle(card_list)
        stack = card_list[28:]
        Cards.pyramid(Cards, button_list, card_list)
        Cards.stack_func(Cards)
        Pyramid.locked(Pyramid, button_list, card_list)
        view(ui.mode)
        for i in button_list:
            i.show()
            i.setCheckable(False)
        ui.Stack_card_open.setCheckable(False)
        ui.Stack_card_close.show()
        ui.Winner.hide()


def view(mode):
    """ Interface's view.

        Function changes interface's view from light colors to dark colors and conversely.
        :param mode:
        :return:
    """
    if not ui.mode:
        mode = False
    else:
        mode = True
    if mode:
        for i in range(len(button_list)):
            if button_list[i].isEnabled():
                if '♥' in card_list[i][0]:
                    button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
                elif '♦' in card_list[i][0]:
                    button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
                else:
                    button_list[i].setStyleSheet("background-color: #4C516D;\n" "color: rgb(0, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
        if '♥' in ui.Stack_card_open.text():
            ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")
        elif '♦' in ui.Stack_card_open.text():
            ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(170, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")
        else:
            ui.Stack_card_open.setStyleSheet("background-color: #4C516D;\n" "color: rgb(0, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
    else:
        for i in range(len(button_list)):
            if button_list[i].isEnabled():
                if '♥' in card_list[i][0]:
                    button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
                elif '♦' in card_list[i][0]:
                    button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")
                else:
                    button_list[i].setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n" 
                                                 "font: 20pt \"MS Shell Dlg 2\";")
        if '♥' in ui.Stack_card_open.text():
            ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")
        elif '♦' in ui.Stack_card_open.text():
            ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(170, 0, 0);\n" 
                                             "font: 20pt \"MS Shell Dlg 2\";")
        else:
            ui.Stack_card_open.setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")


def main():
    """ Main function. """
    ui.actionMode.triggered.connect(partial(view, ui.mode))
    Cards.pyramid(Cards, button_list, card_list)
    ui.Stack_card_close.clicked.connect(partial(Cards.stack_func, Cards))
    Pyramid.locked(Pyramid, button_list, card_list)
    ui.Card1_1.clicked.connect(partial(Cards.score, Cards, ui.Card1_1))
    ui.Card2_1.clicked.connect(partial(Cards.score, Cards, ui.Card2_1))
    ui.Card2_2.clicked.connect(partial(Cards.score, Cards, ui.Card2_2))
    ui.Card3_1.clicked.connect(partial(Cards.score, Cards, ui.Card3_1))
    ui.Card3_2.clicked.connect(partial(Cards.score, Cards, ui.Card3_2))
    ui.Card3_3.clicked.connect(partial(Cards.score, Cards, ui.Card3_3))
    ui.Card4_1.clicked.connect(partial(Cards.score, Cards, ui.Card4_1))
    ui.Card4_2.clicked.connect(partial(Cards.score, Cards, ui.Card4_2))
    ui.Card4_3.clicked.connect(partial(Cards.score, Cards, ui.Card4_3))
    ui.Card4_4.clicked.connect(partial(Cards.score, Cards, ui.Card4_4))
    ui.Card5_1.clicked.connect(partial(Cards.score, Cards, ui.Card5_1))
    ui.Card5_2.clicked.connect(partial(Cards.score, Cards, ui.Card5_2))
    ui.Card5_3.clicked.connect(partial(Cards.score, Cards, ui.Card5_3))
    ui.Card5_4.clicked.connect(partial(Cards.score, Cards, ui.Card5_4))
    ui.Card5_5.clicked.connect(partial(Cards.score, Cards, ui.Card5_5))
    ui.Card6_1.clicked.connect(partial(Cards.score, Cards, ui.Card6_1))
    ui.Card6_2.clicked.connect(partial(Cards.score, Cards, ui.Card6_2))
    ui.Card6_3.clicked.connect(partial(Cards.score, Cards, ui.Card6_3))
    ui.Card6_4.clicked.connect(partial(Cards.score, Cards, ui.Card6_4))
    ui.Card6_5.clicked.connect(partial(Cards.score, Cards, ui.Card6_5))
    ui.Card6_6.clicked.connect(partial(Cards.score, Cards, ui.Card6_6))
    ui.Card7_1.clicked.connect(partial(Cards.score, Cards, ui.Card7_1))
    ui.Card7_2.clicked.connect(partial(Cards.score, Cards, ui.Card7_2))
    ui.Card7_3.clicked.connect(partial(Cards.score, Cards, ui.Card7_3))
    ui.Card7_4.clicked.connect(partial(Cards.score, Cards, ui.Card7_4))
    ui.Card7_5.clicked.connect(partial(Cards.score, Cards, ui.Card7_5))
    ui.Card7_6.clicked.connect(partial(Cards.score, Cards, ui.Card7_6))
    ui.Card7_7.clicked.connect(partial(Cards.score, Cards, ui.Card7_7))
    ui.Stack_card_open.clicked.connect(partial(Cards.score, Cards, ui.Stack_card_open))
    ui.Cards_group.buttonClicked.connect(partial(Pyramid.unlocked, Pyramid, button_list))
    ui.actionNew_game.triggered.connect(Pyramid.new_game)


if __name__ == '__main__':
    main()
    MainWindow.show()
    sys.exit(app.exec_())

