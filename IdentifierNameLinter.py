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
i = 0
python_text=[]
while i<len(pythonLinks):
    with open(pythonLinks[i]) as op:
        try:
            contents = op.read()
            py_text.append(contents)
        except:
            pass
    i=i+1
Language.build_library('build/my-languages.so',
                       ['tree-sitter-go', 'tree-sitter-javascript', 'tree-sitter-python', 'tree-sitter-ruby'])
py_parser=Parser()
PYTHON_LANGUAGE=Language('build/my-languages.so', 'python')
py_parser.set_language(PYTHON_LANGUAGE)
def parser(source, parser1):
    list1 = []
    def node_parser(root1):
        if len(root1.children) != 0:
            for j in root1.children:
                if j.type == 'identifier':
                    list1.append(j)
                node_parser(j)
        else:
            return
    tree_name = parser1.parse(bytes(source, "utf8"))
    root_node = tree_name.root_node
    node_parser(root_node)
    return list1
    for i in range(len(py_text)):   //to print
         print("output for", py_paths[i])
        py_list = parser(py_text[i], py_parser)
        code = py_text[i].split('\n')
        ids = []
        for e in py_list:
            row = e.start_point[0]
            col = e.start_point[1]
             print(code[row][col:e.end_point[1]], "Row Num", row, " Column Num", col)