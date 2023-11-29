def maximize_stocks_within_budget(N, Stocks_and_values, Amount):
    memo = [[-1] * (Amount + 1) for _ in range(N + 1)]

    def dp(index, remaining_amount):
        if index == N or remaining_amount == 0:
            return 0

        if memo[index][remaining_amount] != -1:
            return memo[index][remaining_amount]

        # Exclude the current stock
        result_without_current = dp(index + 1, remaining_amount)

        # Include the current stock if it fits within the budget
        current_stock_cost = Stocks_and_values[index][1]
        if current_stock_cost <= remaining_amount:
            result_with_current = Stocks_and_values[index][0] + dp(index + 1, remaining_amount - current_stock_cost)
            result_without_current = max(result_without_current, result_with_current)

        memo[index][remaining_amount] = result_without_current
        return result_without_current

    return dp(0, Amount)


def read_input(file_path):
    inputs = []
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        for i in range(0, len(lines), 3):
            N = int(lines[i])
            stocks_and_values_str = lines[i + 1][2:-2]  # Removing square brackets and extra characters
            stocks_and_values = [list(map(int, pair.split(', '))) for pair in stocks_and_values_str.split('], [')]
            Amount = int(lines[i + 2])
            inputs.append((N, stocks_and_values, Amount))
    return inputs


def write_output(file_path, results):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result}\n")


input_file_path = 'approachB_inputs.txt'
output_file_path = 'approachB_output.txt'

inputs = read_input(input_file_path)
results = [maximize_stocks_within_budget(*input_data) for input_data in inputs]
write_output(output_file_path, results)
