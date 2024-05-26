"""
EMAIL RESPONSE
Uma nova loja virtual vem migrando para um novo sistema de software para sua gestão de estoque. A última coisa que eles precisam fazer para que o novo sistema esteja totalmente operacional é completar suas mensagens de resposta à pesquisa.

Eles designaram alguém sem experiência em Python para trabalhar nele. Como seria de esperar, agora há bugs no código, e você foi solicitado a corrigir o relatório.

CHALLENGE
This section of the report should print:

Thank you for shopping at Bootmart!
Your total today was:
"""
items_in_cart = 5
cost_of_each_item = 2.50
total_cost = items_in_cart * cost_of_each_item

# Don't Touch Above This line
print("Thank you for shopping at Bootmart!")
print("Your total today was:")


# Don't Touch Below This Line

print(f"${total_cost:.2f}") 
"""
 O f na frente da string indica uma "f-string", que permite a inclusão de variáveis diretamente dentro da string. ${total_cost:.2f} significa que total_cost será formatado com duas casas decimais.
"""