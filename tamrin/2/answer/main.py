from antlr4 import *
from gen.JavaParser import JavaParser
from gen.JavaLexer import JavaLexer
from Code.JavaLexer import VariableListener


def main():
    path_to_file = input("Please enter the path to file:expression: ")
    input_stream = FileStream(path_to_file)
    lexer = JavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    parse_tree = parser.compilationUnit()
    my_listener = VariableListener()
    walker = ParseTreeWalker()

    try:
        walker.walk(my_listener, parse_tree)
    except Exception as e:
        print(e)

# Call the main function
if __name__ == '__main__':
    main()
