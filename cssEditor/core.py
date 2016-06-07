__author__ = 'host3d'
import os

from pprint import pprint as pp


def getCssData(path):
    res = ''
    if not os.path.exists(path):
        print "File %s doesn't exists !"
        return res

    with open(path, 'r') as f:
        res = f.readlines()
    return res

def cleanSpace(var):
    if var.startswith(' '):
        while var.startswith(' '):
            var = var[1:]

    if var.endswith(' '):
        while var.endswith(' '):
            var = var[:-1]
    return var

def cssToDict(path):
    css = getCssData(path)
    res = {}

    if not css:
        return res

    tmp = []
    objs = []
    attr = ''
    value = ''
    isAttr = False
    isCmt = False

    lines = []
    for l in css:
        #Clean comment
        if '//' in l:
            l = l.split('//')[0]
        if '/*' in l:
            l = l.split('/*')[0]
            isCmt = True
            lines.append(l)
        if '*/' in l:
            l = l.split('*/')[-1]
            isCmt = False

        l = l.replace('\n', '')
        if not l or isCmt:
            continue
        lines.append(l)

    for i, l in enumerate(lines):
        if '{' in l:
            isAttr = True
            if not tmp:
                for s in l.split('{'):
                    if s:
                        tmp.append(s)
            objs = [cleanSpace(x) for x in tmp[0].split(',')]
            for obj in objs:
                if not obj in res:
                    res[obj] = {}
        elif '}' in l:
            isAttr = False
            tmp = []
            objs = []
            attr = ''
            value = ''
        else:
            if isAttr:
                l = cleanSpace(l)
                if ':' in l and not attr:
                    ls = l.split(':')
                    attr = cleanSpace(ls[0])
                    value = ':'.join(ls[1:])
                if ';' in l:
                    if not ';' in value:
                        value += cleanSpace(l)
                    for obj in objs:
                        res[obj][attr] = cleanSpace(value).replace(';', '')
                    attr = ''
                else:
                    if not attr in l:
                        value += cleanSpace(l)
            else:
                tmp.append(l)
    return res



if __name__ == '__main__':

    cssPath = os.path.join(os.path.dirname(__file__), 'ui', 'style.qss')

    #TEST getCssData
    if getCssData(cssPath):
        print("getCssData OK")
    else:
        print("getCssData :(")

    #TEST cssToDict
    test = cssToDict(cssPath)
    if test:
        print("cssToDict OK")
        #pp(test)
        print test["QMenuBar::item:pressed"]['background-color']
        #pp(test)
    else:
        print("cssToDict :(")
