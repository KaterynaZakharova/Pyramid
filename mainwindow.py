# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, Card1_1=0, Card2_1=0, Card2_2=0, Card3_1=0, Card3_2=0, Card3_3=0,
                 Card4_1=0, Card4_2=0, Card4_3=0, Card4_4=0, Card5_1=0, Card5_2=0,
                 Card5_3=0, Card5_4=0, Card5_5=0, Card6_1=0, Card6_2=0, Card6_3=0,
                 Card6_4=0, Card6_5=0, Card6_6=0, Card7_1=0, Card7_2=0, Card7_3=0,
                 Card7_4=0, Card7_5=0, Card7_6=0, Card7_7=0, Stack_card_open = 0, Cards_group = 0, mode = False):
        self.mode = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("#MainWindow { border-image: url(background_table.jpg) 0 0 0 0 stretch stretch; }")
        self.Card1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card1_1.setGeometry(QtCore.QRect(405, 30, 90, 120))
        self.Card1_1.setObjectName("Card1_1")
        self.Card2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card2_1.setGeometry(QtCore.QRect(350, 90, 90, 120))
        self.Card2_1.setObjectName("Card2_1")
        self.Card2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card2_2.setGeometry(QtCore.QRect(460, 90, 90, 120))
        self.Card2_2.setObjectName("Card2_2")
        self.Card3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card3_1.setGeometry(QtCore.QRect(290, 150, 90, 120))
        self.Card3_1.setObjectName("Card3_1")
        self.Card3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card3_2.setGeometry(QtCore.QRect(405, 150, 90, 120))
        self.Card3_2.setObjectName("Card3_2")
        self.Card3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card3_3.setGeometry(QtCore.QRect(520, 150, 90, 120))
        self.Card3_3.setObjectName("Card3_3")
        self.Card4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4_2.setGeometry(QtCore.QRect(350, 210, 90, 120))
        self.Card4_2.setObjectName("Card4_2")
        self.Card4_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4_3.setGeometry(QtCore.QRect(460, 210, 90, 120))
        self.Card4_3.setObjectName("Card4_3")
        self.Card4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4_1.setGeometry(QtCore.QRect(230, 210, 90, 120))
        self.Card4_1.setObjectName("Card4_1")
        self.Card4_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card4_4.setGeometry(QtCore.QRect(580, 210, 90, 120))
        self.Card4_4.setObjectName("Card4_4")
        self.Card5_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5_3.setGeometry(QtCore.QRect(405, 270, 90, 120))
        self.Card5_3.setObjectName("Card5_3")
        self.Card5_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5_1.setGeometry(QtCore.QRect(170, 270, 90, 120))
        self.Card5_1.setObjectName("Card5_1")
        self.Card5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5_2.setGeometry(QtCore.QRect(290, 270, 90, 120))
        self.Card5_2.setObjectName("Card5_2")
        self.Card5_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5_4.setGeometry(QtCore.QRect(520, 270, 90, 120))
        self.Card5_4.setObjectName("Card5_4")
        self.Card5_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card5_5.setGeometry(QtCore.QRect(640, 270, 90, 120))
        self.Card5_5.setObjectName("Card5_5")
        self.Card6_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_1.setGeometry(QtCore.QRect(110, 330, 90, 120))
        self.Card6_1.setObjectName("Card6_1")
        self.Card6_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_2.setGeometry(QtCore.QRect(230, 330, 90, 120))
        self.Card6_2.setObjectName("Card6_2")
        self.Card6_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_3.setGeometry(QtCore.QRect(350, 330, 90, 120))
        self.Card6_3.setObjectName("Card6_3")
        self.Card6_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_4.setGeometry(QtCore.QRect(460, 330, 90, 120))
        self.Card6_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.Card6_4.setObjectName("Card6_4")
        self.Card6_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_5.setGeometry(QtCore.QRect(580, 330, 90, 120))
        self.Card6_5.setObjectName("Card6_5")
        self.Card6_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Card6_6.setGeometry(QtCore.QRect(700, 330, 90, 120))
        self.Card6_6.setObjectName("Card6_6")
        self.Card7_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_1.setGeometry(QtCore.QRect(50, 390, 90, 120))
        self.Card7_1.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.Card7_1.setObjectName("Card7_1")
        self.Card7_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_6.setGeometry(QtCore.QRect(640, 390, 90, 120))
        self.Card7_6.setObjectName("Card7_6")
        self.Card7_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_5.setGeometry(QtCore.QRect(520, 390, 90, 120))
        self.Card7_5.setObjectName("Card7_5")
        self.Card7_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_4.setGeometry(QtCore.QRect(405, 390, 90, 120))
        self.Card7_4.setObjectName("Card7_4")
        self.Card7_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_3.setGeometry(QtCore.QRect(290, 390, 90, 120))
        self.Card7_3.setObjectName("Card7_3")
        self.Card7_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_2.setGeometry(QtCore.QRect(170, 390, 90, 120))
        self.Card7_2.setObjectName("Card7_2")
        self.Card7_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Card7_7.setGeometry(QtCore.QRect(760, 390, 90, 120))
        self.Card7_7.setObjectName("Card7_7")
        self.Cards_group = QtWidgets.QButtonGroup(self.centralwidget)
        self.Cards_group.setExclusive(True)
        self.Cards_group.addButton(self.Card1_1)
        self.Cards_group.addButton(self.Card2_1)
        self.Cards_group.addButton(self.Card2_2)
        self.Cards_group.addButton(self.Card3_1)
        self.Cards_group.addButton(self.Card3_2)
        self.Cards_group.addButton(self.Card3_3)
        self.Cards_group.addButton(self.Card4_1)
        self.Cards_group.addButton(self.Card4_2)
        self.Cards_group.addButton(self.Card4_3)
        self.Cards_group.addButton(self.Card4_4)
        self.Cards_group.addButton(self.Card5_1)
        self.Cards_group.addButton(self.Card5_2)
        self.Cards_group.addButton(self.Card5_3)
        self.Cards_group.addButton(self.Card5_4)
        self.Cards_group.addButton(self.Card5_5)
        self.Cards_group.addButton(self.Card6_1)
        self.Cards_group.addButton(self.Card6_2)
        self.Cards_group.addButton(self.Card6_3)
        self.Cards_group.addButton(self.Card6_4)
        self.Cards_group.addButton(self.Card6_5)
        self.Cards_group.addButton(self.Card6_6)
        self.Cards_group.addButton(self.Card7_1)
        self.Cards_group.addButton(self.Card7_2)
        self.Cards_group.addButton(self.Card7_3)
        self.Cards_group.addButton(self.Card7_4)
        self.Cards_group.addButton(self.Card7_5)
        self.Cards_group.addButton(self.Card7_6)
        self.Cards_group.addButton(self.Card7_7)
        self.Score_text = QtWidgets.QLabel(self.centralwidget)
        self.Score_text.setGeometry(QtCore.QRect(790, 530, 41, 16))
        self.Score_text.setTextFormat(QtCore.Qt.RichText)
        self.Score_text.setObjectName("Score_text")
        self.Score_number = QtWidgets.QLabel(self.centralwidget)
        self.Score_number.setGeometry(QtCore.QRect(830, 528, 61, 20))
        self.Score_number.setTextFormat(QtCore.Qt.RichText)
        self.Score_number.setObjectName("Score_number")
        self.Stack_card_close = QtWidgets.QPushButton(self.centralwidget)
        self.Stack_card_close.setGeometry(QtCore.QRect(40, 30, 90, 120))
        self.Stack_card_close.setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n"
                                             "font: 20pt \"MS Shell Dlg 2\";")
        self.Stack_card_close.setObjectName("Stack_card_close")
        self.Stack_card_open = QtWidgets.QPushButton(self.centralwidget)
        self.Stack_card_open.setGeometry(QtCore.QRect(150, 30, 90, 120))
        self.Stack_card_open.setObjectName("Stack_card_open")
        self.Cards_group.addButton(self.Stack_card_open)
        self.Hint = QtWidgets.QLabel(self.centralwidget)
        self.Hint.setGeometry(QtCore.QRect(20, 528, 181, 20))
        self.Hint.setObjectName("Hint")
        self.Combinations = QtWidgets.QLabel(self.centralwidget)
        self.Combinations.setGeometry(QtCore.QRect(710, 10, 161, 211))
        self.Combinations.setObjectName("Combinations")
        self.Winner = QtWidgets.QLabel(self.centralwidget)
        self.Winner.setGeometry(QtCore.QRect(16, 112, 861, 331))
        self.Winner.setObjectName("Winner")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_game = QtWidgets.QAction(MainWindow)
        self.actionNew_game.setObjectName("actionNew_game")
        self.actionRules = QtWidgets.QAction(MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.actionMode = QtWidgets.QAction(MainWindow)
        self.actionMode.setObjectName("actionMode")
        self.menuMenu.addAction(self.actionNew_game)
        self.menuMenu.addAction(self.actionRules)
        self.menuMenu.addAction(self.actionMode)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.Winner.hide()
        self.actionRules.triggered.connect(self.rules)
        self.actionMode.triggered.connect(self.view)
        self.retranslateUi(MainWindow)
        self.Stack_card_open.hide()
        self.Stack_card_close.clicked.connect(self.Stack_card_open.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyramid"))
        self.Score_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Score: </span></p></body></html>"))
        self.Score_number.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
        self.Stack_card_close.setText(_translate("MainWindow", "Stack"))
        self.Hint.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">You have 0 point(s). 13 point(s) left.</span></p></body></html>"))
        self.Combinations.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Combinations:</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Q + A</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">J + 2</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">10 + 3</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">9 + 4</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">8 + 5</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">7 + 6</span></p></body></html>"))
        self.Winner.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#fbe40d;\">CONGRATULATIONS</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#fbe40d;\">YOU WON</span></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew_game.setText(_translate("MainWindow", "New game"))
        self.actionNew_game.setStatusTip(_translate("MainWindow", "Start new game"))
        self.actionNew_game.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionMode.setText(_translate("MainWindow", "Change mode"))
        self.actionMode.setStatusTip(_translate("MainWindow", "Change interface's view"))
        self.actionMode.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionRules.setStatusTip(_translate("MainWindow", "Show rules"))
        self.actionRules.setShortcut(_translate("MainWindow", "Ctrl+R"))

    def rules(self):
        rules_window = QtWidgets.QDialog()
        ui = Ui_Rules()
        ui.setupUi(rules_window)
        rules_window.exec()
        rules_window.show()

    def view(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        if self.mode:
            self.mode = False
        else:
            self.mode = True
        if self.mode:
            self.centralwidget.setStyleSheet("#centralwidget { border-image: url(black_background.png) 0 0 0 0 stretch stretch; }")
            self.statusbar.setStyleSheet("#statusbar { border-image: url(black_background.png) 0 0 0 0 stretch stretch; }")
            self.Score_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d3d3d3 ;\">Score: </span></p></body></html>"))
            self.Score_number.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d3d3d3;\">0</span></p></body></html>"))
            self.Hint.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d3d3d3;\">You have 0 point(s). 13 point(s) left.</span></p></body></html>"))
            self.Combinations.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#d3d3d3;\">Combinations:</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">Q + A</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">J + 2</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">10 + 3</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">9 + 4</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">8 + 5</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#d3d3d3;\">7 + 6</span></p></body></html>"))
            self.Stack_card_close.setStyleSheet("background-color: #4C516D;\n" "color: rgb(0, 0, 0);\n"
                                                "font: 20pt \"MS Shell Dlg 2\";")
        else:
            self.centralwidget.setStyleSheet("#centralwidget { border-image: url(background_table.jpg) 0 0 0 0 stretch stretch; }")
            self.statusbar.setStyleSheet("#statusbar { border-image: url(background_table.jpg) 0 0 0 0 stretch stretch; }")
            self.Score_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Score: </span></p></body></html>"))
            self.Score_number.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">0</span></p></body></html>"))
            self.Hint.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">You have 0 point(s). 13 point(s) left.</span></p></body></html>"))
            self.Combinations.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Combinations:</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Q + A</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">J + 2</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">10 + 3</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">9 + 4</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">8 + 5</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">7 + 6</span></p></body></html>"))
            self.Stack_card_close.setStyleSheet("background-color: white;\n" "color: rgb(0, 0, 0);\n"
                                                 "font: 20pt \"MS Shell Dlg 2\";")



