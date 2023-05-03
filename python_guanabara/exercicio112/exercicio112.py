#from utilidades import moeda
from utilidades.moeda import resumo
from utilidades.dados import leia_dinheiro

#from moeda import moeda, metade, dobro, aumentar, diminuir

valor = leia_dinheiro("Digite um valor em reais: R$")

#moeda.resumo(valor, 80, 35)
resumo(valor,80,20)
