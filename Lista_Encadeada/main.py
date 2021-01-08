from random import randint
import timeit

class TimeMeasuring:

    def _init_(self):
        self.__start_time = 0
        self.__end_time = 0

    def start_time (self):
        self.__start_time = timeit.default_timer()

    def end_time(self):
        return round(timeit.default_timer() - self.__start_time, 4)


class Ordena:
    def quicksort(listNumDesord):
        if len(listNumDesord) <= 1: return listNumDesord
        num = listNumDesord[0]
        return Ordena.quicksort([i for i in listNumDesord if i < num]) + \
                [i for i in listNumDesord if i == num] + \
                Ordena.quicksort([i for i in listNumDesord if i > num])

    def counting_sort(listNumDesord):
        max_element = int(max(listNumDesord))
        min_element = int(min(listNumDesord))
        range_of_elements = max_element - min_element + 1

        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(listNumDesord))]

        for i in range(0, len(listNumDesord)):
            count_arr[listNumDesord[i] - min_element] += 1

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        for i in range(len(listNumDesord) - 1, -1, -1):
            output_arr[count_arr[listNumDesord[i] - min_element] - 1] = listNumDesord[i]
            count_arr[listNumDesord[i] - min_element] -= 1

        for i in range(0, len(listNumDesord)):
            listNumDesord[i] = output_arr[i]

        return listNumDesord

# Grava os valores de cada Nó
class Node:
    def __init__(self, value, next_node=None):
        self.__value = value
        self.next_node = next_node

    @property
    def value(self):
        return self.__value

# Monta, remove e mostra Lista
class LinkaLista:
    def __init__(self):
        self.__main_node = None

    #Adiciona a lista Encadeando
    def append(self, value):
        if self.__main_node is None:
            self.__main_node = Node(value)
            return

        curr_node = self.__main_node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = Node(value)

    # Remove da Lista e concerta encadeamento
    def remove(self, value):
        if self.__main_node is None:
            return

        left_node = None
        curr_node = self.__main_node

        if curr_node.value == value:
            self.__main_node = curr_node.next_node

        while True:
            left_node = curr_node
            curr_node = curr_node.next_node

            if curr_node is None:
                break

            if curr_node.value == value:
                left_node.next_node = curr_node.next_node

    # Tecnicamente transforma a lista em Array simples e retorna a lista encadeada
    def show(self):
        values = []
        curr_node = self.__main_node
        while curr_node is not None:
            values.append(curr_node.value)
            curr_node = curr_node.next_node
        print("Lista Linkada: {}".format(values))
        return values

# Chamada Main
def main():
    linked_list = LinkaLista()
    __time_measuring = TimeMeasuring()

    for x in range(500000):
        linked_list.append(randint(1, 500000))

    lista =  linked_list.show()


    __time_measuring.start_time() # Inicia cronometro
    print(Ordena.quicksort(lista))
    print(f"""Tempo Quick Sort:  {__time_measuring.end_time()} seg""") # Finaliza cronometro

    __time_measuring.start_time() # Inicia cronometro
    print(Ordena.counting_sort(lista))
    print(f"""Tempo Counting Sort:  {__time_measuring.end_time()} seg""") # Finaliza cronometro


if __name__ == "__main__":
    main()
