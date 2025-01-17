result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), int(value))
        result.append(res)
    except Exception as e:
        print(f"Помилка: {type(e).__name__}: {e} для ключа {key}")

print("Результат:", result)
