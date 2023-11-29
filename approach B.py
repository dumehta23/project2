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

