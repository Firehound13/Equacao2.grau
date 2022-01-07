import math

a = float(input("Informe o valor de a:"))

if a == 0:
    print("Não é uma equação do segundo grau!")
else:
 b = float(input("Informe o valor de b:"))
 c = float(input("Informe o valor de c:"))
delta = (b * b) - (4 * a * c)

if delta < 0:
      print("Equação não tem raízes reais")
elif delta == 0:
      raiz = -b / 2 * a
      print(f"Equação tem uma raíz real {raiz}")
elif delta > 0:
      raiz1 = (-b + math.sqrt(delta)) / 2 * a
      raiz2 = (-b - math.sqrt(delta)) / 2 * a
      print(f"Equação tem duas raízes reais {raiz1} e {raiz2}!")

