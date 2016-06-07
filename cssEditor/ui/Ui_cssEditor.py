# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/04_WORKSPACE/perso/cssEditor\ui\Ui_cssEditor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_cssEditor(object):
    def setupUi(self, cssEditor):
        cssEditor.setObjectName(_fromUtf8("cssEditor"))
        cssEditor.resize(886, 672)
        self.horizontalLayout = QtGui.QHBoxLayout(cssEditor)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(cssEditor)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ly_css = QtGui.QVBoxLayout(self.frame)
        self.ly_css.setMargin(2)
        self.ly_css.setSpacing(4)
        self.ly_css.setObjectName(_fromUtf8("ly_css"))
        self.tw_css = QtGui.QTreeWidget(self.frame)
        self.tw_css.setColumnCount(3)
        self.tw_css.setObjectName(_fromUtf8("tw_css"))
        self.tw_css.header().setCascadingSectionResizes(True)
        self.ly_css.addWidget(self.tw_css)
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.ly_edit = QtGui.QVBoxLayout(self.frame_2)
        self.ly_edit.setMargin(2)
        self.ly_edit.setSpacing(4)
        self.ly_edit.setObjectName(_fromUtf8("ly_edit"))
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(cssEditor)
        QtCore.QMetaObject.connectSlotsByName(cssEditor)

    def retranslateUi(self, cssEditor):
        cssEditor.setWindowTitle(_translate("cssEditor", "CssEditor", None))
        self.tw_css.headerItem().setText(0, _translate("cssEditor", "Object", None))
        self.tw_css.headerItem().setText(1, _translate("cssEditor", "attribut", None))
        self.tw_css.headerItem().setText(2, _translate("cssEditor", "value", None))

