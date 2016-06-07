from PyQt4 import uic
import os

if __name__ == '__main__':

    for root,dirs,files in os.walk(os.path.dirname(os.path.dirname(__file__))):
        for f in files:
            if f.endswith('.ui'):
                print root
                uic.compileUiDir(root)
                break
    print "done"