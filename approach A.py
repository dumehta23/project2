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


def read_input(file_path):
    inputs = []
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            N = int(lines[i])
            Stocks_and_values = eval(lines[i + 1])
            Amount = int(lines[i + 2])
            inputs.append((N, Stocks_and_values, Amount))
    return inputs


def write_output(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result}\n")


if __name__ == "__main__":
    input_file_path = "approachA_inputs.txt"
    output_file_path = "approachA_output.txt"

    inputs = read_input(input_file_path)
    results = []

    for input_data in inputs:
        result = maximize_stocks_within_budget(*input_data)
        results.append(result)

    write_output(output_file_path, results)
