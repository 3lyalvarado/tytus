
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTnonassocISISNULLNOTNULLleftMENORIGUALMAYORIGUALIGUALDIFDIF1MENORMAYORleftMASMENOSleftPORDIVIDIDOMODULOleftEXPrightUMENOSUMASAND AS ASC AVG BY CADENA COMA COUNT DECIMAL DESC DIF DIF1 DISTINCT DIVIDIDO EXP FALSE FIRST FROM GROUP HAVING ID IGUAL IS ISNULL LAST LIMIT MAS MAX MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MIN MODULO NOT NOTNULL NULLS NUMERO OFFSET OR ORDER PABRE PCIERRA PCOMA POR PUNTO SELECT SUM TRUE WHEREINSTRUCCIONES  :   INSTRUCCIONES INSTRUCCION   INSTRUCCIONES  :   INSTRUCCION INSTRUCCION  :   I_SELECT  I_SELECT  :   SELECT VALORES PFROM COMPLEMENTO PCOMA   I_SELECT  :   SELECT VALORES PFROM PWHERE COMPLEMENTO PCOMA    I_SELECT  :   SELECT DISTINCT VALORES PFROM COMPLEMENTO PCOMA   I_SELECT  :   SELECT DISTINCT VALORES PFROM PWHERE COMPLEMENTO PCOMA    COMPLEMENTO  :   PGROUPBY PHAVING  COMPLEMENTO  :   PGROUPBY PHAVING PLIMIT   COMPLEMENTO  :   PGROUPBY  COMPLEMENTO  :   PGROUPBY PLIMIT   COMPLEMENTO  :   PORDERBY  COMPLEMENTO  :   PORDERBY PLIMIT   COMPLEMENTO  :   PLIMIT    COMPLEMENTO  :   EMPTY PLIMIT  :   LIMIT CONDICION    PLIMIT  :   LIMIT CONDICION OFFSET CONDICION   PORDERBY  :   ORDER BY LCOMPLEMENTOORDERBY LCOMPLEMENTOORDERBY  :   LCOMPLEMENTOORDERBY COMA COMPLEMENTOORDERBY  LCOMPLEMENTOORDERBY  :   COMPLEMENTOORDERBY    COMPLEMENTOORDERBY  :   ID COMPLEMENTOORDERBY1    COMPLEMENTOORDERBY1  :   COMPLEMENTOORDER   COMPLEMENTOORDERBY1  :   PUNTO ID COMPLEMENTOORDER   COMPLEMENTOORDER  :   ASC  COMPLEMENTOORDER  :   DESC COMPLEMENTOORDER  :   ASC NULLS FIRST  COMPLEMENTOORDER  :   ASC NULLS LAST   COMPLEMENTOORDER  :   DESC NULLS FIRST COMPLEMENTOORDER  :   DESC NULLS LAST  COMPLEMENTOORDER  :   EMPTY    PHAVING  :   HAVING CONDICION PGROUPBY  :   GROUP BY LCOMPLEMENTOGROUP LCOMPLEMENTOGROUP  :   LCOMPLEMENTOGROUP COMA COMPLEMENTOGROUP LCOMPLEMENTOGROUP  :   COMPLEMENTOGROUP COMPLEMENTOGROUP  :   ID COMPLEMENTOGROUP  :   ID PUNTO ID VALORES  :   POR VALORES  :   LISTAVALORES LISTAVALORES  :   LISTAVALORES COMA VALOR LISTAVALORES  :   VALOR VALOR  :   ID ALIAS VALOR  :   ID PUNTO ID ALIAS VALOR  :   ID VALOR  :   ID PUNTO IDVALOR  :   PABRE SUBCONSULTA PCIERRA ALIASVALOR  :   PABRE SUBCONSULTA PCIERRA VALOR  :   COUNT PABRE POR PCIERRA ALIASVALOR  :   COUNT PABRE ID PCIERRA ALIASVALOR  :   COUNT PABRE POR PCIERRA VALOR  :   COUNT PABRE ID PCIERRA VALOR  :   COUNT PABRE ID PUNTO ID PCIERRA ALIASVALOR  :   COUNT PABRE ID PUNTO ID PCIERRAVALOR  :   FUNCION PABRE ID PUNTO ID PCIERRAVALOR  :   FUNCION PABRE ID  PCIERRAVALOR  :   FUNCION PABRE ID PUNTO ID PCIERRA ALIASVALOR  :   FUNCION PABRE ID  PCIERRA ALIASFUNCION    :   AVGFUNCION    :   SUMFUNCION    :   MINFUNCION    :   MAXALIAS  :   AS ID ALIAS  :   ID PFROM  :   FROM ID ALIAS PFROM  :   FROM ID PFROM  :   FROM PABRE SUBCONSULTA PCIERRA ALIAS    SUBCONSULTA    :   SELECT VALORES PFROM COMPLEMENTO SUBCONSULTA    :   SELECT VALORES PFROM PWHERE COMPLEMENTO PWHERE  :   WHERE CONDICION CONDICION  :   CONDICION IGUAL CONDICION CONDICION  :   CONDICION DIF CONDICION CONDICION  :   CONDICION DIF1 CONDICION CONDICION  :   CONDICION MENOR CONDICION CONDICION  :   CONDICION MENORIGUAL CONDICION CONDICION  :   CONDICION MAYOR CONDICION CONDICION  :   CONDICION MAYORIGUAL CONDICION CONDICION  :   CONDICION AND CONDICION CONDICION  :   CONDICION OR CONDICION CONDICION  :   NOT CONDICION CONDICION  :   PABRE CONDICION PCIERRA CONDICION  :   CONDICION MAS CONDICION CONDICION  :   CONDICION MENOS CONDICION CONDICION  :   CONDICION POR CONDICION CONDICION  :   CONDICION DIVIDIDO CONDICION CONDICION  :   CONDICION MODULO CONDICION CONDICION  :   CONDICION EXP CONDICION CONDICION  :   CONDICION IS CONDICION CONDICION  :   CONDICION ISNULL CONDICION CONDICION  :   CONDICION NOTNULL CONDICION CONDICION  :   MENOS CONDICION %prec UMENOSCONDICION  :   MAS CONDICION %prec UMASCONDICION  :   NUMERO CONDICION  :   DECIMALCONDICION  :   CADENA CONDICION  :   TRUE CONDICION  :   FALSE CONDICION  :   ID CONDICION  :   ID PUNTO ID EMPTY :'
    
