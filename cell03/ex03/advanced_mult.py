for a in range(12):
    result = [a * b for b  in range(12)]
    print(f"table {a}: {' '.join(map(str, result))}")