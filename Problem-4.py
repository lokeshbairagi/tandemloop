def count_multiples(numbers):
    counts = [0] * 10  # Initialize a list to store the counts of multiples from 1 to 9
    
    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:
                counts[i] += 1
    
    return counts

# Example usage
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
multiples_counts = count_multiples(my_list)
