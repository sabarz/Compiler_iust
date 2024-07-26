import antlr4
from antlr4 import *
from grammers.soal1Lexer import soal1Lexer
from grammers.soal1Parser import soal1Parser
from grammers.soal1Listener import soal1Listener



class DepthListener(soal1Listener):
    def __init__(self):
        self.depth = 0
        self.max_depth = 0

    def enterIfStatement(self, ctx: soal1Parser.IfStatementContext):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    def exitIfStatement(self, ctx: soal1Parser.IfStatementContext):
        self.depth -= 1

    def enterWhileStatement(self, ctx: soal1Parser.WhileStatementContext):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    def exitWhileStatement(self, ctx: soal1Parser.WhileStatementContext):
        self.depth -= 1


def main():
    input_address = input('Enter the f..... address : ')
    file_stream = FileStream(input_address)
    lexer = soal1Lexer(file_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = soal1Parser(stream)

    tree = parser.start()

    listener = DepthListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    print(f"Maximum depth of code: {listener.max_depth}")


if __name__ == '__main__':
    main()
