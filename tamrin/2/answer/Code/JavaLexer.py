from gen.JavaParser import *


class VariableListener(ParseTreeListener):

    def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        variable_name = ctx.variableDeclaratorId().Identifier().getText()
        variable_type = ctx.parentCtx.parentCtx.children[0].getText()
        line_number = ctx.start.line

        if ctx.variableDeclaratorId().dims():
            print(f'line{line_number}:type:{variable_type}{ctx.variableDeclaratorId().dims().getText()}-name:{variable_name}')
        else:
            print(f'line{line_number}:type:{variable_type}-name:{variable_name}')


