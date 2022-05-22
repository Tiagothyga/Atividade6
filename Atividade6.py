#Crie um sistema que imprima um recibo de compras para o usuário. O sistema vai perguntar a 
# quantidade de itens diferentes e depois vai perguntar qual o nome do item e a quantidade deste 
# item. No final o programa exibe o recibo juntamente com o valor final da compra. Veja um exemplo 
# de como o sistema deve funcionar: 
#
#>> Quantidade de itens diferentes: 2
#>> Nome do item 1: Bolacha
#>> Quantidade deste produto: 3
#>> Valor unitário deste produto: 1.50
#>> Nome do item 2: Suco caixinha
#>> Quantidade deste produto: 1
#>> Valor unitário deste produto: 2
#=============================
#                 Recibo:
#Quantidade  |   Nome   |   Valor
#3 Bolacha R$4.50   
#1 Suco caixinha R$2.00
#
#Total 6.50
#=============================
#
#Neste exercício vocês devem usar o dicionário para representar um 
# produto, e os laços para fazer as iterações conforme o número de 
# itens diferentes pedido no exercício.
#
#Para entregar essa atividade desenvolva o código de cada um dos exercícios
#e coloque-os no Github. Aqui no Classroom envie apenas o link para seu código.

print("Bem vindo(a) ☺️")
QID = int(input("Quantidade de itens: "))

itens = []

i =0
while i < QID:
    nome_item = input("Nome do iten {}: ".format(i+1))
    quantidade = float(input("Quantidade deste item: "))
    valor_produto = float(input("Valor unitario do item: "))

    item = {
        "nome": nome_item,
        "quantidade": quantidade,
        "valor": valor_produto
    }

    itens.append(item)
    
    i+=1

total = 0

print("=============================================")
print("              Recibo")
print("_____________________________________________")
print(" Quantidade  │ Nome do item  │   Valor")

for item in itens:
    print("     {}     │   {}       │    R${}".format(item["quantidade"], item["nome"], item["valor"]))
    total += item["valor"] * item["quantidade"]
print("---------------------------------------------")
print("Total: R$",total)
print("=============================================")