#pinheirocfc@gmail.com
#https://github.com/Wesley-Pinheiro

#executar esta comando no terminal para instalar a biblioteca: pip install pycep_correios
import pycep_correios 

#variavel com o CEP para consulta
iCEP = '79814530'

if len(iCEP) == 8:

    #chama a consulta do CEP
    try:
        endereco = pycep_correios.consultar_cep(str(iCEP))
    except:
        print("Erro ao consultar CEP")

    #se as respostas forem vazias nao encontrou o CEP
    if endereco['cidade'] != None or endereco['cidade'] != ' ':
        #respostas da consulta
        print('endereco completo: ' + str(endereco))
        print(endereco['end'])
        print(endereco['bairro'])
        print(endereco['cidade'])
        print(endereco['uf'])
        print(endereco['cep'])
    else:
        print('CEP nao localizado')
else:
    #cep informado nao esta no formato correto
    print('Informe o CEP com 8 caracteres no formato: 00000000')
