def find_fibnocii_numbers(n):
    if n <= 1:
        return 1
    else:
        return find_fibnocii_numbers(n-1) + find_fibnocii_numbers(n-2)

# find fibnocii numbers


print(find_fibnocii_numbers(3))
