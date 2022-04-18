import random

fortune_number = random.randint(1,3)
lucky_number = random.randint(1,100)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "Você terá um dia incrível"
if fortune_number == 2:
    fortune_text = "Seu dia será mais ou menos"
if fortune_number == 3:
    fortune_text = "Seu dia será horrível, não saia de casa"

print(f"{fortune_text}. Seu número da sorte é : {lucky_number}")