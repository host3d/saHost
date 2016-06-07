__author__ = 'host3d'
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from core import *
from ui.Ui_cssEditor import Ui_cssEditor
from ui.cssQTreeWidget import CssQTreeWidget



class CssEditor(QWidget,Ui_cssEditor):
    def __init__(self, parent=None):
        super(CssEditor, self).__init__(parent)

        self.setupUi(self)

        self.cssPath = os.path.join(os.path.dirname(__file__), 'ui', 'style.qss')
        self.css = {}

        self.importCss()
        self.showCss()

    def importCss(self):
        self.css = cssToDict(self.cssPath)

    def showCss(self):
        self.tw_css.clear()

        root = self.tw_css.invisibleRootItem()

        for objName, attrs in self.css.items():
            obj = QTreeWidgetItem()
            obj.setText(0, objName)
            for attrName, value in attrs.items():
                attr = QTreeWidgetItem()
                attr.setText(1, attrName)
                attr.setText(2, value)
                obj.addChild(attr)

            root.addChild(obj)






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = CssEditor()
    win.show()
    sys.exit(app.exec_())
