import random

def generate_problem(problem_type):
    if problem_type == "algebra":
        # Example: Solve 2x + 3 = 11
        x = random.randint(1, 10)
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = a * x + b
        problem = f"Solve for x: {a}x + {b} = {c}"
        return problem, x
    elif problem_type == "radical":
        # Example: What is the square root of n^2?
        n = random.randint(2, 12)
        problem = f"What is the square root of {n**2}?"
        return problem, n
    elif problem_type == "function":
        # Example: If f(x) = 2x + 1, what is f(3)?
        a = random.randint(1, 5)
        b = random.randint(0, 10)
        x = random.randint(1, 10)
        fx = a * x + b
        problem = f"If f(x) = {a}x + {b}, what is f({x})?"
        return problem, fx
    elif problem_type == "geometry":
        # Example: Area of a rectangle
        l = random.randint(2, 10)
        w = random.randint(2, 10)
        area = l * w
        problem = f"What is the area of a rectangle with length {l} and width {w}?"
        return problem, area
    elif problem_type == "statistics":
        # Example: Mean of three numbers
        nums = [random.randint(1, 20) for _ in range(3)]
        mean = sum(nums) / 3
        problem = f"What is the mean of {nums[0]}, {nums[1]}, and {nums[2]}? (Round to 2 decimals)"
        return problem, round(mean, 2)
    else:
        return "No problem available.", ""
