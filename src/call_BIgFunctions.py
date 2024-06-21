# call_big_functions.py
from java.util import ArrayList
import BigFunctions

def main():
    print("Factorial of 5:", BigFunctions.factorial(5))

    # sortArray
    array = [5, 2, 8, 3, 1]
    sorted_array = BigFunctions.sortArray(array)
    print("Sorted array:", sorted_array)
    list_of_strings = ArrayList()
    list_of_strings.add("apple")
    list_of_strings.add("banana")
    list_of_strings.add("cherry")
    list_of_strings.add("date")
    list_of_strings.add("fig")
    filtered_list = BigFunctions.filterByLength(list_of_strings, 5)
    print("Filtered list:", list(filtered_list))

    # Call the concatenateStrings function
    concatenated_string = BigFunctions.concatenateStrings("Hello, ", "world!")
    print("Concatenated string:", concatenated_string)

    # Call the findMax function
    max_element = BigFunctions.findMax(array)
    print("Maximum element in array:", max_element)

if __name__ == "__main__":
    main()
