# -*- coding: utf-8 -*-

import random

N = 0.1
AGE = 0
FILE = open("data/iris.data", 'r')
TRAINING_BASE_SIZE = 50
TEST_BASE_SIZE = 100 - TRAINING_BASE_SIZE
HITS_COUNT = 0
ERRORS_COUNT = 0


def sum_array(m1, m2):
    array_r = []

    for i in range(len(m1)):
        value = m1[i] + m2[i]
        array_r.append(round(value, 2))

    return array_r


def multiply_cons_array(c, array):
    array_r = []

    for i in range(len(array)):
        valor = array[i] * c
        array_r.append(round(valor, 2))

    return array_r


def sign(u):
    if u < 0:
        return -1
    elif u > 0:
        return 1
    else:
        return 0


def summation(m1, m2):
    u = 0.0

    for i in range(len(m1)):
        u = u + m1[i] * m2[i]

    return round(u, 2)


def new_weights(d, y, w, x):
    rate = N * (d - y)
    x_rate = multiply_cons_array(rate, x)

    return sum_array(w, x_rate)


if __name__ == "__main__":
    lines = FILE.readlines()
    random.shuffle(lines)

    training_base_array = []
    test_base_array = []

    x = []
    x_test = []
    d = []
    d_test = []

    w = [0.01, 0.34, -0.23, 0.94, 0.05]

    print("Training...")
    print("----------------------------")

    for i in range(len(lines)):
        attributes = lines[i].replace("\n", "").split(",")
        at_1 = float(attributes[0])
        at_2 = float(attributes[1])
        at_3 = float(attributes[2])
        at_4 = float(attributes[3])
        class_name = attributes[4]

        e = [at_1, at_2, at_3, at_4, class_name]

        if i < TRAINING_BASE_SIZE:
            training_base_array.append(e)

            x_k = [1.0, at_1, at_2, at_3, at_4]
            x.append(x_k)
            dd = 0

            if class_name == "Iris-setosa":
                dd = 1
            else:
                dd = -1

            d.append(dd)

        else:
            test_base_array.append(e)

            x_i_t = [1.0, at_1, at_2, at_3, at_4]
            x_test.append(x_i_t)

            dd = 0
            if class_name == "Iris-setosa":
                dd = 1
            else:
                dd = -1

            d_test.append(dd)

    for f in range(100):
        ERROR = False

        for j in range(len(training_base_array)):
            xx = x[j]

            u = summation(w, xx)
            dn = d[j]
            y = sign(u)

            if dn - y:
                v_x = x[j]
                w = new_weights(dn, y, w, v_x)

                ERROR = True
                AGE = AGE + 1

    print("Number of Ages:", AGE)
    print("Weights:", w, "\n")

    print("Testing...")
    print("----------------------------")

    for i in range(TEST_BASE_SIZE):
        u = summation(w, x_test[i])
        dn = d_test[i]
        y = sign(u)

        if y == -1:
            print("Decide for: Iris-virginica")
        if y == 1:
            print("Decide for: Iris-setosa")

        if dn == y:
            HITS_COUNT = HITS_COUNT + 1
        else:
            ERRORS_COUNT = ERRORS_COUNT + 1

    rate = round(((100.0 / TEST_BASE_SIZE) * HITS_COUNT), 2)

    print("\nResults")
    print("----------------------------")
    print("Amount of Hits:  ", HITS_COUNT)
    print("Amount of Errors:", ERRORS_COUNT)
    print("Hit Rate:        ", rate, "%")
