# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def get_fibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return get_fibonacci(n-1) + get_fibonacci(n-2)

def solution():
  fibonacci_sum = 0
  i = 1
  while fibonacci_sum <= 4000000:
    fib_value = get_fibonacci(i)
    if fib_value %2 != 0:
      fibonacci_sum += fib_value
    i += 1
  return fibonacci_sum

print(solution()) # 4613732
