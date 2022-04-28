import numpy as np

def interval_predict(number:int=1) -> int:
    
    """Пишем функцию которая угадывает число загаднное компьютером в интервале от 1 до 100

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        count - Число попыток
    """
    
    count = 0
    min_digit = 0  #начало интервала 
    max_interval = 100 #верхняя граница интервала

    while True:
        count += 1
        mid_number = round((min_digit+max_interval)/2) # в каждом шаге берем среднее значение в искомом интервале
        
        if mid_number > number: #  в каждом цикле сужаем пополам интервал поиска иходного значения
            max_interval = mid_number
        elif mid_number < number:
            min_digit = mid_number
        else:
            ##print(f"Число угадано за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
            
    return(count)


def score_game(interval_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        interval_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(interval_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(interval_predict)