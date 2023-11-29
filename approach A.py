def maximize_stocks_within_budget(N, Stocks_and_values, Amount):
    max_count = 0
    num_items = N

    for i in range(2 ** num_items):
        total_value = 0
        total_stocks = 0

        for j in range(num_items):
            if (i & (1 << j)) > 0:
                total_value += Stocks_and_values[j][1]
                total_stocks += Stocks_and_values[j][0]

        if total_value <= Amount and total_stocks > max_count:
            max_count = total_stocks

    return max_count


def process_input_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        # Read the number of test cases
        num_test_cases = int(input_file.readline().strip())

        for _ in range(num_test_cases):
            # Read N (size of items)
            N = int(input_file.readline().strip())

            # Read Stocks_and_values (list of items)
            Stocks_and_values = [list(map(int, input_file.readline().strip()[1:-1].split(', '))) for _ in range(N)]

            # Read Amount (budget)
            Amount = int(input_file.readline().strip())

            # Call the function and write the result to the output file
            result = maximize_stocks_within_budget(N, Stocks_and_values, Amount)
            output_file.write(str(result) + '\n')


# Example usage
input_filename = 'approachA_inputs.txt'
output_filename = 'approachA_outputs.txt'
process_input_file(input_filename, output_filename)
