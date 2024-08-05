# import os

# current_path = r'g:\Meu Drive\TI Oficial\Projetos\Cobranca\Envio_Whatsapp'
# parent_path = os.path.dirname(current_path)
# grandparent_path = os.path.dirname(parent_path)

# print(grandparent_path)



import os

desired_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(desired_path)
