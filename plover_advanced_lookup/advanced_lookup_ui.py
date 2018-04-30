# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plover_advanced_lookup\advanced_lookup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdvancedLookup(object):
    def setupUi(self, AdvancedLookup):
        AdvancedLookup.setObjectName("AdvancedLookup")
        AdvancedLookup.resize(400, 430)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        AdvancedLookup.setFont(font)
        AdvancedLookup.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AdvancedLookup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.byTranslationLabel = QtWidgets.QLabel(AdvancedLookup)
        self.byTranslationLabel.setObjectName("byTranslationLabel")
        self.gridLayout.addWidget(self.byTranslationLabel, 2, 0, 1, 1)
        self.byTranslationText = QtWidgets.QPlainTextEdit(AdvancedLookup)
        self.byTranslationText.setReadOnly(True)
        self.byTranslationText.setObjectName("byTranslationText")
        self.gridLayout.addWidget(self.byTranslationText, 3, 0, 1, 1)
        self.inTranslationLabel = QtWidgets.QLabel(AdvancedLookup)
        self.inTranslationLabel.setObjectName("inTranslationLabel")
        self.gridLayout.addWidget(self.inTranslationLabel, 4, 0, 1, 1)
        self.inTranslationText = QtWidgets.QPlainTextEdit(AdvancedLookup)
        self.inTranslationText.setReadOnly(True)
        self.inTranslationText.setObjectName("inTranslationText")
        self.gridLayout.addWidget(self.inTranslationText, 5, 0, 1, 1)
        self.byStrokeLabel = QtWidgets.QLabel(AdvancedLookup)
        self.byStrokeLabel.setObjectName("byStrokeLabel")
        self.gridLayout.addWidget(self.byStrokeLabel, 2, 1, 1, 1)
        self.byStrokeText = QtWidgets.QPlainTextEdit(AdvancedLookup)
        self.byStrokeText.setReadOnly(True)
        self.byStrokeText.setObjectName("byStrokeText")
        self.gridLayout.addWidget(self.byStrokeText, 3, 1, 1, 1)
        self.inStrokeText = QtWidgets.QPlainTextEdit(AdvancedLookup)
        self.inStrokeText.setReadOnly(True)
        self.inStrokeText.setObjectName("inStrokeText")
        self.gridLayout.addWidget(self.inStrokeText, 5, 1, 1, 1)
        self.inStrokeLabel = QtWidgets.QLabel(AdvancedLookup)
        self.inStrokeLabel.setObjectName("inStrokeLabel")
        self.gridLayout.addWidget(self.inStrokeLabel, 4, 1, 1, 1)
        self.queryLabel = QtWidgets.QLabel(AdvancedLookup)
        self.queryLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.queryLabel.setObjectName("queryLabel")
        self.gridLayout.addWidget(self.queryLabel, 0, 0, 1, 1)
        self.searchInput = QtWidgets.QLineEdit(AdvancedLookup)
        self.searchInput.setObjectName("searchInput")
        self.gridLayout.addWidget(self.searchInput, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.action_Clear = QtWidgets.QAction(AdvancedLookup)
        icon = QtGui.QIcon()
        icon.addFile(":/trash.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Clear.setIcon(icon)
        self.action_Clear.setObjectName("action_Clear")
        self.action_ToggleOnTop = QtWidgets.QAction(AdvancedLookup)
        self.action_ToggleOnTop.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addFile(":/pin.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ToggleOnTop.setIcon(icon1)
        self.action_ToggleOnTop.setObjectName("action_ToggleOnTop")
        self.action_SelectFont = QtWidgets.QAction(AdvancedLookup)
        icon2 = QtGui.QIcon()
        icon2.addFile(":/font_selector.svg", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SelectFont.setIcon(icon2)
        self.action_SelectFont.setObjectName("action_SelectFont")

        self.retranslateUi(AdvancedLookup)
        self.action_Clear.triggered.connect(AdvancedLookup.on_clear)
        self.action_ToggleOnTop.triggered['bool'].connect(AdvancedLookup.on_toggle_ontop)
        self.action_SelectFont.triggered.connect(AdvancedLookup.on_select_font)
        self.searchInput.textEdited['QString'].connect(AdvancedLookup.on_lookup)
        QtCore.QMetaObject.connectSlotsByName(AdvancedLookup)
        AdvancedLookup.setTabOrder(self.searchInput, self.byTranslationText)
        AdvancedLookup.setTabOrder(self.byTranslationText, self.byStrokeText)
        AdvancedLookup.setTabOrder(self.byStrokeText, self.inTranslationText)
        AdvancedLookup.setTabOrder(self.inTranslationText, self.inStrokeText)

    def retranslateUi(self, AdvancedLookup):
        _translate = QtCore.QCoreApplication.translate
        AdvancedLookup.setWindowTitle(_translate("AdvancedLookup", "Plover: Suggestions"))
        self.byTranslationLabel.setText(_translate("AdvancedLookup", "By translation"))
        self.inTranslationLabel.setText(_translate("AdvancedLookup", "In translation"))
        self.byStrokeLabel.setText(_translate("AdvancedLookup", "By stroke"))
        self.inStrokeLabel.setText(_translate("AdvancedLookup", "In stroke"))
        self.queryLabel.setText(_translate("AdvancedLookup", "Search by translation or steno:"))
        self.searchInput.setPlaceholderText(_translate("AdvancedLookup", "word or STEPB/TPHO"))
        self.action_Clear.setText(_translate("AdvancedLookup", "&Clear"))
        self.action_Clear.setToolTip(_translate("AdvancedLookup", "Clear paper tape"))
        self.action_Clear.setShortcut(_translate("AdvancedLookup", "Ctrl+L"))
        self.action_ToggleOnTop.setText(_translate("AdvancedLookup", "&Toggle \"always on top\""))
        self.action_ToggleOnTop.setToolTip(_translate("AdvancedLookup", "Toggle \"always on top\""))
        self.action_ToggleOnTop.setShortcut(_translate("AdvancedLookup", "Ctrl+T"))
        self.action_SelectFont.setText(_translate("AdvancedLookup", "Select &font"))
        self.action_SelectFont.setToolTip(_translate("AdvancedLookup", "Open font selection dialog"))

from . import resources_rc
