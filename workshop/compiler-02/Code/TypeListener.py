from antlr4 import *
from Gen.TypeCheckerListener import TypeCheckerListener


class TypeListener(TypeCheckerListener):
    def __init__(self):
        self.type = ""

    def get_type(self):
        return self.type

    def exitExpr1(self, ctx):

        if ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Integer":
            ctx.type = "Integer"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Integer":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "String" and ctx.getChild(2).type == "Integer":
            ctx.type = "String"

        elif ctx.getChild(0).type == "String" and ctx.getChild(2).type == "Float":
            ctx.type = "String"

        elif ctx.getChild(0).type == "String" and ctx.getChild(2).type == "String":
            ctx.type = "String"

        elif ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "String":
            raise Exception("string and integer can't come together")

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "String":
            raise Exception("float and integer can't come together")

        else:
            raise Exception("None")

        self.type = ctx.type

    def exitExpr2(self, ctx):

        if ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Integer":
            ctx.type = "Integer"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Integer":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "String" or ctx.getChild(2).type == "String":
            raise Exception("string can't be subtracted")

        self.type = ctx.type

    def exitExpr3(self, ctx):
        ctx.type = ctx.getChild(0).type

        self.type = ctx.type

    def exitTerm1(self, ctx):

        if ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Integer":
            ctx.type = "Integer"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Integer":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "String" or ctx.getChild(2).type == "String":
            raise Exception("string can't get multiplied")

        else:
            raise Exception("None")

    def exitTerm2(self, ctx):

        if ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Integer":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Integer" and ctx.getChild(2).type == "Float":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "Float" and ctx.getChild(2).type == "Integer":
            ctx.type = "Float"

        elif ctx.getChild(0).type == "String" or ctx.getChild(2).type == "String":
            raise Exception("string can't be divided")

        else:
            raise Exception("None")

    def exitTerm3(self, ctx):
        ctx.type = ctx.getChild(0).type

    def exitFactString(self, ctx):
        ctx.type = "String"

    def exitFactInteger(self, ctx):
        ctx.type = "Integer"

    def exitFactFloat(self, ctx):
        ctx.type = "Float"

    def exitFactExpr(self, ctx):
        ctx.type = ctx.getChild(1).type
