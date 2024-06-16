def count_occurrences(lst, elem):
    return lst.count(elem)

lst = input("Enter a list of elements (separated by spaces): ")
lst = [x for x in lst.split()]

elem = input("Enter the element to count: ")

result = count_occurrences(lst, elem)

print(f"The element '{elem}' occurs {result} times in the list.")