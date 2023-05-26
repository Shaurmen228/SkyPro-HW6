import random


def get_list_words() -> list:
    """
    Считываем с файла слова в лист
    """
    with open("words.txt") as file:
        list_words = file.readlines()
        list_words = [line.strip() for line in list_words]
    return list_words


def write_statistics(player_name: str, score: int):
    """
    Запись статистики в текстовый файл
    """
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{player_name} {score}")


def get_statistics():
    """
    Получение статистики
    :return:
    """
    dict_player = {}
    list_score = []
    with open("history.txt") as file:
        contents = file.readlines()

    for line in contents:

        line = line.rstrip()
        split_line = line.split(" ")
        dict_player[split_line[0]] = split_line[1]
        list_score = list(map(int, dict_player.values()))

    print(f"\nВсего игр сыграно: {len(dict_player)}\nМаксимальный рекорд: {max(list_score)}")


def run():
    player_name = input("Введите ваше имя: ")
    list_words = get_list_words()
    total_score = 0

    for word in list_words:
        word_list = list(word)
        random.shuffle(word_list)

        print(f"Угадайте слово: {''.join(word_list)}")
        response = input("Введите слово: ")

        if response.lower().strip(" ") == word:
            print("Верно! Вы получаете 10 очков.")
            total_score += 10
        else:
            print(f"Неверно! Верный ответ – {word}.")

    write_statistics(player_name, total_score)
    get_statistics()


def main():
    run()


main()
