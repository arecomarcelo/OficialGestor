from enum import Enum

'''
Enum.member.name: Retorna o nome do membro.
Enum.member.value: Retorna o valor do membro.
Enum(member_name): Converte uma string para um membro do enumerador.
Enum(value): Converte um valor para um membro do enumerador.
'''
class Direcao(Enum):
    DIREITA = 1
    ESQUERDA = 2