def print_m(m):  # функция вывода матриц на экран
    for i in m: print(i)
    print()


def clozhenie(tuple_of_matrices):
    m1 = tuple_of_matrices[0]
    m2 = tuple_of_matrices[1]
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):  # проверка на совпадение размеров матриц
        print('Извините, я так не умею (никто не умеет)')
    else:
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m1[i][j] += m2[i][j]
        print_m(m1)


def multiplication(tuple_of_matrices):
    m1 = tuple_of_matrices[0]
    m2 = tuple_of_matrices[1]
    if len(m1[0]) != len(m2):
        print('Павел Андреевич вы дебил')
    else:
        matritsa = [[0] * len(m1) for i in range(len(m2[0]))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                s = 0
                for k in range(len(m2)):
                    s += m1[i][k] * m2[k][j]
                    matritsa[i][j] = s
        return matritsa


def find_reversed_matrix(m):
    def check(m, reversed_m):
        mult = multiplication((m, reversed_m))
        for i in range(len(mult)):
            for j in range(len(mult[0])):
                mult[i][j] = round(mult[i][j])
                reversed_m[i][j] = round(reversed_m[i][j], 5)
        print('Ваша обратная матрица, сударь:')
        print_m(reversed_m)
        print('Результат умножения исходной матрицы на обратную (этому точно можно доверять, см. функцию check):')
        print_m(mult)

    def getMatrixMinor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def det(m):
        s = 0
        if len(m) == 1:  # дописано в конце
            return m[0][0]
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        else:
            for j in range(len(m)):
                s += (-1) ** (j + 1) * m[0][j] * det(getMatrixMinor(m, 0, j))
            return -s

    def transpose_matrix(m):
        trans_m = [[0 for j in range(len(m))] for i in range(len(m[0]))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                trans_m[i][j] = m[j][i]
        return trans_m

    if len(m) != len(m[0]):  # перемещено из функции det потому что зачем
        print('Ну всё, приехали. Как такое считать то??')
        raise Exception("You can't go on with it")
    else:
        n = len(m)
        determinant = det(m)
        if determinant == 0:
            print('Вы издеваетесь что ли... тут определитель 0')
            raise Exception("You can't go on with it")
        else:
            m_alg_dop, list_of_alg_dop = [], []
            for i in range(n):
                for j in range(n):
                    alg_dop_of_x = (-1) ** (i + j) * det(getMatrixMinor(m, i, j))
                    list_of_alg_dop.append(alg_dop_of_x)
            for i in range(0, len(list_of_alg_dop), n):
                m_alg_dop.append(list_of_alg_dop[i:i + n])
            trans_m = transpose_matrix(m_alg_dop)
            for i in range(n):  # делим на определитель
                for j in range(n):
                    trans_m[i][j] = trans_m[i][j] / determinant
            reversed_matrix = trans_m
            return check(m, reversed_matrix)


def what():  # функция, спрашивающая что делать с этими вашими матрицами
    v = int(input(
        'Введите "1" если хотите сложить матрицы, введите "2" если хотите умножить их и "3" если хотите найти обратную матрицу)))0))000 '))
    if v == 1:  # сложение получается
        clozhenie(inputMatrices(2))
    elif v == 2:  # умножение получается
        print_m(multiplication(inputMatrices(2)))
    elif v == 3:  # обратная матрица
        find_reversed_matrix(inputMatrices(1))
    else:
        print('Павел Андреевич, вы еблан!')


def inputMatrices(k):
    def do_matrix_please(n):  # составим матрицы по введённым размерам, вернём tuple из двух получившихся матриц
        print('Введите вашу матрицу построчно через пробелы')
        while True:
            try:
                matrix = [[i for i in list(map(int, input().split()))] for j in range(n)]
                break  # как только всё пройдёт без ошибок, мы выйдем из цикла
            except ValueError:
                print('Зачем вы вводите буковки/символы/пробелы?? Попробуйте ещё раз!)')
        max_len = max([len(i) for i in matrix])  # это длина самой длинной строки в матрице
        for i in matrix:
            if len(i) != max_len:  # если вдруг длина введённых пользователем строк оказалось разной
                i.extend([0 for i in range(max_len - len(i))])  # добавляем столько ноликов, сколько не хватает
        return matrix

    def input_n(number):  # чтобы избежать ошибки из-за введённой буквы вместо цифры
        flag = True
        while flag == True:
            try:
                n = int(input(f'Сколько строк будет матрице {number}? '))  # число строк матрицы
                flag = False
            except:
                print('Зачем вы вводите буковки/символы/пробелы?? Попробуйте ещё раз!)')
        return n

    if k == 1:
        m = do_matrix_please(input_n(1))
        return m
    m1 = do_matrix_please(input_n(1))
    m2 = do_matrix_please(input_n(2))
    return (m1, m2)


def main():  # главная функция
    what()


main()
