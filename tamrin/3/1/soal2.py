from antlr4 import *
from grammers.soal1Lexer import soal1Lexer
import os

input_address=input('Enter the f..... address : ')
file_stream=FileStream(input_address)

lexer=soal1Lexer(file_stream)
token=lexer.nextToken()
refactoredSTR=''

fname = 'razi'
sh = '99521316'

while token.type != Token.EOF:
    if token.type == lexer.COMMENT:
        hold = token.text[1:].strip()
        refactoredSTR += f'#{fname} {hold} {sh}\n'
    else:
        refactoredSTR += token.text
    token = lexer.nextToken()


print(refactoredSTR+'\n')