def notas(* num, sit=0):
    '''
    -> Função para avaliar a nota e situação de varios alunos
    :param num: uma ou mais notas dos alunos
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return : dicionário com várias informações sobre a situaçao da turma'''

    nota = {}
    nota["total"] = len(num) 
    nota["maior"] = max(num)
    nota["menor"] = min(num)
    nota["media"] = sum(num)/len(num)

    if sit:
        if nota["media"] >= 8:
            nota["situaçao"] = "EXCELENTE"
        if 8 > nota["media"] > 6:
            nota["situaçao"] = "BOA"
        else:
            nota["situaçao"] = "PÉSSIMA"

    return nota



resp = notas(5.5, 2, 7, sit=False)
print(resp)