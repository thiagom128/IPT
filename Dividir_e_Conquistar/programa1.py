import math


def SegmentoSomaMaxima(A, low, mid, high):

    left_sum = -math.inf
    _sum = 0
    max_left = 0
    for i in range(mid, low, -1):
        _sum = _sum + A[i]
        if (_sum > left_sum):
            left_sum = _sum
            max_left = i

    right_sum = -math.inf
    _sum = 0
    max_right = 0
    for i in range(mid + 1, high):
        _sum = _sum + A[i]
        if (_sum > right_sum):
            right_sum = _sum
            max_right = i
    return max_left, max_right, (left_sum + right_sum)


def Subarray(A, low, high):

    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high) / 2)

        left_low, left_high, left_sum = Subarray(A, low, mid)
        right_low, right_high, right_sum = Subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = SegmentoSomaMaxima(A, low, mid, high)

        if ((left_sum >= right_sum) and (left_sum >= cross_sum)):
            return left_low, left_high, left_sum
        elif ((right_sum >= left_sum) and (right_sum >= cross_sum)):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    #Extraido do Texto para validar o Algoritmo.
    #A = [-16, 20, -10, 12, 27, -6, -4, 8]
    print("Vamos iniciar o problema de dividir e conquistar!!!!")
    print("Inserir a seguir os numeros no formato ( Numero, Numero,) ")
    print("Exemplo: -1,2,0,9")
    A = [int(x) for x in input("\nEntre com os valores: ").split(", ")]
    low,high,sum = Subarray(A, 0, len(A) - 1)
    print("Resultado: \n1. cross_low = {}  \n2. cross_hight = {} \n3. cross_sum = {} ".format(low,high,sum))