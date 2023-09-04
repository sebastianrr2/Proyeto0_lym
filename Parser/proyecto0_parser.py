import ply.yacc as yacc
import proyecto0_lexer

# Importa los tokens desde el lexer
tokens = proyecto0_lexer.tokens

def p_program(p):
    '''
    program : commands
    '''
    p[0] = p[1]

def p_commands(p):
    '''
    commands : command
             | commands command
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_command(p):
    '''
    command : simple_command
    '''
    p[0] = p[1]

def p_simple_command(p):
    '''
    simple_command : YES
                   | NO
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error at line", p.lineno)

# Crea el lexer
lexer = proyecto0_lexer.lexer
parser = yacc.yacc()

# Leer el archivo de ejemplo
filename = r"c:\Users\sebas\OneDrive - Universidad de los Andes\5 semestre\lym\proyecto 0\Proyeto0_lym\Parser\ejemplo1"
with open(filename, "r") as file:
    program = file.read()

# Parsear el programa
result = parser.parse(program)

# Verificar si hubo errores de sintaxis
if result is not None:
    print("El programa tiene una sintaxis válida.")
else:
    print("El programa tiene errores de sintaxis.")
