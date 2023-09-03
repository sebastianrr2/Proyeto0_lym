import ply.yacc as yacc
import proyecto0_lexer as lexer

# Regla gramatical para el programa
def p_program(p):
    'program : commands'
    p[0] = "SÍ"  # Si llegamos aquí, el programa tiene sintaxis válida

# Regla para los comandos
def p_commands(p):
    '''commands : command SEMICOLON commands
                | empty'''
    pass

# Regla para un comando
def p_command(p):
    '''command : ID EQUALS value
               | jump
               | walk
               | turn
               | drop
               | grab
               | letGo
               | nop
               | ID LPAREN arguments RPAREN  # Llamada a procedimiento
               | conditional
               | loop
               | repeatTimes'''
    pass

# Reglas para saltos y bloques
def p_jump(p):
    'jump : JUMP LPAREN value COMMA value RPAREN SEMICOLON'
    pass

def p_walk(p):
    'walk : WALK LPAREN value RPAREN SEMICOLON'
    pass

# Define el resto de las reglas gramaticales

# Regla para manejar errores
def p_error(p):
    print(f"Error sintáctico en la entrada: {p.value}")

# Definición de la cadena vacía
def p_empty(p):
    'empty :'
    pass

# Crea el parser
parser = yacc.yacc()

# Función para verificar la sintaxis del programa
def verifica_sintaxis(program_text):
    result = parser.parse(program_text, lexer=lexer.lexer)
    return result

# Lee el archivo de entrada
with open('archivo_programa.robot', 'r') as file:
    programa_robot = file.read()

# Ejecuta la verificación de sintaxis
resultado = verifica_sintaxis(programa_robot)

if resultado == "SÍ":
    print("El programa tiene una sintaxis válida.")
else:
    print("El programa tiene errores de sintaxis.")



