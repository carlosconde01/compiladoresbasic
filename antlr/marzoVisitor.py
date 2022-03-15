# Generated from /Users/carlosconde/Desktop/marzo/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#start.
    def visitStart(self, ctx:marzoParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#sentence.
    def visitSentence(self, ctx:marzoParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#var_decl.
    def visitVar_decl(self, ctx:marzoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#var_assign.
    def visitVar_assign(self, ctx:marzoParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#println.
    def visitPrintln(self, ctx:marzoParser.PrintlnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#expression.
    def visitExpression(self, ctx:marzoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiplicacion.
    def visitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#division.
    def visitDivision(self, ctx:marzoParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#comparison.
    def visitComparison(self, ctx:marzoParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifsinelse.
    def visitIfsinelse(self, ctx:marzoParser.IfsinelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifconelse.
    def visitIfconelse(self, ctx:marzoParser.IfconelseContext):
        return self.visitChildren(ctx)



del marzoParser