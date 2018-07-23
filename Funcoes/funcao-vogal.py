def vogal(letra):
  letra = letra.upper()
  if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
    return True
  else:
    return False

l = input("Digite a Letra : ")
print (vogal(l))