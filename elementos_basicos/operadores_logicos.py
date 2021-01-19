# Existen 3  Operadores logicos Y SE PRIORIZAN
'''
  NOT  -> NEGACIÓN
  AND  -> CONJUNCIÓN
  OR   -> DISYUNCIÓN
PRIORIDAD GENERAL
1. ()
2. **
3. *, /, MOD, NOT
4. >, <, ==, >=, <=, !=, OR
'''

a = 10
b = 15
c = 20

resultado = not((a<b) and (b<c))
print(resultado)