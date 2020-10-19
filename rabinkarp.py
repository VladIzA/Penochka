
def rabin_karp (text, pattern):

    pattern_sum = sum(ord(s) for s in pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    number = 0
    proverka = False

    for i in range(text_length - pattern_length):    #Начинаю с 1 символа до символа, равного разнице длин строки и подстроки
        part = text[i:(pattern_length + i)]          #Рассматриваю часть строки, равной по длине искомой подстроки
        text_sum = sum(ord(s) for s in part)
        if pattern_sum == text_sum:                  #Сравниваю суммы числовых значений символов
            for j in range(len(part) - 1):
                if ord(part[j]) != ord(pattern[j]):  #Если какие-либо символы не совпадают то цикл прерывается
                     proverka = False; break
                else: proverka = True
            if proverka == True:                     #Если всё совпало, то к количеству совпадений прибавляется 1
                number += 1           
    return number

a = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
b = "Иван"

print(rabin_karp(a, b))