# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
from random import randint


def pseudo(filename):
    vowel="аоуыэяёюие"
    consonant="бвгджзйкдмнлнпрстфхцчшщъь"

    name_lenght = randint(4,7)
    vowel_number = randint(1, name_lenght)
    consonant_number = name_lenght-vowel_number

    x=random.sample(vowel,vowel_number)
    y=random.sample(consonant,consonant_number)
    s = x+y
    random.shuffle(s)

    # print(''.join(s).title())
    with open(filename, "a", encoding="utf-8") as file:
        file.write(''.join(s).title()+"\n")

if __name__ == "__main__":
    pseudo("names.txt")
