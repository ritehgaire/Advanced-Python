import csv
from functools import reduce

def count(predicate, itr):
    # Apply the predicate to filter the items in the iterable, and then count the filtered items
    count_filter = filter(predicate, itr)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
    return count_reduce

def average(itr):
    # Calculate the average of numbers in the iterable
    iterable = iter(itr)
    return avg_helper(0, iterable, 0)

def avg_helper(curr_count, itr, curr_sum): 
    # Helper function to recursively calculate the sum and count of the iterable items
    next_num = next(itr, "null")
    if next_num == "null": 
        # Return the average when all items are processed
        return curr_sum / curr_count
    curr_count += 1 
    curr_sum += next_num
    return avg_helper(curr_count, itr, curr_sum)

with open('sales.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)  # Read the header row
    count_belgium = count(lambda x: x[1] == "Belgium", reader)
    print(count_belgium)
    
    csvfile.seek(0)  # Reset the file pointer to the beginning
    next(reader)  # Skip the header row again
    avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
    print(avg_portugal)
