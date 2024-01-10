# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну одного слова на інше.
# Виведіть триманий рядок на екрані.

input_string = input("Enter string: ")
word_to_find = input("Enter word to find: ")
replacement_word = input("Enter word to replace: ")
final_string = input_string.replace(word_to_find, replacement_word)

print(f"final string: {final_string}")

