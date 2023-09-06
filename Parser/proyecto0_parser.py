
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
# Definición de la gramática con las reglas:

def p_program(p):
#    program : commands_and_definitions program_body
    print("Program syntax is correct.")

# Definición de variables (defVar)
def p_variable_definitions(p):
#    variable_definitions : empty
                           #| variable_definitions DEFVAR ID NUMBER SEMICOLON
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
#    procedure_definitions : empty
                            #| procedure_definitions DEFPROC ID LPAREN parameters RPAREN LBRACE program_body RBRACE
    if len(p) > 2:
        # Verifica que la sintaxis sea correcta para la definición de procedimientos
        if p[2].lower() != "defproc":
            print("Error: Se esperaba la palabra clave 'defProc' en la definición de procedimiento.")
        
        procedure_name = p[3]  # Nombre del procedimiento
        procedure_params = p[5]  # Lista de parámetros
        
        # Verifica que se hayan proporcionado paréntesis de apertura y cierre
        if p[4] != "(" or p[6] != ")":
            print("Error: Falta paréntesis de apertura o cierre en la definición de procedimiento.")
        
        # Verifica que el cuerpo del procedimiento esté encerrado entre llaves
        if p[7] != "{" or p[9] != "}":
            print("Error: Falta llave de apertura o cierre para el cuerpo del procedimiento.")
        
        procedure_body = p[8]  # Cuerpo del procedimiento


# Parámetros de procedimientos
def p_parameters(p):
#    parameters : empty
                  #| ID COMMA parameters
    if len(p) > 2:
        # Aquí puedes verificar la sintaxis correcta de los parámetros
        parameter_name = p[1]
        # Puedes realizar las verificaciones necesarias aquí
    pass



# Resto de las reglas de tu gramática aquí...

# Construye el parser
parser = yacc.yacc()




def p_empty(p):
  '''empty :'''
  pass

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




