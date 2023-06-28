from antlr4 import *
from Lexico import Lexico
from SintaticoParser import SintaticoParser
import re

def removeComments(codigo):
    pattern = r'\/\*[\s\S]*?\*\/|\/\/.*'
    return re.sub(pattern, '', codigo)

with open('teste.txt', 'r') as myfile:
    data = removeComments(myfile.read())

lexer = Lexico(InputStream(data))
stream = CommonTokenStream(lexer)

parser = SintaticoParser(stream)
tree = parser.program()

with open('arvore.txt', 'w') as treefile:
    treefile.write(tree.toStringTree(recog=parser))
    treefile.close()

