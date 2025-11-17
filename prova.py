# def exibir_produto (nome, preco):
#   return f"O produto {nome}, custa R${preco}"

# nome = input("Digite o nome do produto: ")
# price = float(input("Digite o preço do produto: "))

# resultado = exibir_produto(nome=nome, preco=price)

# print(resultado)
# ========================================================

# def calcular_desconto(preco, desconto):
#   valor_desconto = preco * (desconto / 100)
#   preco_final = preco - valor_desconto
#   return f"O valor final com desconto é R${preco_final:.2f}"

# resultado = calcular_desconto(1000, 20)

# print(resultado)
# =========================================================

# def celsius_para_fahrenheit(celsius):
#   to_fah = (celsius * 9/5) + 32
#   return f"{celsius}°C equivale a {to_fah}°F"

# ask_user = int(input("Digite a temperatura em Celsius: "))
# print(celsius_para_fahrenheit(ask_user))
# ==========================================================

# def imposto_sobre_salario(bruto, imposto=15):
#   calc = bruto * (imposto / 100)
#   liquido = bruto - calc
#   return f"Valor de imposto a ser pago = R${calc:.2f},\n salario liquido = R${liquido:.2f}"

# print(imposto_sobre_salario(3000, 20))
# ===========================================================

# def calcular_media(notas):
#   return sum(notas) / len(notas)

# def aprovado_reprovado(media):
#   if media < 7:
#     print("Reprovado")
#   else:
#     print("Aprovado")

# notas = []
# for i in range(1, 5):
#   nota = float(input(f"Digite sua nota {i}: "))
#   notas.append(nota)

# media = calcular_media(notas)
# print(f"Sua média foi {media:.1f}")
# aprovado_reprovado(media)
# =======================================================

def depositar(valor_depositado, saldo):
  if valor_depositado <= 0:
    print("Valor inválido!")
    return saldo
  
  novoSaldo = valor_depositado + saldo
  print(f"Depósito de R${valor_depositado:.2f} feito com sucesso!")
  return novoSaldo

saldo = 0
deposito = float(input("Digite o valor do depósito: "))
saldo = depositar(deposito, saldo)
print(f"Seu novo saldo é R${saldo:.2f}")

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

valorSaque = float(input("Digite o valor de saque que deseja: "))
saldo = saque(valorSaque, saldo)
print(f"Novo saldo= R${saldo:.2f}")
