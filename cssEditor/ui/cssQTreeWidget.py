__author__ = 'host3d'
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CssQTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super(CssQTreeWidget, self).__init__(parent)