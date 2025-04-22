"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""

import numpy as np 

def random_predict(number: int=1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return (count)    

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем угадывает наш подход 

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_lst = []
    np.random.seed(1) #фиксируем сид для воспроизводимости 
    random_arrey = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_arrey:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst))  
    print(f"Ваш aлгоритм угадывает число в среднем за: {score} попыток!")  
    return(score)    


if __name__ == '__main__':
    score_game(random_predict)       
        
#print(f"Количество попыток: {random_predict(35)}") 