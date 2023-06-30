import math

def solve_logarithm(base, result):
    """
    Решает логарифмическое уравнение log_base(x) = result.

    Параметры:
    - base: Основание логарифма (int или float).
    - result: Значение логарифма (int или float).

    Возвращает:
    - Значение x, которое удовлетворяет уравнению (int или float).
    """
    return math.pow(base, result)

# Пример использования
base = 10   # Основание логарифма
result = 2  # Значение логарифма

solution = solve_logarithm(base, result)
print(f"Решение логарифма: {solution}")
