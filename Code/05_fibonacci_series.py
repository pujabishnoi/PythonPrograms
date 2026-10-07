def fibonacci_series(n):
    series = []
    a = 0
    b = 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    print(fibonacci_series(10))