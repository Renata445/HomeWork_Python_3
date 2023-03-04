list = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

W = input("Введите слово: ").upper()
sum = 0
for i in W:
    for l, k in list.items():
        if i in k:
            sum += l
print(f"Стоимость слова: {sum}")