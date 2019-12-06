input_list = input("Введіть кілька слів: ")
words = input_list.split()
words.sort()
print("Твої слова по алфовітному порядку: ")
for word in words:
    print(word)
