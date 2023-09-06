import ply.yacc as yacc
import proyecto0_lexer
import os
import codecs
import re
from sys import stdin
# Importa los tokens desde el lexer
tokens = proyecto0_lexer.tokens


# Define diccionarios para rastrear procedimientos y variables
procedures = {}  # Para rastrear procedimientos definidos
variables = {}
# Definición de la gramática con las reglas

def p_program(p):
    """program : program_statement
               | program program_statement
    """

def p_program_statement(p):
    """program_statement : variable_definitions
                        | procedure_definitions
                        | leap_command
                        | walk_command
                        | turn_command
                        | turnto_command
                        | generic_command
                        | leap_value
                        | walk_value
    """
# Definición de variables (defVar)
def p_variable_definitions(p):
    """variable_definitions : EMPTY
                           | variable_definitions DEFVAR ID NUMBER SEMICOLON"""
    if len(p) > 2:
        # Verifica que la sintaxis sea correcta, incluyendo la palabra clave "defVar",
        # un nombre de variable (ID) y un valor inicial (NUMBER)
        if p[2].lower() != "defvar":
            print("Error: Se esperaba la palabra clave 'defVar' en la definición de variable.")
        if not p[3]:
            print("Error: Falta el nombre de la variable en la definición de variable.")
        if not p[4]:
            print("Error: Falta el valor inicial en la definición de variable.")

# Definición de procedimientos (defProc)
def p_procedure_definitions(p):
    """procedure_definitions : EMPTY
                            | procedure_definitions DEFPROC ID LPAREN tuple_values RPAREN LBRACE RBRACE"""
    if len(p) > 2:
        # Verifica que la sintaxis sea correcta para la definición de procedimientos
        if p[2].lower() != "defproc":
            print("Error: Se esperaba la palabra clave 'defProc' en la definición de procedimiento.")
        if not p[3]:
            print("Error: Falta el nombre del procedimiento en la definición de procedimiento.")
        # Verifica que se hayan proporcionado paréntesis de apertura y cierre
        if p[4] != "(" or p[6] != ")":
            print("Error: Falta paréntesis de apertura o cierre en la definición de procedimiento.")
        
        # Verifica que el cuerpo del procedimiento esté encerrado entre llaves
        if p[7] != "{" or p[9] != "}":
            print("Error: Falta llave de apertura o cierre para el cuerpo del procedimiento.")
        
        procedure_body = p[8]  # Cuerpo del procedimiento

def p_tuple_values(p):
    """tuple_values : VALUE COMMA VALUE
                    | VALUE"""
    # Verifica la sintaxis de los valores en la tupla
    if len(p) == 4:
        print("Tuple values syntax is correct.")
        # Puedes realizar acciones específicas con los valores aquí si es necesario
    elif len(p) == 2:
        print("Single value in tuple syntax is correct.")
        # Puedes realizar acciones específicas con el valor aquí si es necesario
    else:
        print("Tuple values syntax is incorrect.")

def p_leap_value_single(p):
    """leap_value : LEAP LPAREN VALUE RPAREN"""
    # Verifica la sintaxis de un valor individual
    if len(p) == 2:
        print("Single value syntax is correct.")
    else:
        print("Single value syntax is incorrect.")

def p_leap_command(p):
    """leap_command : LEAP LPAREN tuple_values RPAREN"""
    if len(p) == 4:
        # Verifica que la sintaxis sea correcta
        if p[3].lower() in {'front', 'right', 'left', 'back', 'north', 'south', 'west', 'east'}:
            print("Leap command syntax is correct.")
        else:
            print("Invalid direction or coordinate in leap command.")
    else:
        # La sintaxis es incorrecta
        print("Leap command syntax is incorrect.")

# Resto de las reglas de tu gramática aquí...

def p_walk_command(p):
    """walk_command : WALK LPAREN tuple_values RPAREN"""
    if len(p) == 4:
        # Verifica que la sintaxis sea correcta
        if p[3].lower() in {'front', 'right', 'left', 'back', 'north', 'south', 'west', 'east'}:
            print("Walk command syntax is correct.")
        else:
            print("Invalid direction or coordinate in walk command.")
    else:
        # La sintaxis es incorrecta
        print("Walk command syntax is incorrect.")


def p_walk_value_single(p):
    """walk_value : WALK LPAREN VALUE RPAREN"""
    # Verifica la sintaxis de un valor individual
    if len(p) == 2:
        print("Single value syntax is correct for walk command.")
    else:
        print("Single value syntax is incorrect for walk command.")

def p_turn_command(p):
    """turn_command : TURN LPAREN DIRECTION RPAREN"""
    if len(p) == 4:
        # Verifica que la sintaxis sea correcta
        if p[3].lower() in {'left', 'right', 'around'}:
            print("Turn command syntax is correct.")
        else:
            print("Invalid direction in turn command.")
    else:
        # La sintaxis es incorrecta
        print("Turn command syntax is incorrect.")

def p_turnto_command(p):
    """turnto_command : TURNTO LPAREN ORIENTATION RPAREN"""
    if len(p) == 4:
        # Verifica que la sintaxis sea correcta
        if p[3].lower() in {'north', 'south', 'east', 'west'}:
            print("Turnto command syntax is correct.")
        else:
            print("Invalid orientation in turnto command.")
    else:
        # La sintaxis es incorrecta
        print("Turnto command syntax is incorrect.")

def p_generic_command(p):
    """generic_command : DROP LPAREN VALUE RPAREN
                       | GET LPAREN VALUE RPAREN
                       | GRAB LPAREN VALUE RPAREN
                       | LETGO LPAREN VALUE RPAREN
                       | NOP LPAREN RPAREN"""
    if len(p) == 5:
        # Verifica que la sintaxis sea correcta
        command_name = p[1].lower()
        if command_name in {'drop', 'get', 'grab', 'letgo'}:
            print(f"{command_name} command syntax is correct with value: {p[3]}.")
        else:
            print(f"Invalid command: {command_name}.")
    elif len(p) == 4 and p[1].lower() == 'nop':
        # Comando 'nop' sin valor, la sintaxis es correcta
        print("NOP command syntax is correct.")
    else:
        # La sintaxis es incorrecta
        print("Command syntax is incorrect.")


# Construye el parser
parser = yacc.yacc()

# Resto de tu código...

def p_error(p):
    print("Syntax error at line", p.lineno)

# Crea el lexer
lexer = proyecto0_lexer.lexer
parser = yacc.yacc()

# Leer el archivo de ejemplo
filename = r"C:\Users\User\Desktop\UniAndes\Lenguaje de maquinas\Proyeto0_lym\Parser\ejemplo3.txt"
with open(filename, "r") as file:
    program = file.read()

# Parsear el programa
result = parser.parse(program)

# Verificar si hubo errores de sintaxis
if result is not None:
    print("El programa tiene una sintaxis válida.")
else:
    print("El programa tiene errores de sintaxis.")
