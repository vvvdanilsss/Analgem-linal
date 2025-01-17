def reading_matrix(name="певой"):
    """
    Считывает матрицу и записывает ее в список
    :return: Сформированный список
    """
    n = int(input(f"Введите количество строк {name} матрицы (число): "))
    lst = []
    for i in range(n):
        lst.append(list(map(float, input(f"Введите строку номер {i + 1} (элементы через пробел): ").split())))
    return lst


def multipling_lists(lst1, lst2):
    """
    Умножает два вложенных списка
    :param lst1: Первый входной список
    :param lst2: Второй входной список
    :return: Конечный вложенный список
    """
    n1, m1, n2, m2 = len(lst1), len(lst1[0]), len(lst2), len(lst2[0])
    if m1 != n2:
        return "Перемножить не получится :( матрицы не согласованы"
    LST = []
    for i in range(n1):
        lst = []
        for j in range(m2):
            value = 0
            for k in range(m1):
                value += lst1[i][k] * lst2[k][j]
            lst.append(round(value, 3))
        LST.append(lst)
    return LST


def summarizes_lists(lst1, lst2):
    """
    Суммирует два вложенных списка
    :param lst1: Первый входной список
    :param lst2: Второй входной список
    :return: Конечный вложенный список
    """
    n1, m1, n2, m2 = len(lst1), len(lst1[0]), len(lst2), len(lst2[0])
    if n1 != n2 or m1 != m2:
        return "Сложить не получится :( размерности матриц не равны"
    else:
        LST = []
        for i in range(n1):
            lst = []
            for j in range(m1):
                lst.append(round(lst1[i][j] + lst2[i][j], 3))
            LST.append(lst)
        return LST


def converts_list_to_matrix(lst, name="Результат умножения: "):
    """
    Делает из вложенного списка матрицу
    :param lst: Входной список
    :return: Матрица
    """
    if type(lst) == str:
        print(lst)
    else:
        print(name)
        for line in lst:
            print(*line)


l1 = reading_matrix()
l2 = reading_matrix(name="второй")
converts_list_to_matrix(multipling_lists(l1, l2))
converts_list_to_matrix(summarizes_lists(l1, l2), name="Результат сложения: ")