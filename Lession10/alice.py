from datetime import datetime


def count_words(filename):
    """Подсчет слов в файле"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        with open('missing_file.txt', 'a', encoding='utf-8') as mf:
            dt = datetime.today()
            mf.write(f"\n{filename} не найден.|| {dt}")
    else:
        # Подсчет приблизительного колличества слов в файле
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


file_names = ['alice.txt', 'asd.txt', 'test.txt', 'alibaba.txt']
for file_name in file_names:
    count_words(file_name)

