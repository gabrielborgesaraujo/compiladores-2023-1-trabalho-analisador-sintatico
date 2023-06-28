from antlr4 import *
from Lexico import Lexico
from SintaticoParser import SintaticoParser
import re
from antlr4.tree.Trees import Trees

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


class TokenVisitor(ParseTreeVisitor):
    def visitTerminal(self, node):
        token = node.getSymbol()
        print(f"Token: {token.type}, Texto: {token.text}")

        # Retorne None para ignorar os nós filhos
        return None

    def visitChildren(self, node):
        # Percorra todos os nós filhos
        result = None
        for child in node.getChildren():
            child_result = child.accept(self)
            if child_result is not None:
                result = child_result

        return result
    
class CodeGeneratorVisitor(ParseTreeVisitor):
    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.next_token_index = 0
        
    def visitTerminal(self, node):
        token = node.getSymbol()
        token_type = token.type
        token_text = token.text
        
        
        next_token_index = self.next_token_index + 1
        if next_token_index < len(self.token_stream.tokens):
            next_token = self.token_stream.tokens[next_token_index]
        else:
            next_token = None

        if token_type == Lexico.FUN:
            return "def "
        if token_type == Lexico.VAR:
            return ""
        elif token_type == Lexico.IDENTIFIER:
            return token_text
        elif token_type == Lexico.NUMBER:
            return token_text
        elif token_type == Lexico.STRING:
            return f'"{token_text[1:-1]}"'
        elif token_type == Lexico.PLUS:
            return "+"
        elif token_type == Lexico.MINUS:
            return "-"
        elif token_type == Lexico.OPEN_BRACE:
            return ":\n"
        elif token_type == Lexico.CLOSE_BRACE:
            return ""
        elif token_type == Lexico.RETURN:
            return "return "
        elif token_type == Lexico.COMMA:
            return ", "
        elif token_type == Lexico.SEMICOLON:
            return ")\n"
        elif token_type == Lexico.ASSIGN:
            return " = "
        elif token_type == Lexico.OPEN_PAREN:
            return "("
        elif token_type == Lexico.CLOSE_PAREN:
            return ")"
        elif token_type == Lexico.IF:
            return "if "
        elif token_type == Lexico.ELSE:
            if next_token.type == Lexico.IF:
                return "elif "
            return "else"
        elif token_type == Lexico.AND:
            return " and "
        elif token_type == Lexico.OR:
            return " or "
        elif token_type == Lexico.EQUAL:
            return " == "
        elif token_type == Lexico.NOT_EQUAL:
            return " != "
        elif token_type == Lexico.LESS_THAN:
            return " < "
        elif token_type == Lexico.GREATER_THAN:
            return " > "
        elif token_type == Lexico.GREATER_EQUAL:
            return " >= "
        elif token_type == Lexico.LESS_EQUAL:
            return " <= "
        elif token_type == Lexico.COMMENT:
            return ""
        elif token_type == Lexico.DOT:
            return "."
        elif token_type == Lexico.FOR:
            return "for "
        elif token_type == Lexico.MODULO:
            return " % "
        elif token_type == Lexico.FALSE:
            return "False"
        elif token_type == Lexico.TRUE:
            return "True"
        elif token_type == Lexico.WHILE:
            return "while "
        elif token_type == Lexico.MULTIPLY:
            return " * "
        elif token_type == Lexico.SLASH:
            return " / "
        elif token_type == Lexico.NIL:
            return "None"
        elif token_type == Lexico.NOT:
            return "not "
        elif token_type == Lexico.PRINT:   
            if next_token and next_token.type == Lexico.IDENTIFIER or next_token.type == Lexico.NUMBER or next_token.type == Lexico.STRING: 
                return "print("
   

        return None

    def visitChildren(self, node):
        result = ""
        for child in node.getChildren():
            child_result = child.accept(self)
            if child_result is not None:
                result += child_result                
        return result
    
visitor = CodeGeneratorVisitor(stream)
print(visitor.visit(tree))