_lr_action_items = {'SELECT':([0,1,2,3,5,12,42,52,84,118,158,],[4,4,-2,-3,-1,28,28,-4,-5,-6,-7,]),'$end':([1,2,3,5,52,84,118,158,],[0,-2,-3,-1,-4,-5,-6,-7,]),'DISTINCT':([4,],[7,]),'POR':([4,7,28,29,58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[8,8,8,49,98,-91,-92,-93,-94,-95,-96,98,98,98,98,-90,-89,98,98,98,98,98,98,98,98,98,98,98,-82,-83,-84,-85,98,98,98,-79,-97,98,]),'ID':([4,7,11,20,22,25,26,28,29,30,37,40,41,45,47,56,59,60,61,62,69,70,79,80,81,82,83,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,109,116,117,147,148,149,152,160,161,],[11,11,23,41,11,45,46,11,50,51,68,68,23,23,23,68,68,68,68,68,112,115,23,23,124,125,23,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,146,68,23,112,163,115,165,23,23,]),'PABRE':([4,7,13,14,15,16,17,18,20,22,28,37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[12,12,29,30,-57,-58,-59,-60,42,12,12,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'COUNT':([4,7,22,28,],[13,13,13,13,]),'AVG':([4,7,22,28,],[15,15,15,15,]),'SUM':([4,7,22,28,],[16,16,16,16,]),'MIN':([4,7,22,28,],[17,17,17,17,]),'MAX':([4,7,22,28,],[18,18,18,18,]),'FROM':([6,8,9,10,11,21,23,24,44,45,46,47,48,76,77,79,80,83,122,123,126,160,161,168,169,],[20,-37,-38,-40,-43,20,-62,-41,-39,-44,-61,-46,20,-42,-45,-49,-50,-54,-47,-48,-56,-52,-53,-51,-55,]),'COMA':([9,10,11,23,24,44,45,46,47,76,77,79,80,83,110,111,112,113,114,115,122,123,126,150,151,153,154,155,160,161,162,163,164,165,168,169,170,171,172,173,174,],[22,-40,-43,-62,-41,-39,-44,-61,-46,-42,-45,-49,-50,-54,147,-34,-35,149,-20,-98,-47,-48,-56,-21,-22,-24,-25,-30,-52,-53,-33,-36,-19,-98,-51,-55,-23,-26,-27,-28,-29,]),'PUNTO':([11,50,51,68,112,115,],[25,81,82,109,148,152,]),'AS':([11,41,45,47,79,80,83,117,160,161,],[26,26,26,26,26,26,26,26,26,26,]),'WHERE':([19,23,41,43,46,72,78,157,],[37,-62,-64,37,-61,-63,37,-65,]),'GROUP':([19,23,32,41,43,46,58,63,64,65,66,67,68,72,75,78,105,107,108,121,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,157,],[38,-62,38,-64,38,-61,-68,-91,-92,-93,-94,-95,-96,-63,38,38,-78,-90,-89,38,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,-65,]),'ORDER':([19,23,32,41,43,46,58,63,64,65,66,67,68,72,75,78,105,107,108,121,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,157,],[39,-62,39,-64,39,-61,-68,-91,-92,-93,-94,-95,-96,-63,39,39,-78,-90,-89,39,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,-65,]),'LIMIT':([19,23,32,33,35,41,43,46,54,58,63,64,65,66,67,68,72,75,78,86,105,107,108,110,111,112,113,114,115,121,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,150,151,153,154,155,157,162,163,164,165,170,171,172,173,174,],[40,-62,40,40,40,-64,40,-61,40,-68,-91,-92,-93,-94,-95,-96,-63,40,40,-31,-78,-90,-89,-32,-34,-35,-18,-20,-98,40,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,-21,-22,-24,-25,-30,-65,-33,-36,-19,-98,-23,-26,-27,-28,-29,]),'PCOMA':([19,23,31,32,33,34,35,36,41,43,46,53,54,55,57,58,63,64,65,66,67,68,71,72,74,75,85,86,105,107,108,110,111,112,113,114,115,119,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,150,151,153,154,155,156,157,162,163,164,165,170,171,172,173,174,],[-98,-62,52,-98,-10,-14,-12,-15,-64,-98,-61,84,-8,-11,-13,-68,-91,-92,-93,-94,-95,-96,-16,-63,118,-98,-9,-31,-78,-90,-89,-32,-34,-35,-18,-20,-98,158,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,-21,-22,-24,-25,-30,-17,-65,-33,-36,-19,-98,-23,-26,-27,-28,-29,]),'PCIERRA':([23,27,33,34,35,36,41,46,49,50,51,54,55,57,58,63,64,65,66,67,68,71,72,73,78,85,86,105,106,107,108,110,111,112,113,114,115,120,121,124,125,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,150,151,153,154,155,156,157,159,162,163,164,165,170,171,172,173,174,],[-62,47,-10,-14,-12,-15,-64,-61,79,80,83,-8,-11,-13,-68,-91,-92,-93,-94,-95,-96,-16,-63,117,-98,-9,-31,-78,145,-90,-89,-32,-34,-35,-18,-20,-98,-66,-98,160,161,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,-21,-22,-24,-25,-30,-17,-65,-67,-33,-36,-19,-98,-23,-26,-27,-28,-29,]),'HAVING':([33,110,111,112,162,163,],[56,-32,-34,-35,-33,-36,]),'NOT':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'MENOS':([37,40,56,58,59,60,61,62,63,64,65,66,67,68,71,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[62,62,62,97,62,62,62,62,-91,-92,-93,-94,-95,-96,97,97,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,97,97,-90,-89,62,97,97,97,97,97,97,97,97,97,-80,-81,-82,-83,-84,-85,97,97,97,-79,-97,97,]),'MAS':([37,40,56,58,59,60,61,62,63,64,65,66,67,68,71,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,116,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[61,61,61,96,61,61,61,61,-91,-92,-93,-94,-95,-96,96,96,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,96,96,-90,-89,61,96,96,96,96,96,96,96,96,96,-80,-81,-82,-83,-84,-85,96,96,96,-79,-97,96,]),'NUMERO':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'DECIMAL':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'CADENA':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'TRUE':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'FALSE':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'BY':([38,39,],[69,70,]),'IGUAL':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[87,-91,-92,-93,-94,-95,-96,87,87,87,87,-90,-89,-69,-70,-71,-72,-73,-74,-75,87,87,-80,-81,-82,-83,-84,-85,87,87,87,-79,-97,87,]),'DIF':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[88,-91,-92,-93,-94,-95,-96,88,88,88,88,-90,-89,-69,-70,-71,-72,-73,-74,-75,88,88,-80,-81,-82,-83,-84,-85,88,88,88,-79,-97,88,]),'DIF1':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[89,-91,-92,-93,-94,-95,-96,89,89,89,89,-90,-89,-69,-70,-71,-72,-73,-74,-75,89,89,-80,-81,-82,-83,-84,-85,89,89,89,-79,-97,89,]),'MENOR':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[90,-91,-92,-93,-94,-95,-96,90,90,90,90,-90,-89,-69,-70,-71,-72,-73,-74,-75,90,90,-80,-81,-82,-83,-84,-85,90,90,90,-79,-97,90,]),'MENORIGUAL':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[91,-91,-92,-93,-94,-95,-96,91,91,91,91,-90,-89,-69,-70,-71,-72,-73,-74,-75,91,91,-80,-81,-82,-83,-84,-85,91,91,91,-79,-97,91,]),'MAYOR':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[92,-91,-92,-93,-94,-95,-96,92,92,92,92,-90,-89,-69,-70,-71,-72,-73,-74,-75,92,92,-80,-81,-82,-83,-84,-85,92,92,92,-79,-97,92,]),'MAYORIGUAL':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[93,-91,-92,-93,-94,-95,-96,93,93,93,93,-90,-89,-69,-70,-71,-72,-73,-74,-75,93,93,-80,-81,-82,-83,-84,-85,93,93,93,-79,-97,93,]),'AND':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[94,-91,-92,-93,-94,-95,-96,94,94,-78,94,-90,-89,-69,-70,-71,-72,-73,-74,-75,-76,94,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,94,]),'OR':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[95,-91,-92,-93,-94,-95,-96,95,95,-78,95,-90,-89,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,95,]),'DIVIDIDO':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[99,-91,-92,-93,-94,-95,-96,99,99,99,99,-90,-89,99,99,99,99,99,99,99,99,99,99,99,-82,-83,-84,-85,99,99,99,-79,-97,99,]),'MODULO':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[100,-91,-92,-93,-94,-95,-96,100,100,100,100,-90,-89,100,100,100,100,100,100,100,100,100,100,100,-82,-83,-84,-85,100,100,100,-79,-97,100,]),'EXP':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[101,-91,-92,-93,-94,-95,-96,101,101,101,101,-90,-89,101,101,101,101,101,101,101,101,101,101,101,101,101,101,-85,101,101,101,-79,-97,101,]),'IS':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[102,-91,-92,-93,-94,-95,-96,102,102,102,102,-90,-89,-69,-70,-71,-72,-73,-74,-75,102,102,-80,-81,-82,-83,-84,-85,None,None,None,-79,-97,102,]),'ISNULL':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[103,-91,-92,-93,-94,-95,-96,103,103,103,103,-90,-89,-69,-70,-71,-72,-73,-74,-75,103,103,-80,-81,-82,-83,-84,-85,None,None,None,-79,-97,103,]),'NOTNULL':([58,63,64,65,66,67,68,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,156,],[104,-91,-92,-93,-94,-95,-96,104,104,104,104,-90,-89,-69,-70,-71,-72,-73,-74,-75,104,104,-80,-81,-82,-83,-84,-85,None,None,None,-79,-97,104,]),'OFFSET':([63,64,65,66,67,68,71,105,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,],[-91,-92,-93,-94,-95,-96,116,-78,-90,-89,-69,-70,-71,-72,-73,-74,-75,-76,-77,-80,-81,-82,-83,-84,-85,-86,-87,-88,-79,-97,]),'ASC':([115,165,],[153,153,]),'DESC':([115,165,],[154,154,]),'NULLS':([153,154,],[166,167,]),'FIRST':([166,167,],[171,173,]),'LAST':([166,167,],[172,174,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INSTRUCCIONES':([0,],[1,]),'INSTRUCCION':([0,1,],[2,5,]),'I_SELECT':([0,1,],[3,3,]),'VALORES':([4,7,28,],[6,21,48,]),'LISTAVALORES':([4,7,28,],[9,9,9,]),'VALOR':([4,7,22,28,],[10,10,44,10,]),'FUNCION':([4,7,22,28,],[14,14,14,14,]),'PFROM':([6,21,48,],[19,43,78,]),'ALIAS':([11,41,45,47,79,80,83,117,160,161,],[24,72,76,77,122,123,126,157,168,169,]),'SUBCONSULTA':([12,42,],[27,73,]),'COMPLEMENTO':([19,32,43,75,78,121,],[31,53,74,119,120,159,]),'PWHERE':([19,43,78,],[32,75,121,]),'PGROUPBY':([19,32,43,75,78,121,],[33,33,33,33,33,33,]),'PLIMIT':([19,32,33,35,43,54,75,78,121,],[34,34,55,57,34,85,34,34,34,]),'PORDERBY':([19,32,43,75,78,121,],[35,35,35,35,35,35,]),'EMPTY':([19,32,43,75,78,115,121,165,],[36,36,36,36,36,155,36,155,]),'PHAVING':([33,],[54,]),'CONDICION':([37,40,56,59,60,61,62,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,116,],[58,71,86,105,106,107,108,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,156,]),'LCOMPLEMENTOGROUP':([69,],[110,]),'COMPLEMENTOGROUP':([69,147,],[111,162,]),'LCOMPLEMENTOORDERBY':([70,],[113,]),'COMPLEMENTOORDERBY':([70,149,],[114,164,]),'COMPLEMENTOORDERBY1':([115,],[150,]),'COMPLEMENTOORDER':([115,165,],[151,170,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INSTRUCCIONES","S'",1,None,None,None),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_Inicio','Lexico.py',187),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_Inicio1','Lexico.py',191),
  ('INSTRUCCION -> I_SELECT','INSTRUCCION',1,'p_Instruccion','Lexico.py',194),
  ('I_SELECT -> SELECT VALORES PFROM COMPLEMENTO PCOMA','I_SELECT',5,'p_ISelect','Lexico.py',197),
  ('I_SELECT -> SELECT VALORES PFROM PWHERE COMPLEMENTO PCOMA','I_SELECT',6,'p_ISelect1','Lexico.py',200),
  ('I_SELECT -> SELECT DISTINCT VALORES PFROM COMPLEMENTO PCOMA','I_SELECT',6,'p_ISelect2','Lexico.py',203),
  ('I_SELECT -> SELECT DISTINCT VALORES PFROM PWHERE COMPLEMENTO PCOMA','I_SELECT',7,'p_ISelect3','Lexico.py',206),
  ('COMPLEMENTO -> PGROUPBY PHAVING','COMPLEMENTO',2,'p_ComplementoH','Lexico.py',210),
  ('COMPLEMENTO -> PGROUPBY PHAVING PLIMIT','COMPLEMENTO',3,'p_ComplementoHL','Lexico.py',213),
  ('COMPLEMENTO -> PGROUPBY','COMPLEMENTO',1,'p_ComplementoG','Lexico.py',216),
  ('COMPLEMENTO -> PGROUPBY PLIMIT','COMPLEMENTO',2,'p_ComplementoGL','Lexico.py',219),
  ('COMPLEMENTO -> PORDERBY','COMPLEMENTO',1,'p_ComplementoO','Lexico.py',222),
  ('COMPLEMENTO -> PORDERBY PLIMIT','COMPLEMENTO',2,'p_ComplementoOL','Lexico.py',225),
  ('COMPLEMENTO -> PLIMIT','COMPLEMENTO',1,'p_ComplementoL','Lexico.py',228),
  ('COMPLEMENTO -> EMPTY','COMPLEMENTO',1,'p_ComplementoE','Lexico.py',231),
  ('PLIMIT -> LIMIT CONDICION','PLIMIT',2,'p_Limit','Lexico.py',234),
  ('PLIMIT -> LIMIT CONDICION OFFSET CONDICION','PLIMIT',4,'p_LimitOff','Lexico.py',237),
  ('PORDERBY -> ORDER BY LCOMPLEMENTOORDERBY','PORDERBY',3,'p_OrderBy','Lexico.py',240),
  ('LCOMPLEMENTOORDERBY -> LCOMPLEMENTOORDERBY COMA COMPLEMENTOORDERBY','LCOMPLEMENTOORDERBY',3,'p_ComplementoOrderL','Lexico.py',243),
  ('LCOMPLEMENTOORDERBY -> COMPLEMENTOORDERBY','LCOMPLEMENTOORDERBY',1,'p_ComplementoOrderL1','Lexico.py',246),
  ('COMPLEMENTOORDERBY -> ID COMPLEMENTOORDERBY1','COMPLEMENTOORDERBY',2,'p_ComplementoOrderCI','Lexico.py',249),
  ('COMPLEMENTOORDERBY1 -> COMPLEMENTOORDER','COMPLEMENTOORDERBY1',1,'p_ComplementoOrderCOBC','Lexico.py',252),
  ('COMPLEMENTOORDERBY1 -> PUNTO ID COMPLEMENTOORDER','COMPLEMENTOORDERBY1',3,'p_ComplementoOrderCOBP','Lexico.py',255),
  ('COMPLEMENTOORDER -> ASC','COMPLEMENTOORDER',1,'p_ComplementoOrder','Lexico.py',259),
  ('COMPLEMENTOORDER -> DESC','COMPLEMENTOORDER',1,'p_ComplementoOD','Lexico.py',262),
  ('COMPLEMENTOORDER -> ASC NULLS FIRST','COMPLEMENTOORDER',3,'p_ComplementoOANF','Lexico.py',265),
  ('COMPLEMENTOORDER -> ASC NULLS LAST','COMPLEMENTOORDER',3,'p_ComplementoOANL','Lexico.py',268),
  ('COMPLEMENTOORDER -> DESC NULLS FIRST','COMPLEMENTOORDER',3,'p_ComplementoODNF','Lexico.py',271),
  ('COMPLEMENTOORDER -> DESC NULLS LAST','COMPLEMENTOORDER',3,'p_ComplementoODNL','Lexico.py',274),
  ('COMPLEMENTOORDER -> EMPTY','COMPLEMENTOORDER',1,'p_ComplementoEm','Lexico.py',277),
  ('PHAVING -> HAVING CONDICION','PHAVING',2,'p_Having','Lexico.py',281),
  ('PGROUPBY -> GROUP BY LCOMPLEMENTOGROUP','PGROUPBY',3,'p_GroupBy','Lexico.py',284),
  ('LCOMPLEMENTOGROUP -> LCOMPLEMENTOGROUP COMA COMPLEMENTOGROUP','LCOMPLEMENTOGROUP',3,'p_ComplementoGroupL','Lexico.py',287),
  ('LCOMPLEMENTOGROUP -> COMPLEMENTOGROUP','LCOMPLEMENTOGROUP',1,'p_ComplementoGroupLS','Lexico.py',290),
  ('COMPLEMENTOGROUP -> ID','COMPLEMENTOGROUP',1,'p_ComplementoGroupC','Lexico.py',293),
  ('COMPLEMENTOGROUP -> ID PUNTO ID','COMPLEMENTOGROUP',3,'p_ComplementoGroupC1','Lexico.py',296),
  ('VALORES -> POR','VALORES',1,'p_Valores','Lexico.py',299),
  ('VALORES -> LISTAVALORES','VALORES',1,'p_ValoresLista','Lexico.py',302),
  ('LISTAVALORES -> LISTAVALORES COMA VALOR','LISTAVALORES',3,'p_ListaValores','Lexico.py',305),
  ('LISTAVALORES -> VALOR','LISTAVALORES',1,'p_ListaValoresS','Lexico.py',308),
  ('VALOR -> ID ALIAS','VALOR',2,'p_Valor','Lexico.py',311),
  ('VALOR -> ID PUNTO ID ALIAS','VALOR',4,'p_Valor2','Lexico.py',314),
  ('VALOR -> ID','VALOR',1,'p_Valor3','Lexico.py',317),
  ('VALOR -> ID PUNTO ID','VALOR',3,'p_Valor4','Lexico.py',320),
  ('VALOR -> PABRE SUBCONSULTA PCIERRA ALIAS','VALOR',4,'p_ValorSub','Lexico.py',323),
  ('VALOR -> PABRE SUBCONSULTA PCIERRA','VALOR',3,'p_ValorSub1','Lexico.py',326),
  ('VALOR -> COUNT PABRE POR PCIERRA ALIAS','VALOR',5,'p_ValorCountAa','Lexico.py',329),
  ('VALOR -> COUNT PABRE ID PCIERRA ALIAS','VALOR',5,'p_ValorCounta','Lexico.py',332),
  ('VALOR -> COUNT PABRE POR PCIERRA','VALOR',4,'p_ValorCountA','Lexico.py',335),
  ('VALOR -> COUNT PABRE ID PCIERRA','VALOR',4,'p_ValorCount','Lexico.py',338),
  ('VALOR -> COUNT PABRE ID PUNTO ID PCIERRA ALIAS','VALOR',7,'p_ValorCountAliasId','Lexico.py',341),
  ('VALOR -> COUNT PABRE ID PUNTO ID PCIERRA','VALOR',6,'p_ValorCountIdP','Lexico.py',344),
  ('VALOR -> FUNCION PABRE ID PUNTO ID PCIERRA','VALOR',6,'p_ValorFunciones','Lexico.py',347),
  ('VALOR -> FUNCION PABRE ID PCIERRA','VALOR',4,'p_ValorFunciones1','Lexico.py',350),
  ('VALOR -> FUNCION PABRE ID PUNTO ID PCIERRA ALIAS','VALOR',7,'p_ValorFuncionesA','Lexico.py',353),
  ('VALOR -> FUNCION PABRE ID PCIERRA ALIAS','VALOR',5,'p_ValorFunciones1A','Lexico.py',356),
  ('FUNCION -> AVG','FUNCION',1,'p_funcionAvg','Lexico.py',359),
  ('FUNCION -> SUM','FUNCION',1,'p_funcionSum','Lexico.py',362),
  ('FUNCION -> MIN','FUNCION',1,'p_funcionMin','Lexico.py',365),
  ('FUNCION -> MAX','FUNCION',1,'p_funcionMax','Lexico.py',368),
  ('ALIAS -> AS ID','ALIAS',2,'p_Alias','Lexico.py',371),
  ('ALIAS -> ID','ALIAS',1,'p_AliasS','Lexico.py',374),
  ('PFROM -> FROM ID ALIAS','PFROM',3,'p_FromIdA','Lexico.py',377),
  ('PFROM -> FROM ID','PFROM',2,'p_FromId','Lexico.py',380),
  ('PFROM -> FROM PABRE SUBCONSULTA PCIERRA ALIAS','PFROM',5,'p_FromSub','Lexico.py',383),
  ('SUBCONSULTA -> SELECT VALORES PFROM COMPLEMENTO','SUBCONSULTA',4,'p_SubconsultaFrom','Lexico.py',386),
  ('SUBCONSULTA -> SELECT VALORES PFROM PWHERE COMPLEMENTO','SUBCONSULTA',5,'p_SubconsultaFromW','Lexico.py',389),
  ('PWHERE -> WHERE CONDICION','PWHERE',2,'p_Where','Lexico.py',393),
  ('CONDICION -> CONDICION IGUAL CONDICION','CONDICION',3,'p_CondicionIgual','Lexico.py',396),
  ('CONDICION -> CONDICION DIF CONDICION','CONDICION',3,'p_CondicionDif','Lexico.py',399),
  ('CONDICION -> CONDICION DIF1 CONDICION','CONDICION',3,'p_CondicionDif1','Lexico.py',402),
  ('CONDICION -> CONDICION MENOR CONDICION','CONDICION',3,'p_CondicionMenor','Lexico.py',405),
  ('CONDICION -> CONDICION MENORIGUAL CONDICION','CONDICION',3,'p_CondicionMenorI','Lexico.py',408),
  ('CONDICION -> CONDICION MAYOR CONDICION','CONDICION',3,'p_CondicionMayor','Lexico.py',411),
  ('CONDICION -> CONDICION MAYORIGUAL CONDICION','CONDICION',3,'p_CondicionMayorI','Lexico.py',414),
  ('CONDICION -> CONDICION AND CONDICION','CONDICION',3,'p_CondicionAnd','Lexico.py',417),
  ('CONDICION -> CONDICION OR CONDICION','CONDICION',3,'p_CondicionOr','Lexico.py',420),
  ('CONDICION -> NOT CONDICION','CONDICION',2,'p_CondicionNot','Lexico.py',423),
  ('CONDICION -> PABRE CONDICION PCIERRA','CONDICION',3,'p_CondicionParentesis','Lexico.py',426),
  ('CONDICION -> CONDICION MAS CONDICION','CONDICION',3,'p_CondicionMas','Lexico.py',429),
  ('CONDICION -> CONDICION MENOS CONDICION','CONDICION',3,'p_CondicionMenos','Lexico.py',432),
  ('CONDICION -> CONDICION POR CONDICION','CONDICION',3,'p_CondicionPor','Lexico.py',435),
  ('CONDICION -> CONDICION DIVIDIDO CONDICION','CONDICION',3,'p_CondicionDiv','Lexico.py',438),
  ('CONDICION -> CONDICION MODULO CONDICION','CONDICION',3,'p_CondicionMod','Lexico.py',441),
  ('CONDICION -> CONDICION EXP CONDICION','CONDICION',3,'p_CondicionExp','Lexico.py',444),
  ('CONDICION -> CONDICION IS CONDICION','CONDICION',3,'p_CondicionIs','Lexico.py',447),
  ('CONDICION -> CONDICION ISNULL CONDICION','CONDICION',3,'p_CondicionIsN','Lexico.py',450),
  ('CONDICION -> CONDICION NOTNULL CONDICION','CONDICION',3,'p_CondicionNotN','Lexico.py',453),
  ('CONDICION -> MENOS CONDICION','CONDICION',2,'p_CondicionM','Lexico.py',456),
  ('CONDICION -> MAS CONDICION','CONDICION',2,'p_CondicionP','Lexico.py',459),
  ('CONDICION -> NUMERO','CONDICION',1,'p_CondicionNum','Lexico.py',462),
  ('CONDICION -> DECIMAL','CONDICION',1,'p_CondicionDec','Lexico.py',465),
  ('CONDICION -> CADENA','CONDICION',1,'p_CondicionCad','Lexico.py',468),
  ('CONDICION -> TRUE','CONDICION',1,'p_CondicionTrue','Lexico.py',471),
  ('CONDICION -> FALSE','CONDICION',1,'p_CondicionFalse','Lexico.py',474),
  ('CONDICION -> ID','CONDICION',1,'p_CondicionId','Lexico.py',477),
  ('CONDICION -> ID PUNTO ID','CONDICION',3,'p_CondicionIdP','Lexico.py',480),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','Lexico.py',483),
]
