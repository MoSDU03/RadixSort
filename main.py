def countingSortForRadixSort(inputArray, placeValue):

    """
        linear sort algorithm.
    :param placeValue: the base
    :param inputArray: the input array to be sorted
    :return: sorted array
    """
    count = [0] * 10
    for i in range(len(inputArray)):
        """
        counting the iteration of each number in the array
        """
        placeElement = (inputArray[i] // placeValue) % 10
        count[placeElement] += 1

    for i in range(1, 10):
        """
        the sum of the elements less than x.
        it's used to know where to start to put the range of this number
        """
        count[i] += count[i-1]
    outputArray = [0] * len(inputArray)
    for i in range(len(inputArray) - 1, -1, -1):
        """
        put the sorted elements in the output array.
        """
        placeElement = (inputArray[i] // placeValue) % 10
        outputArray[count[placeElement] - 1] = inputArray[i]
        count[placeElement] -= 1
    return outputArray


def numLength(n):
    """

    :param n: the number we want its length
    :return: the length of the num
    """
    return len(str(n))


def getDigit(n, d):
    """
    get the digit d in the number n
    // ==> floor division
    """
    for i in range(d - 1):
        n //= 10
    return n % 10


def radixSort(inputArray):
    maxElement = max(inputArray)  # the max element in the input array
    num_digits = numLength(maxElement)  # the max number of digit for the max number in the input array
    placeValue = 1  # the beginning base least significant bit (LSB)
    outputArray = inputArray  # create output array the same size as input array
    for d in range(num_digits):  # looping the number of the digit
        outputArray = countingSortForRadixSort(outputArray, placeValue)  # sorting for the base place value
        placeValue *= 10  # increase the base * 10
    return outputArray


arr = [2, 20, 61, 997, 1, 619]
print(radixSort(arr))
