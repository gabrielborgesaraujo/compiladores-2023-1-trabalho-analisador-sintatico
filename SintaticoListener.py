# Generated from Sintatico.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SintaticoParser import SintaticoParser
else:
    from SintaticoParser import SintaticoParser

# This class defines a complete listener for a parse tree produced by SintaticoParser.
class SintaticoListener(ParseTreeListener):

    # Enter a parse tree produced by SintaticoParser#program.
    def enterProgram(self, ctx:SintaticoParser.ProgramContext):
        pass

    # Exit a parse tree produced by SintaticoParser#program.
    def exitProgram(self, ctx:SintaticoParser.ProgramContext):
        pass


    # Enter a parse tree produced by SintaticoParser#declaration.
    def enterDeclaration(self, ctx:SintaticoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SintaticoParser#declaration.
    def exitDeclaration(self, ctx:SintaticoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SintaticoParser#funDecl.
    def enterFunDecl(self, ctx:SintaticoParser.FunDeclContext):
        pass

    # Exit a parse tree produced by SintaticoParser#funDecl.
    def exitFunDecl(self, ctx:SintaticoParser.FunDeclContext):
        pass


    # Enter a parse tree produced by SintaticoParser#varDecl.
    def enterVarDecl(self, ctx:SintaticoParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SintaticoParser#varDecl.
    def exitVarDecl(self, ctx:SintaticoParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SintaticoParser#statement.
    def enterStatement(self, ctx:SintaticoParser.StatementContext):
        pass

    # Exit a parse tree produced by SintaticoParser#statement.
    def exitStatement(self, ctx:SintaticoParser.StatementContext):
        pass


    # Enter a parse tree produced by SintaticoParser#exprStmt.
    def enterExprStmt(self, ctx:SintaticoParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#exprStmt.
    def exitExprStmt(self, ctx:SintaticoParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#forStmt.
    def enterForStmt(self, ctx:SintaticoParser.ForStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#forStmt.
    def exitForStmt(self, ctx:SintaticoParser.ForStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#ifStmt.
    def enterIfStmt(self, ctx:SintaticoParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#ifStmt.
    def exitIfStmt(self, ctx:SintaticoParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#printStmt.
    def enterPrintStmt(self, ctx:SintaticoParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#printStmt.
    def exitPrintStmt(self, ctx:SintaticoParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#returnStmt.
    def enterReturnStmt(self, ctx:SintaticoParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#returnStmt.
    def exitReturnStmt(self, ctx:SintaticoParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#whileStmt.
    def enterWhileStmt(self, ctx:SintaticoParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by SintaticoParser#whileStmt.
    def exitWhileStmt(self, ctx:SintaticoParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by SintaticoParser#block.
    def enterBlock(self, ctx:SintaticoParser.BlockContext):
        pass

    # Exit a parse tree produced by SintaticoParser#block.
    def exitBlock(self, ctx:SintaticoParser.BlockContext):
        pass


    # Enter a parse tree produced by SintaticoParser#expression.
    def enterExpression(self, ctx:SintaticoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SintaticoParser#expression.
    def exitExpression(self, ctx:SintaticoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SintaticoParser#assignment.
    def enterAssignment(self, ctx:SintaticoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SintaticoParser#assignment.
    def exitAssignment(self, ctx:SintaticoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SintaticoParser#logic_or.
    def enterLogic_or(self, ctx:SintaticoParser.Logic_orContext):
        pass

    # Exit a parse tree produced by SintaticoParser#logic_or.
    def exitLogic_or(self, ctx:SintaticoParser.Logic_orContext):
        pass


    # Enter a parse tree produced by SintaticoParser#logic_and.
    def enterLogic_and(self, ctx:SintaticoParser.Logic_andContext):
        pass

    # Exit a parse tree produced by SintaticoParser#logic_and.
    def exitLogic_and(self, ctx:SintaticoParser.Logic_andContext):
        pass


    # Enter a parse tree produced by SintaticoParser#equality.
    def enterEquality(self, ctx:SintaticoParser.EqualityContext):
        pass

    # Exit a parse tree produced by SintaticoParser#equality.
    def exitEquality(self, ctx:SintaticoParser.EqualityContext):
        pass


    # Enter a parse tree produced by SintaticoParser#comparison.
    def enterComparison(self, ctx:SintaticoParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SintaticoParser#comparison.
    def exitComparison(self, ctx:SintaticoParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SintaticoParser#term.
    def enterTerm(self, ctx:SintaticoParser.TermContext):
        pass

    # Exit a parse tree produced by SintaticoParser#term.
    def exitTerm(self, ctx:SintaticoParser.TermContext):
        pass


    # Enter a parse tree produced by SintaticoParser#factor.
    def enterFactor(self, ctx:SintaticoParser.FactorContext):
        pass

    # Exit a parse tree produced by SintaticoParser#factor.
    def exitFactor(self, ctx:SintaticoParser.FactorContext):
        pass


    # Enter a parse tree produced by SintaticoParser#unary.
    def enterUnary(self, ctx:SintaticoParser.UnaryContext):
        pass

    # Exit a parse tree produced by SintaticoParser#unary.
    def exitUnary(self, ctx:SintaticoParser.UnaryContext):
        pass


    # Enter a parse tree produced by SintaticoParser#call.
    def enterCall(self, ctx:SintaticoParser.CallContext):
        pass

    # Exit a parse tree produced by SintaticoParser#call.
    def exitCall(self, ctx:SintaticoParser.CallContext):
        pass


    # Enter a parse tree produced by SintaticoParser#primary.
    def enterPrimary(self, ctx:SintaticoParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SintaticoParser#primary.
    def exitPrimary(self, ctx:SintaticoParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SintaticoParser#arguments.
    def enterArguments(self, ctx:SintaticoParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by SintaticoParser#arguments.
    def exitArguments(self, ctx:SintaticoParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by SintaticoParser#function.
    def enterFunction(self, ctx:SintaticoParser.FunctionContext):
        pass

    # Exit a parse tree produced by SintaticoParser#function.
    def exitFunction(self, ctx:SintaticoParser.FunctionContext):
        pass


    # Enter a parse tree produced by SintaticoParser#parameters.
    def enterParameters(self, ctx:SintaticoParser.ParametersContext):
        pass

    # Exit a parse tree produced by SintaticoParser#parameters.
    def exitParameters(self, ctx:SintaticoParser.ParametersContext):
        pass



del SintaticoParser