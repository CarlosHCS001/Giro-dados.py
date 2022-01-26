from random import randint
repeat_rolling = True
while repeat_rolling:
    print("Vôce rolou o dado e o resultado é o seguinte -",randint(1,10))
    print("Vôce deseja rolar o dado denovo ?")
    repeat_rolling = ("s" or "sim") in input().lower()