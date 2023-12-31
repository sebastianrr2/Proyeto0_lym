
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DEFPROC DEFVAR DIRECTION DROP EMPTY GET GRAB ID LBRACE LEAP LETGO LPAREN NOP NUMBER ORIENTATION RBRACE RPAREN SEMICOLON TURN TURNTO VALUE WALKprogram : program_statement\n               | program program_statement\n    program_statement : variable_definitions\n                        | procedure_definitions\n                        | leap_command\n                        | walk_command\n                        | turn_command\n                        | turnto_command\n                        | generic_command\n                        | leap_value\n                        | walk_value\n    variable_definitions : EMPTY\n                           | variable_definitions DEFVAR ID NUMBER SEMICOLONprocedure_definitions : EMPTY\n                            | procedure_definitions DEFPROC ID LPAREN tuple_values RPAREN LBRACE RBRACEtuple_values : VALUE COMMA VALUE\n                    | VALUEleap_value : LEAP LPAREN VALUE RPARENleap_command : LEAP LPAREN tuple_values RPARENwalk_command : WALK LPAREN tuple_values RPARENwalk_value : WALK LPAREN VALUE RPARENturn_command : TURN LPAREN DIRECTION RPARENturnto_command : TURNTO LPAREN ORIENTATION RPARENgeneric_command : DROP LPAREN VALUE RPAREN\n                       | GET LPAREN VALUE RPAREN\n                       | GRAB LPAREN VALUE RPAREN\n                       | LETGO LPAREN VALUE RPAREN\n                       | NOP LPAREN RPAREN'
    
_lr_action_items = {'EMPTY':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[12,12,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'LEAP':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[13,13,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'WALK':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[14,14,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'TURN':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[15,15,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'TURNTO':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[16,16,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'DROP':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[17,17,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'GET':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[18,18,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'GRAB':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'LETGO':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'NOP':([0,1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,22,46,49,50,52,53,54,55,56,57,58,59,60,66,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-28,-19,-18,-20,-21,-22,-23,-24,-25,-26,-27,-13,-15,]),'DEFVAR':([3,12,60,],[23,-12,-13,]),'DEFPROC':([4,12,66,],[24,-14,-15,]),'LPAREN':([13,14,15,16,17,18,19,20,21,35,],[25,26,27,28,29,30,31,32,33,48,]),'ID':([23,24,],[34,35,]),'VALUE':([25,26,29,30,31,32,48,51,],[37,39,42,43,44,45,62,63,]),'DIRECTION':([27,],[40,]),'ORIENTATION':([28,],[41,]),'RPAREN':([33,36,37,38,39,40,41,42,43,44,45,61,62,63,],[46,49,50,52,53,54,55,56,57,58,59,64,-17,-16,]),'NUMBER':([34,],[47,]),'COMMA':([37,39,62,],[51,51,51,]),'SEMICOLON':([47,],[60,]),'LBRACE':([64,],[65,]),'RBRACE':([65,],[66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_statement':([0,1,],[2,22,]),'variable_definitions':([0,1,],[3,3,]),'procedure_definitions':([0,1,],[4,4,]),'leap_command':([0,1,],[5,5,]),'walk_command':([0,1,],[6,6,]),'turn_command':([0,1,],[7,7,]),'turnto_command':([0,1,],[8,8,]),'generic_command':([0,1,],[9,9,]),'leap_value':([0,1,],[10,10,]),'walk_value':([0,1,],[11,11,]),'tuple_values':([25,26,48,],[36,38,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_statement','program',1,'p_program','proyecto0_parser.py',17),
  ('program -> program program_statement','program',2,'p_program','proyecto0_parser.py',18),
  ('program_statement -> variable_definitions','program_statement',1,'p_program_statement','proyecto0_parser.py',22),
  ('program_statement -> procedure_definitions','program_statement',1,'p_program_statement','proyecto0_parser.py',23),
  ('program_statement -> leap_command','program_statement',1,'p_program_statement','proyecto0_parser.py',24),
  ('program_statement -> walk_command','program_statement',1,'p_program_statement','proyecto0_parser.py',25),
  ('program_statement -> turn_command','program_statement',1,'p_program_statement','proyecto0_parser.py',26),
  ('program_statement -> turnto_command','program_statement',1,'p_program_statement','proyecto0_parser.py',27),
  ('program_statement -> generic_command','program_statement',1,'p_program_statement','proyecto0_parser.py',28),
  ('program_statement -> leap_value','program_statement',1,'p_program_statement','proyecto0_parser.py',29),
  ('program_statement -> walk_value','program_statement',1,'p_program_statement','proyecto0_parser.py',30),
  ('variable_definitions -> EMPTY','variable_definitions',1,'p_variable_definitions','proyecto0_parser.py',34),
  ('variable_definitions -> variable_definitions DEFVAR ID NUMBER SEMICOLON','variable_definitions',5,'p_variable_definitions','proyecto0_parser.py',35),
  ('procedure_definitions -> EMPTY','procedure_definitions',1,'p_procedure_definitions','proyecto0_parser.py',48),
  ('procedure_definitions -> procedure_definitions DEFPROC ID LPAREN tuple_values RPAREN LBRACE RBRACE','procedure_definitions',8,'p_procedure_definitions','proyecto0_parser.py',49),
  ('tuple_values -> VALUE COMMA VALUE','tuple_values',3,'p_tuple_values','proyecto0_parser.py',67),
  ('tuple_values -> VALUE','tuple_values',1,'p_tuple_values','proyecto0_parser.py',68),
  ('leap_value -> LEAP LPAREN VALUE RPAREN','leap_value',4,'p_leap_value_single','proyecto0_parser.py',80),
  ('leap_command -> LEAP LPAREN tuple_values RPAREN','leap_command',4,'p_leap_command','proyecto0_parser.py',88),
  ('walk_command -> WALK LPAREN tuple_values RPAREN','walk_command',4,'p_walk_command','proyecto0_parser.py',102),
  ('walk_value -> WALK LPAREN VALUE RPAREN','walk_value',4,'p_walk_value_single','proyecto0_parser.py',115),
  ('turn_command -> TURN LPAREN DIRECTION RPAREN','turn_command',4,'p_turn_command','proyecto0_parser.py',123),
  ('turnto_command -> TURNTO LPAREN ORIENTATION RPAREN','turnto_command',4,'p_turnto_command','proyecto0_parser.py',135),
  ('generic_command -> DROP LPAREN VALUE RPAREN','generic_command',4,'p_generic_command','proyecto0_parser.py',147),
  ('generic_command -> GET LPAREN VALUE RPAREN','generic_command',4,'p_generic_command','proyecto0_parser.py',148),
  ('generic_command -> GRAB LPAREN VALUE RPAREN','generic_command',4,'p_generic_command','proyecto0_parser.py',149),
  ('generic_command -> LETGO LPAREN VALUE RPAREN','generic_command',4,'p_generic_command','proyecto0_parser.py',150),
  ('generic_command -> NOP LPAREN RPAREN','generic_command',3,'p_generic_command','proyecto0_parser.py',151),
]
