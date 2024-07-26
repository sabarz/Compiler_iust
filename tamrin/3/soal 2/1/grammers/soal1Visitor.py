# Generated from E:/saba folder/univercity/term 7 4021/compiler/tamrin/3/1/grammers/soal1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .soal1Parser import soal1Parser
else:
    from soal1Parser import soal1Parser

# This class defines a complete generic visitor for a parse tree produced by soal1Parser.

class soal1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by soal1Parser#start.
    def visitStart(self, ctx:soal1Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#statement.
    def visitStatement(self, ctx:soal1Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:soal1Parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:soal1Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#ifStatement.
    def visitIfStatement(self, ctx:soal1Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#whileStatement.
    def visitWhileStatement(self, ctx:soal1Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#compoundStatement.
    def visitCompoundStatement(self, ctx:soal1Parser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#expression.
    def visitExpression(self, ctx:soal1Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#literal.
    def visitLiteral(self, ctx:soal1Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:soal1Parser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#comparisonOperator.
    def visitComparisonOperator(self, ctx:soal1Parser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by soal1Parser#type.
    def visitType(self, ctx:soal1Parser.TypeContext):
        return self.visitChildren(ctx)



del soal1Parser