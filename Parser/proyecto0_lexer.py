import ply.lex as lex
import re
import codecs
import os
import sys

import ply.lex as lex

# Lista de tokens
tokens = [
    # Palabras clave
    'DEFVAR',
    'DEFPROC',
    'LEAP',
    'WALK',
    'TURN',
    'TURNTO',
    'DROP',
    'GET',
    'GRAB',
    'LETGO',
    'NOP',

    # Otros tokens
    'ID',
    'NUMBER',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'DIRECTION',
    'ORIENTATION',
    'EMPTY',
    'VALUE',

]

# Expresiones regulares para tokens simples
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'



# Expresión regular para números (puede ser entero o decimal)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Expresión regular para identificadores (nombres de variables y procedimientos)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

# Expresión regular para direcciones (left, right, around)
def t_DIRECTION(t):
    r'left|right|around'
    t.type = 'DIRECTION'
    return t

# Expresión regular para orientaciones (north, south, east, west)
def t_ORIENTATION(t):
    r'north|south|east|west'
    t.type = 'ORIENTATION'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Expresión regular para manejar saltos de línea y llevar cuenta del número de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores (caracteres no válidos)
def t_error(t):
    print(f"Caracter no válido: '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()