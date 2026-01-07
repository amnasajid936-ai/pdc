import asyncio
import sys

# Palindrome function
def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome

# Async coroutines
async def sum_coroutine(num):
    await asyncio.sleep(4)
    total = sum(range(1, num + 1))
    return f'Sum of first {num} integers = {total}'

async def factorial_coroutine(num):
    await asyncio.sleep(4)
    result = 1
    for i in range(2, num + 1):
        result *= i
    return f'Factorial of {num} = {result}'

async def palindrome_coroutine(strings):
    await asyncio.sleep(2)
    output = []
    for s in strings:
        rev, is_pal = reverse_and_check_palindrome(s)
        output.append(f"{s} → {rev} | Palindrome: {is_pal}")
    return "\n".join(output)

# Main async function
async def main(num1, num2, strings):
    # Create tasks
    task_sum = asyncio.create_task(sum_coroutine(num1))
    task_fact = asyncio.create_task(factorial_coroutine(num2))
    task_palindrome = asyncio.create_task(palindrome_coroutine(strings))

    # Wait for all tasks to finish concurrently
    results = await asyncio.gather(task_sum, task_fact, task_palindrome)

    # Print results
    print("\n".join(results))

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    strings = ["madam", "apple", "racecar", "python", "level"]

    asyncio.run(main(num1, num2, strings))
