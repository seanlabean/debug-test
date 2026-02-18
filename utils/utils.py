def calculate_metrics(numbers):
    results = []
    for i, num in enumerate(numbers):
        # INTENTIONAL BUG: This will fail when num is 0
        # Perfect for demonstrating "Conditional Breakpoints" (i == 3)
        calc = 100 / num 
        results.append(calc)
    return sum(results)