class WordsFinder:
    # таблица преобразования для str.translate
    trans_table = str.maketrans('.!,:;=?', '       ')

    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        '''
        подготовительный метод, считывает содержимое файлов self.file_names
        и возвращает словарь с ключом названия файла и значением списка всех
        слов в файле
        '''
        all_words = {}
        for file_name in self.file_names:
            with open(file_name) as file:
                content = file.read()
                content = content.lower() \
                                 .replace(' - ', ' ') \
                                 .translate(self.trans_table)
                content = ' '.join(content.split())
                all_words[file_name] = content.split()
        return all_words

    def find(self, search_word: str):
        '''
        возвращает словарь с ключом названия файла и значением первой позиции
        искомого слова
        '''
        search_word = search_word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            found = False
            for i in range(len(words)):
                if words[i] == search_word:
                    found = True
                    break
            if found:
                found_words[file_name] = i + 1  # позиция начинается с 1
        return found_words

    def count(self, search_word: str):
        '''
        возвращает словарь с ключом названия файла и значением количества
        нахождений искомого слова
        '''
        search_word = search_word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(search_word)
        return word_number


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    # print()
    # print('the')
    # finder = WordsFinder("Mother Goose - Monday’s Child.txt",
    #                      'Rudyard Kipling - If.txt',
    #                      'Walt Whitman - O Captain! My Captain!.txt')
    # print(finder.get_all_words())
    # print(finder.find('the'))
    # print(finder.count('the'))
