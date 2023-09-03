import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'ID',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'EQUALS',
    'COMMA',
    'IF',
    'ELSE',
    'WHILE',
    'NORTH',
    'SOUTH',
    'WEST',
    'EAST',
    'FRONT',
    'RIGHT',
    'LEFT',
    'BACK',
    'NOP',
    'DEFVAR',
    'DEFPROC',
    'JUMP',
    'WALK',
    'LEAP',
    'TURN',
    'TURNTON',
    'DROP',
    'GET',
    'GRAB',
    'LETGO',
    'REPEATTIMES',
)

# Expresiones regulares para tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_EQUALS = r'='

# Tokens específicos del lenguaje
t_DEFVAR = r'defVar'
t_DEFPROC = r'defProc'
t_JUMP = r'jump'
t_WALK = r'walk'
t_LEAP = r'leap'
t_TURN = r'turn'
t_TURNTON = r'turnto'
t_DROP = r'drop'
t_GET = r'get'
t_GRAB = r'grab'
t_LETGO = r'letGo'
t_NOP = r'nop'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_NORTH = r'north'
t_SOUTH = r'south'
t_WEST = r'west'
t_EAST = r'east'
t_FRONT = r'front'
t_RIGHT = r'right'
t_LEFT = r'left'
t_BACK = r'back'
t_REPEATTIMES = r'repeatTimes'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

# Ignorar espacios y tabuladores
t_ignore = ' \t'

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar errores
def t_error(t):
    print(f"Error léxico en el carácter '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Palabras reservadas
reserved = {
    'defvar': 'DEFVAR',
    'defproc': 'DEFPROC',
    'jump': 'JUMP',
    'walk': 'WALK',
    'leap': 'LEAP',
    'turn': 'TURN',
    'turnto': 'TURNTON',
    'drop': 'DROP',
    'get': 'GET',
    'grab': 'GRAB',
    'letgo': 'LETGO',
    'nop': 'NOP',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'north': 'NORTH',
    'south': 'SOUTH',
    'west': 'WEST',
    'east': 'EAST',
    'front': 'FRONT',
    'right': 'RIGHT',
    'left': 'LEFT',
    'back': 'BACK',
    'repeattimes': 'REPEATTIMES',
}
