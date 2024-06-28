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

# Define countries by continent
european_countries = ["Belgium", "Portugal", "France", "Germany", "Spain"]
asian_countries = ["China", "Japan", "India", "South Korea", "Thailand"]

with open('sales.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)  # Read the header row

    # Initialize dictionaries to store counts and averages
    europe_data = {}
    asia_data = {}

    for country in european_countries:
        csvfile.seek(0)
        next(reader)  # Skip the header row again
        count_country = count(lambda x: x[1] == country, reader)
        csvfile.seek(0)
        next(reader)  # Skip the header row again
        avg_country = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == country, reader)))
        europe_data[country] = {'count': count_country, 'average': avg_country}
    
    for country in asian_countries:
        csvfile.seek(0)
        next(reader)  # Skip the header row again
        count_country = count(lambda x: x[1] == country, reader)
        csvfile.seek(0)
        next(reader)  # Skip the header row again
        avg_country = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == country, reader)))
        asia_data[country] = {'count': count_country, 'average': avg_country}

    # Print results for Europe
    print("Europe Sales Data:")
    for country, data in europe_data.items():
        print(f"{country}: Count = {data['count']}, Average = {data['average']:.2f}")

    # Print results for Asia
    print("Asia Sales Data:")
    for country, data in asia_data.items():
        print(f"{country}: Count = {data['count']}, Average = {data['average']:.2f}")
