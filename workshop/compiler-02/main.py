from antlr4 import *
from Gen.TypeCheckerLexer import TypeCheckerLexer
from Gen.TypeCheckerParser import TypeCheckerParser
from Code.TypeListener import TypeListener
from io import StringIO


def main():
    input_expression = input("Enter an expression: ")

    lexer = TypeCheckerLexer(InputStream(input_expression))

    token_stream = CommonTokenStream(lexer)

    parser = TypeCheckerParser(token_stream)

    parse_tree = parser.start()

    listener = TypeListener()

    walker = ParseTreeWalker()
    try:
        walker.walk(listener, parse_tree)
        typeResult = listener.type
        print(typeResult)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
