# Generated from E:/saba folder/univercity/term 7 4021/compiler/tamrin/3/1/grammers/soal1.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,77,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,87,
        8,7,10,7,12,7,90,9,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,0,
        1,14,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,2,0,8,9,17,18,1,0,10,
        11,1,0,12,14,1,0,15,16,97,0,27,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,
        6,43,1,0,0,0,8,48,1,0,0,0,10,54,1,0,0,0,12,60,1,0,0,0,14,76,1,0,
        0,0,16,91,1,0,0,0,18,93,1,0,0,0,20,95,1,0,0,0,22,97,1,0,0,0,24,26,
        3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,
        28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,38,3,4,
        2,0,33,38,3,6,3,0,34,38,3,8,4,0,35,38,3,10,5,0,36,38,3,12,6,0,37,
        32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,
        0,38,3,1,0,0,0,39,40,3,22,11,0,40,41,5,19,0,0,41,42,5,23,0,0,42,
        5,1,0,0,0,43,44,5,19,0,0,44,45,5,1,0,0,45,46,3,14,7,0,46,47,5,23,
        0,0,47,7,1,0,0,0,48,49,5,2,0,0,49,50,5,3,0,0,50,51,3,14,7,0,51,52,
        5,4,0,0,52,53,3,2,1,0,53,9,1,0,0,0,54,55,5,5,0,0,55,56,5,3,0,0,56,
        57,3,14,7,0,57,58,5,4,0,0,58,59,3,2,1,0,59,11,1,0,0,0,60,64,5,6,
        0,0,61,63,3,2,1,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,
        1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,7,0,0,68,13,1,0,0,0,
        69,70,6,7,-1,0,70,77,3,16,8,0,71,77,5,19,0,0,72,73,5,3,0,0,73,74,
        3,14,7,0,74,75,5,4,0,0,75,77,1,0,0,0,76,69,1,0,0,0,76,71,1,0,0,0,
        76,72,1,0,0,0,77,88,1,0,0,0,78,79,10,3,0,0,79,80,3,18,9,0,80,81,
        3,14,7,4,81,87,1,0,0,0,82,83,10,2,0,0,83,84,3,20,10,0,84,85,3,14,
        7,3,85,87,1,0,0,0,86,78,1,0,0,0,86,82,1,0,0,0,87,90,1,0,0,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,15,1,0,0,0,90,88,1,0,0,0,91,92,7,0,0,0,
        92,17,1,0,0,0,93,94,7,1,0,0,94,19,1,0,0,0,95,96,7,2,0,0,96,21,1,
        0,0,0,97,98,7,3,0,0,98,23,1,0,0,0,6,27,37,64,76,86,88
    ]

class soal1Parser ( Parser ):

    grammarFileName = "soal1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'('", "')'", "'while'", 
                     "'{'", "'}'", "'true'", "'false'", "'+'", "'-'", "'=='", 
                     "'<'", "'>'", "'int'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "' '", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IntegerLiteral", "BooleanLiteral", "Identifier", 
                      "COMMENT", "WS", "SPACE", "SEMICOL" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_assignmentStatement = 3
    RULE_ifStatement = 4
    RULE_whileStatement = 5
    RULE_compoundStatement = 6
    RULE_expression = 7
    RULE_literal = 8
    RULE_arithmeticOperator = 9
    RULE_comparisonOperator = 10
    RULE_type = 11

    ruleNames =  [ "start", "statement", "variableDeclaration", "assignmentStatement", 
                   "ifStatement", "whileStatement", "compoundStatement", 
                   "expression", "literal", "arithmeticOperator", "comparisonOperator", 
                   "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    IntegerLiteral=17
    BooleanLiteral=18
    Identifier=19
    COMMENT=20
    WS=21
    SPACE=22
    SEMICOL=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(soal1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(soal1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(soal1Parser.StatementContext,i)


        def getRuleIndex(self):
            return soal1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = soal1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 622692) != 0):
                self.state = 24
                self.statement()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(soal1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(soal1Parser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(soal1Parser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(soal1Parser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(soal1Parser.WhileStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(soal1Parser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return soal1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = soal1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.variableDeclaration()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.assignmentStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.ifStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.whileStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.compoundStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(soal1Parser.TypeContext,0)


        def Identifier(self):
            return self.getToken(soal1Parser.Identifier, 0)

        def SEMICOL(self):
            return self.getToken(soal1Parser.SEMICOL, 0)

        def getRuleIndex(self):
            return soal1Parser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = soal1Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.type_()
            self.state = 40
            self.match(soal1Parser.Identifier)
            self.state = 41
            self.match(soal1Parser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(soal1Parser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(soal1Parser.ExpressionContext,0)


        def SEMICOL(self):
            return self.getToken(soal1Parser.SEMICOL, 0)

        def getRuleIndex(self):
            return soal1Parser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = soal1Parser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(soal1Parser.Identifier)
            self.state = 44
            self.match(soal1Parser.T__0)
            self.state = 45
            self.expression(0)
            self.state = 46
            self.match(soal1Parser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(soal1Parser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(soal1Parser.StatementContext,0)


        def getRuleIndex(self):
            return soal1Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = soal1Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(soal1Parser.T__1)
            self.state = 49
            self.match(soal1Parser.T__2)
            self.state = 50
            self.expression(0)
            self.state = 51
            self.match(soal1Parser.T__3)
            self.state = 52
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(soal1Parser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(soal1Parser.StatementContext,0)


        def getRuleIndex(self):
            return soal1Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = soal1Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(soal1Parser.T__4)
            self.state = 55
            self.match(soal1Parser.T__2)
            self.state = 56
            self.expression(0)
            self.state = 57
            self.match(soal1Parser.T__3)
            self.state = 58
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(soal1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(soal1Parser.StatementContext,i)


        def getRuleIndex(self):
            return soal1Parser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = soal1Parser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(soal1Parser.T__5)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 622692) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(soal1Parser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(soal1Parser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(soal1Parser.Identifier, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(soal1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(soal1Parser.ExpressionContext,i)


        def arithmeticOperator(self):
            return self.getTypedRuleContext(soal1Parser.ArithmeticOperatorContext,0)


        def comparisonOperator(self):
            return self.getTypedRuleContext(soal1Parser.ComparisonOperatorContext,0)


        def getRuleIndex(self):
            return soal1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = soal1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 17, 18]:
                self.state = 70
                self.literal()
                pass
            elif token in [19]:
                self.state = 71
                self.match(soal1Parser.Identifier)
                pass
            elif token in [3]:
                self.state = 72
                self.match(soal1Parser.T__2)
                self.state = 73
                self.expression(0)
                self.state = 74
                self.match(soal1Parser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = soal1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 78
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 79
                        self.arithmeticOperator()
                        self.state = 80
                        self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = soal1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 83
                        self.comparisonOperator()
                        self.state = 84
                        self.expression(3)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(soal1Parser.IntegerLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(soal1Parser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return soal1Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = soal1Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 393984) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return soal1Parser.RULE_arithmeticOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticOperator" ):
                listener.enterArithmeticOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticOperator" ):
                listener.exitArithmeticOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperator" ):
                return visitor.visitArithmeticOperator(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticOperator(self):

        localctx = soal1Parser.ArithmeticOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arithmeticOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return soal1Parser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = soal1Parser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return soal1Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = soal1Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




