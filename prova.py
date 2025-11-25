def depositar(valor_depositado, saldo):
  if valor_depositado <= 0:
    print("Valor inválido!")
    return saldo
  
  novoSaldo = valor_depositado + saldo
  print(f"Depósito de R${valor_depositado:.2f} feito com sucesso!")
  return novoSaldo

def saque(valorSaque, saldo):
  if valorSaque > saldo:
    print("Saldo indisponível")
    return saldo
  elif valorSaque <= 0:
    print("Valor de saque inválido")
    return saldo
  else:
    novoSaldo = saldo - valorSaque
    print(f"Saque de R${valorSaque:.2f} Efetuado com sucesso!")
    return novoSaldo

saldo = 0
while True:
  print("===Caixa Eletrônico===")
  print("1 - Depositar Dinheiro ")
  print("2 - Sacar Dinheiro ")
  print("3 - Ver Saldo ")
  print("4 - Encerrar o Programa ")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    deposito = float(input("Digite o valor do depósito: "))
    saldo = depositar(deposito, saldo)
    print(f"Seu saldo é de: R${saldo:.2f}")
  elif opcao == "2":
    valorSaque = float(input("Digite o valor de saque que deseja: "))
    saldo = saque(valorSaque, saldo)
    print(f"Seu saldo é de: R${saldo:.2f}")
  elif opcao == "3":
    print(f"Seu saldo é de: R${saldo:.2f}")
  elif opcao == "4":
    print("Encerrando programa...")
    break
  else:
    print("Opção inválida, tente novamente.")
