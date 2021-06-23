# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*notas, situacao=False):
    '''
    => Função para analisar notas de uma turma de alunos
    :param notas: aceita inserir várias notas dos alunos.
    :param situacao:mostra a situação da turma (opcional)
    :return:mostra vários dados criados a partir das notas da turma
    '''
    infos = {}
    print("As notas informadas foram: ", end=" ")
    for valor in notas:
        print(f"{valor}", end="")
        if valor == notas[-1]:
            print("")
        else:
            print(" / ", end="")
    media = sum(notas) / len(notas)
    infos["total de notas"] = len(notas)
    infos["maior nota"] = max(notas)
    infos["menor nota"] = min(notas)
    infos["media da turma"] = media
    if situacao:
        if media >= 7:
            infos["situação"] = "BOA"
        elif 5 <= media < 7:
            infos["situação"] = "RAZOÁVEL"
        else:
            infos["situação"] = "RUIM"
    return infos


#  Programa principal
dados = notas(5, 2.5, 1, 6, situacao=True)
print(dados)

