# Generated from C:/Users/saba/Downloads/compiler-02/TypeChecker.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,76,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,5,7,42,8,7,10,
        7,12,7,45,9,7,1,7,1,7,1,8,4,8,50,8,8,11,8,12,8,51,1,9,5,9,55,8,9,
        10,9,12,9,58,9,9,1,9,1,9,4,9,62,8,9,11,9,12,9,63,1,10,4,10,67,8,
        10,11,10,12,10,68,1,10,1,10,1,11,1,11,1,11,1,11,1,43,0,12,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,2,1,0,48,
        57,2,0,9,9,32,32,80,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,0,
        0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,33,1,0,0,0,11,35,1,0,0,0,13,37,1,
        0,0,0,15,39,1,0,0,0,17,49,1,0,0,0,19,56,1,0,0,0,21,66,1,0,0,0,23,
        72,1,0,0,0,25,26,5,40,0,0,26,2,1,0,0,0,27,28,5,41,0,0,28,4,1,0,0,
        0,29,30,5,43,0,0,30,6,1,0,0,0,31,32,5,45,0,0,32,8,1,0,0,0,33,34,
        5,42,0,0,34,10,1,0,0,0,35,36,5,47,0,0,36,12,1,0,0,0,37,38,5,61,0,
        0,38,14,1,0,0,0,39,43,5,34,0,0,40,42,9,0,0,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,44,1,0,0,0,43,41,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,34,0,0,47,16,1,0,0,0,48,50,7,0,0,0,49,48,1,0,0,0,50,51,1,
        0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,18,1,0,0,0,53,55,7,0,0,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,61,5,46,0,0,60,62,7,0,0,0,61,60,1,0,0,0,62,63,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,20,1,0,0,0,65,67,7,1,0,0,
        66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,70,1,
        0,0,0,70,71,6,10,0,0,71,22,1,0,0,0,72,73,5,10,0,0,73,74,1,0,0,0,
        74,75,6,11,1,0,75,24,1,0,0,0,6,0,43,51,56,63,68,2,0,1,0,6,0,0
    ]

class TypeCheckerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Plus = 3
    MINUS = 4
    MUL = 5
    DIVIDE = 6
    ASSIGN = 7
    STRING = 8
    INTEGER = 9
    FLOAT = 10
    Whitespace = 11
    Newline = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'='", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", "STRING", "INTEGER", 
            "FLOAT", "Whitespace", "Newline" ]

    ruleNames = [ "T__0", "T__1", "Plus", "MINUS", "MUL", "DIVIDE", "ASSIGN", 
                  "STRING", "INTEGER", "FLOAT", "Whitespace", "Newline" ]

    grammarFileName = "TypeChecker.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


