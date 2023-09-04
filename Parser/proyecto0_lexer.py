import ply.lex as Lexer
# Lista de tokens
tokens = [
    'NAME',
    'NUMBER',
    'ASIGNACION',
    'PARIZ',
    'PARDER',
    'COMA',
    'SEMICOLON',
    'LLAVEIZQ',
    'LLAVEDER',
    'IF',
    'ELSE',
    'WHILE',
    'REPEAT',
    'TIMES',
    'FACING',
    'CAN',
    'MOVE',
    'TURN',
    'DROP',
    'PICK_UP',
    'OTHER_ACTION',
    'DEFVAR',
    'DEFPROC',
    'JUMP',
    'PUTCB',
    'LETGO',
    'WALK',
    'NORTH',
    'SOUTH',
    'EAST',
    'WEST',
    'NOP',
    'YES',
    'NO'
]

# Expresiones regulares para los tokens
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_ASIGNACION = r'='
t_PARIZ = r'\('
t_PARDER = r'\)'
t_COMA = r','
t_SEMICOLON = r';'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_REPEAT = r'repeat'
t_TIMES = r'times'
t_FACING = r'facing'
t_CAN = r'can'
t_MOVE = r'move'
t_TURN = r'turn'
t_DROP = r'drop'
t_PICK_UP = r'pickup'
t_OTHER_ACTION = r'other_action'
t_DEFVAR = r'defVar'
t_DEFPROC = r'defProc'
t_JUMP = r'jump'
t_PUTCB = r'putCB'
t_LETGO = r'letGo'
t_WALK = r'walk'
t_NORTH = r'north'
t_SOUTH = r'south'
t_EAST = r'east'
t_WEST = r'west'
t_NOP = r'nop'
t_YES = r'yes'
t_NO = r'no'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar saltos
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass
