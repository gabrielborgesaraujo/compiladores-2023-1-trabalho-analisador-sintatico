from antlr4 import *
from Lexico import Lexico
from SintaticoParser import SintaticoParser
import re
from geradorCodigoPython import *
from antlr4.CommonTokenFactory import CommonToken

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
        self.pilha = []
        self.identacao = 0
        
    def visitTerminal(self, node):
        token = node.getSymbol()
        token_type = token.type
        token_text = token.text
        
        
        next_token_index = self.next_token_index + 1
        if next_token_index < len(self.token_stream.tokens):
            next_token = self.token_stream.tokens[next_token_index]
        else:
            next_token = None

        if ";" in token_text:
            token_text.replace(";", "")
        
        if token_type == Lexico.FUN:
            self.pilha.append("def ")
            return "def "
        if token_type == Lexico.VAR:
            self.pilha.append("var")
            return ""
        elif token_type == Lexico.IDENTIFIER:
            self.pilha.append(token_text)
            return token_text
        elif token_type == Lexico.NUMBER:
            self.pilha.append(token_text)
            return token_text
        elif token_type == Lexico.STRING:
            self.pilha.append(token_text)
            return f'"{token_text[1:-1]}"'
        elif token_type == Lexico.PLUS:
            self.pilha.append("+")
            return "+"
        elif token_type == Lexico.MINUS:
            self.pilha.append("-")
            return "-"
        elif token_type == Lexico.OPEN_BRACE:
            self.pilha.append("{")
            return ":\n"
        elif token_type == Lexico.CLOSE_BRACE:
            self.pilha.append("}")
            return ""
        elif token_type == Lexico.RETURN:
            self.pilha.append("return ")
            return "return "
        elif token_type == Lexico.COMMA:
            self.pilha.append(", ")
            return ", "
        elif token_type == Lexico.SEMICOLON:
            self.pilha.append(";")
            return ");\n"
        elif token_type == Lexico.ASSIGN:
            self.pilha.append(" = ")
            return " = "
        elif token_type == Lexico.OPEN_PAREN:
            self.pilha.append("(")
            return "("
        elif token_type == Lexico.CLOSE_PAREN:
            self.pilha.append(")")
            if next_token.type == Lexico.SEMICOLON:
                self.pilha.append("\n")
                return ")\n"
            return ")"
        elif token_type == Lexico.IF:
            if self.pilha[-1] == "else":
                self.pilha.append("if ")
                return ""
            self.pilha.append("if ")
            return "if "
        elif token_type == Lexico.ELSE:
            self.next_token_index = self.token_stream.tokens.index(token)+1
            next_token = self.token_stream.tokens[self.next_token_index]
            if next_token.type == Lexico.IF:
                self.pilha.append("else")
                return "elif "
            self.pilha.append("else")
            return "else"
        elif token_type == Lexico.AND:
            self.pilha.append(" and ")
            return " and "
        elif token_type == Lexico.OR:
            self.pilha.append(" or ")
            return " or "
        elif token_type == Lexico.EQUAL:
            self.pilha.append(" == ")
            return " == "
        elif token_type == Lexico.NOT_EQUAL:
            self.pilha.append(" != ")
            return " != "
        elif token_type == Lexico.LESS_THAN:
            self.pilha.append(" < ")
            return " < "
        elif token_type == Lexico.GREATER_THAN:
            self.pilha.append(" > ")
            return " > "
        elif token_type == Lexico.GREATER_EQUAL:
            self.pilha.append(" >= ")
            return " >= "
        elif token_type == Lexico.LESS_EQUAL:
            self.pilha.append(" <= ")
            return " <= "
        elif token_type == Lexico.COMMENT:
            return ""
        elif token_type == Lexico.DOT:
            self.pilha.append(".")
            return "."
        elif token_type == Lexico.FOR:
            self.pilha.append("for ")
            return "for "
        elif token_type == Lexico.MODULO:
            self.pilha.append(" % ")
            return " % "
        elif token_type == Lexico.FALSE:
            self.pilha.append("False")
            return "False"
        elif token_type == Lexico.TRUE:
            self.pilha.append("True")
            return "True"
        elif token_type == Lexico.WHILE:
            self.pilha.append("while ")
            return "while "
        elif token_type == Lexico.MULTIPLY:
            self.pilha.append(" * ")
            return " * "
        elif token_type == Lexico.SLASH:
            self.pilha.append(" / ")
            return " / "
        elif token_type == Lexico.NIL:
            self.pilha.append("None")
            return "None"
        elif token_type == Lexico.NOT:
            self.pilha.append("not ")
            return "not "
        elif token_type == Lexico.PRINT:   
            self.pilha.append("print")
            return "print("
   

        return None

    def visitChildren(self, node):
        result = ""
        for child in node.getChildren():
            child_result = child.accept(self)
            if child_result is not None:
                result += child_result           
        return result


import re    
visitor = CodeGeneratorVisitor(stream)
codePythonString = visitor.visit(tree)
def remove_double_parenthesis_semicolon(string):
    pattern = r'\)\);|\);'
    result = re.sub(pattern, ')', string)
    return result

def check_unnecessary_parentheses(code):
    stack = []
    unnecessary_indices = []

    for i, char in enumerate(code):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                unnecessary_indices.append(i)

    # Adiciona os índices dos parênteses de abertura sem correspondência
    unnecessary_indices.extend(stack)

    return unnecessary_indices

def format_code(code):
    unnecessary_indices = check_unnecessary_parentheses(code)
    formatted_code = ""

    for i, char in enumerate(code):
        if i not in unnecessary_indices:
            formatted_code += char

    return formatted_code

with open('codigoPython.txt', 'w') as codefile:
    codefile.write(format_code(remove_double_parenthesis_semicolon(codePythonString)))
    codefile.close()