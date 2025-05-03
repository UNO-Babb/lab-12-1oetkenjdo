# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of numbers for each run.
# You can change the number of elements in the arrays.
# We will test 3 arrays: one that is already in order, one that is sorted in reverse order, and one that is random.

import time
import random
import AllSorts

def main():
    random.seed(2025)  
    numberTerms = 10000  

    orderedList = list(range(numberTerms))
    reversedList = list(range(numberTerms, 0, -1))
    randomList = [random.randint(1, 10000) for _ in range(numberTerms)]


    sorts = [
        ("Bubble Sort", AllSorts.bubbleSort),
        ("Bubble Sort Early Exit", AllSorts.bubbleSortEarlyExit),
        ("Selection Sort", AllSorts.selectionSort),
        ("Insertion Sort", AllSorts.insertionSort),
        ("Merge Sort", AllSorts.mergeSort),
    ]


    lists = [
        ("Ordered", orderedList),
        ("Reversed", reversedList),
        ("Random", randomList),
    ]


    print(f"Begin Sorting {numberTerms} elements.\n")


    with open("results.txt", "w") as f:
        f.write(f"Sorting {numberTerms} elements.\n\n")


        for sort_name, sort_func in sorts:
            print(f"=== {sort_name} ===")
            f.write(f"=== {sort_name} ===\n")
            for list_type, data in lists:
                data_copy = data.copy()
                print(f"{list_type} list:")
                f.write(f"{list_type} list:\n")
                startTime = time.time()
                sort_func(data_copy)
                endTime = time.time()
                elapsedTime = endTime - startTime
                print(f"Time: {elapsedTime:.5f} seconds\n")
                f.write(f"Time: {elapsedTime:.5f} seconds\n\n")

    print("Sorting Complete. Results saved to 'results.txt'.")


if __name__ == '__main__':
    main()
