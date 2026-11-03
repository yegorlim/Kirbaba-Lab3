def _quiet(*args):
    pass


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return 3


def _identity(x):
    return x


def sink(arr, i, n, say=_quiet, indent="", kf=_identity):
    comparisons = 0
    assignments = 0
    k = i
    assignments += 1
    while True:
        j = 2 * k + 1
        assignments += 1
        comparisons += 1
        if j >= n:
            break
        if j + 1 < n:
            comparisons += 1
            if kf(arr[j + 1]) > kf(arr[j]):
                j += 1
                assignments += 1
        comparisons += 1
        if kf(arr[k]) >= kf(arr[j]):
            say(
                f"{indent}{arr[k]} >= {arr[j]}: "
                "на своєму місці"
            )
            break
        say(
            f"{indent}обмін {arr[k]}[{k}] "
            f"і {arr[j]}[{j}]"
        )
        assignments += swap(arr, k, j)
        k = j
        assignments += 1
    return comparisons, assignments


def heapsort(arr, verbose=False, key=None):
    n = len(arr)
    kf = key if key is not None else _identity
    say = print if verbose else _quiet
    comparisons = 0
    assignments = 0
    say("--- Фаза 1: побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        say(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        c, a = sink(arr, i, n, say, kf=kf)
        comparisons += c
        assignments += a
        say(f"Масив після занурення: {arr}")
    say("--- Фаза 2: сортування ---")
    for i in range(n - 1, 0, -1):
        say(
            f"Міняємо корінь {arr[0]} "
            f"і елемент [{i}] = {arr[i]}"
        )
        assignments += swap(arr, 0, i)
        c, a = sink(arr, 0, i, say, kf=kf)
        comparisons += c
        assignments += a
        say(f"Масив після кроку: {arr}")
    return arr, comparisons, assignments


if __name__ == "__main__":
    data = [69, 52, 97, 27, 10, 88, 29, 1, 24]
    print("Початковий масив:", data)
    s, c, a = heapsort(list(data), verbose=True)
    print("Відсортований список:", s)
    print("Кількість порівнянь:", c)
    print("Кількість присвоювань:", a)