class Ui_Rules(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 550)
        Dialog.setMinimumSize(QtCore.QSize(480, 550))
        Dialog.setMaximumSize(QtCore.QSize(480, 550))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        Dialog.setStyleSheet("#Dialog { border-image: url(scroll_background.jpg) 0 0 0 0 stretch stretch; }")
        self.rules_text = QtWidgets.QLabel(Dialog)
        self.rules_text.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.rules_text.setTextFormat(QtCore.Qt.MarkdownText)
        self.rules_text.setScaledContents(False)
        self.rules_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rules_text.setWordWrap(True)
        self.rules_text.setObjectName("rules_text")
        self.verticalLayout.addWidget(self.rules_text)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rules"))
        self.rules_text.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">PYRAMID</p><p>Rules: The object of the game is to remove pairs of cards that add up to the total of the highest card in the deck from a pyramid arrangement of 28 cards.</p><p>It usually uses the standard 52-card deck, Jacks value at 11, Queens 12, and Kings 13.</p><p>To set up the pyramid, one card is dealt face up at the top of the playing area, then two cards beneath and partially covering it, then three beneath them, and so on completing with a row of seven cards for a total of 28 cards dealt. The remaining cards are placed to the side face down. This is the Stock.</p><p>To play, pairs of exposed cards can be removed to the Foundation if their values total 13. Thus, kings can be removed immediately to the Foundation. Cards must not be covered. Thus when an Ace rests on a Queen, that Queen can not be removed.</p><p>You may draw cards from the Stock one at a time and match it with any exposed card. If no match is made the drawn Stock card is still discarded into the Foundation.</p><p>Once the Stock is exhausted and/or no more pairs can be made, the game ends.</p><p>To score, count the number of remaining face up cards in the pyramid. A perfect score is therefore zero, where all cards have been matched into the Foundation.</p></body></html>"))