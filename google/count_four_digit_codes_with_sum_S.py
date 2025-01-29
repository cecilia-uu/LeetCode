def googleCountWithSumS(S: int) -> int:
    def count_ways(sum_so_far, digit_count):
        # Base case: If 4 digits are used and sum matches S
        if digit_count == 4:
            return 1 if sum_so_far == S else 0

        # If the sum exceeds S, stop further exploration
        if sum_so_far > S:
            return 0

        # Count combinations using recursion for the next digit
        count = 0
        for digit in range(10):
            count += count_ways(sum_so_far + digit, digit_count + 1)

        return count

    # Start recursion with initial sum as 0 and 0 digits used
    return count_ways(0, 0)

print(googleCountWithSumS(35))
print(googleCountWithSumS(4))
print(googleCountWithSumS(2))