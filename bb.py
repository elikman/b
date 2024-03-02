def casting_algorithm(N, K):
    # Создаем список претендентов от 1 до N
    candidates = list(range(1, N + 1))
    
    # Индекс текущего претендента в списке
    current_index = 0
    
    # Пока в списке не останется один претендент
    while len(candidates) > 1:
        # Подсчитываем количество тактов и обновляем индекс
        current_index = (current_index + K - 1) % len(candidates)
        
        # Удаляем выбывшего претендента из списка
        candidates.pop(current_index)
    
    # Возвращаем номер победившего претендента
    return candidates[0]

# Чтение ввода
N = int(input())
K = int(input())

# Вызов функции и вывод результата
result = casting_algorithm(N, K)
print(result)
