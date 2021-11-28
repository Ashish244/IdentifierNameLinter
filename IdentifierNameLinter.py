import TreeSitter.python.Internal
import TreeSitter.Language
import os
from os import path
from platform import system
from setuptools import Extension, setup
pythonLinks=[]
goLink=[]
javascriptLinks=[]
rubyLinks=[]
for f1, f2, f3 in os.walk(r'files_from_git'):
    for file in f3:
        if file.endswith('.py'):
            pythonLinks.append(os.path.join(f1, file))
        if file.endswith('.go'):
            goLink.append(os.path.join(f1, file))
        if file.endswith('.js'):
            javascriptLinks.append(os.path.join(f1, file))
        if file.endswith('.rb'):
            rubyLinks.append(os.path.join(f1, file))

        #if file.endswith('.js'):
            #javascriptLinks.append(os.path.join(f2, file))
        #if file.endswith('.rb'):
            #rubyLinks.append(os.path.join(f2, file))
i = 0
python_text=[]
Language.build_library('build/my-languages.so',
                       ['tree-sitter-go', 'tree-sitter-javascript', 'tree-sitter-python', 'tree-sitter-ruby'])
pythonparser=Parser()
PY_LANGUAGE=Language('build/my-languages.so','python')
pythonparser.set_language(PY_LANGUAGE)
def parser(source, parser1):
    list1=[]
    def node_parser(root1):
        if len(root1.children)!=0:
            for j in root1.children:
                if j.type=='identifier':
                    list1.append(j)
                node_parser(j)
                #list1.append(i)
        else:
            return
    Treename=parser1.parse(bytes(source, "utf8"))
    Root_node=Treename.Root_node
    node_parser(Root_node)
    return list1
    for i in range(len(python_text)):
         print("output for", pythonpaths[i])
        PythonList = parser(python_text[i], py_parser)
        code = python_text[i].split('\n')
        for e in PythonList:
            row=e.start_point[0]
            col=e.start_point[1]
             print(code[row][col:e.end_point[1]],"Row Num",row,"Column Num",col)