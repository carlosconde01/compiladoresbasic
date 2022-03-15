from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser


class GenCode(marzoListener):

    # def __init__(self):
    # self. dictionary = {}

    def enterProgram(self, ctx: marzoParser.ProgramContext):
        print(".data")

    def exitVar_decl(self, ctx: marzoParser.Var_declContext):
        print(ctx.ID().getText() + ': .space 10')
        # self.dictionary.values

    def exitVar_assign(self, ctx: marzoParser.Var_assignContext):
        # print('li $t0, ' + ctx.expression().getText())
        # print('simbolo')
        # print(ctx.ID().getText())
        # print('valor')
        # print(marzoParser.symbolTable[ctx.ID().getText()])
        # print(marzoParser.symbolTable[ctx.expression().getText()])

        print(
            'li ' + ctx.ID().getText() + ', ' + str(marzoParser.symbolTable[ctx.ID().getText()]))

        # print(ctx.ID().getText())

    def exitPrintln(self, ctx: marzoParser.PrintlnContext):
        print('li $v0, 4')
        print('la $a0, ' + ctx.expression().getText())
        print('syscall')

    def exitSuma(self, ctx: marzoParser.SumaContext):

        print('add ' + ctx.ID().getText() + ', ' +
              str(ctx.NUMBER()[0]) + ', ' + str(ctx.NUMBER()[1]))

    def exitResta(self, ctx: marzoParser.RestaContext):
        print('sub ' + ctx.ID().getText() + ', ' +
              str(ctx.NUMBER()[0]) + ', ' + str(ctx.NUMBER()[1]))

    def exitMultiplicacion(self, ctx: marzoParser.MultiplicacionContext):
        print('mul ' + ctx.ID().getText() + ', ' +
              str(ctx.NUMBER()[0]) + ', ' + str(ctx.NUMBER()[1]))

    def exitDivision(self, ctx: marzoParser.DivisionContext):
        print('div ' + ctx.ID().getText() + ', ' +
              str(ctx.NUMBER()[0]) + ', ' + str(ctx.NUMBER()[1]))

    def enterIfsinelse(self, ctx: marzoParser.IfsinelseContext):
        print('conditionTrue: ')

    def exitIfsinelse(self, ctx: marzoParser.IfsinelseContext):
        comparisonType = ctx.comparison().getText()
        if comparisonType == '>':
            print('bgt ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '<':
            print('blt ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '>=':
            print('bge ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '<=':
            print('ble ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '==':
            print('beq ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '!=':
            print('bne ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')

    def enterIfconelse(self, ctx: marzoParser.IfconelseContext):
        print('conditionTrue:')

    def exitIfconelse(self, ctx: marzoParser.IfconelseContext):
        comparisonType = ctx.comparison().getText()
        if comparisonType == '>':
            print('bgt ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '<':
            print('blt ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '>=':
            print('bge ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '<=':
            print('ble ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '==':
            print('beq ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')
        elif comparisonType == '!=':
            print('bne ' + str(ctx.NUMBER()[0]) + ', ' +
                  str(ctx.NUMBER()[1]) + ', conditionTrue')

        # print(ctx.sentence2()[0].getText())
        #print('conditionTrue: ')
        # print(ctx.sentence()[0].getText())
        # for i in ctx.sentence():
        #  print(ctx.sentence()[i])

        # def exitPrimaria(self, ctx: marzoParser.PrimariaContext):
        #     print("load $1, " + ctx.Numero().getText())

        # def exitSuma(self, ctx: marzoParser.SumaContext):
        #     print("ADD")
