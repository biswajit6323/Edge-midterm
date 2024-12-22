def generate_odd_series(limit):
    odd_series = []
    for num in range(1, limit + 1):
        if num % 2 != 0:
            odd_series.append(num)
    return odd_series
def sum_series(series):
    return sum(series)
odd_series = generate_odd_series(1000)
sum_of_odd_series = sum_series(odd_series)
print("Series of odd integers up to 1000:")
print(odd_series)
print("\nSum of the odd integer series:")
print(sum_of_odd_series)