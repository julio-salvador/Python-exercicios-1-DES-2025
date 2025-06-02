#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

projetoX = int(input("Digite o tempo para o projeto X: "))
projetoY = int(input("Digite o tempo para o projeto Y: "))
projetoZ = int(input("Digite o tempo para o projeto Z: "))
 
if projetoX < 0 or projetoY < 0 or projetoZ < 0:
    print("Erro existe um número negativo.")
else:
    soma = projetoX + projetoY + projetoZ
    print(f"Tempo total do projeto: {soma} dias")