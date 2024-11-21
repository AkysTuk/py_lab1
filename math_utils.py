def factorial(n):
    """
    Обчислює факторіал числа n.
    :param n: Ціле число, для якого потрібно обчислити факторіал.
    :return: Факторіал числа n.
    """
    if n < 0:
        raise ValueError("Факторіал визначено тільки для невід'ємних чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_even_numbers(numbers):
    """
    Обчислює суму всіх парних чисел у списку.
    :param numbers: Список чисел.
    :return: Сума парних чисел.
    """
    return sum(num for num in numbers if num % 2 == 0)