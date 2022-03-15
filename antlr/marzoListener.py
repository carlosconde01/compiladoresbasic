# Generated from /Users/carlosconde/Desktop/marzo/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#start.
    def enterStart(self, ctx:marzoParser.StartContext):
        pass

    # Exit a parse tree produced by marzoParser#start.
    def exitStart(self, ctx:marzoParser.StartContext):
        pass


    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#sentence.
    def enterSentence(self, ctx:marzoParser.SentenceContext):
        pass

    # Exit a parse tree produced by marzoParser#sentence.
    def exitSentence(self, ctx:marzoParser.SentenceContext):
        pass


    # Enter a parse tree produced by marzoParser#var_decl.
    def enterVar_decl(self, ctx:marzoParser.Var_declContext):
        pass

    # Exit a parse tree produced by marzoParser#var_decl.
    def exitVar_decl(self, ctx:marzoParser.Var_declContext):
        pass


    # Enter a parse tree produced by marzoParser#var_assign.
    def enterVar_assign(self, ctx:marzoParser.Var_assignContext):
        pass

    # Exit a parse tree produced by marzoParser#var_assign.
    def exitVar_assign(self, ctx:marzoParser.Var_assignContext):
        pass


    # Enter a parse tree produced by marzoParser#println.
    def enterPrintln(self, ctx:marzoParser.PrintlnContext):
        pass

    # Exit a parse tree produced by marzoParser#println.
    def exitPrintln(self, ctx:marzoParser.PrintlnContext):
        pass


    # Enter a parse tree produced by marzoParser#expression.
    def enterExpression(self, ctx:marzoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by marzoParser#expression.
    def exitExpression(self, ctx:marzoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#resta.
    def enterResta(self, ctx:marzoParser.RestaContext):
        pass

    # Exit a parse tree produced by marzoParser#resta.
    def exitResta(self, ctx:marzoParser.RestaContext):
        pass


    # Enter a parse tree produced by marzoParser#multiplicacion.
    def enterMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by marzoParser#multiplicacion.
    def exitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by marzoParser#division.
    def enterDivision(self, ctx:marzoParser.DivisionContext):
        pass

    # Exit a parse tree produced by marzoParser#division.
    def exitDivision(self, ctx:marzoParser.DivisionContext):
        pass


    # Enter a parse tree produced by marzoParser#comparison.
    def enterComparison(self, ctx:marzoParser.ComparisonContext):
        pass

    # Exit a parse tree produced by marzoParser#comparison.
    def exitComparison(self, ctx:marzoParser.ComparisonContext):
        pass


    # Enter a parse tree produced by marzoParser#ifsinelse.
    def enterIfsinelse(self, ctx:marzoParser.IfsinelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifsinelse.
    def exitIfsinelse(self, ctx:marzoParser.IfsinelseContext):
        pass


    # Enter a parse tree produced by marzoParser#ifconelse.
    def enterIfconelse(self, ctx:marzoParser.IfconelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifconelse.
    def exitIfconelse(self, ctx:marzoParser.IfconelseContext):
        pass



del marzoParser