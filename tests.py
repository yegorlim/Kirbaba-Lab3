import random
from heap_sort import heapsort


def random_tests(trials=2000, seed=1):
    rnd = random.Random(seed)
    for _ in range(trials):
        n = rnd.randint(1, 25)
        data = [rnd.randint(1, 50) for _ in range(n)]
        assert heapsort(list(data))[0] == sorted(data)
    return trials


def stability_demo():
    data = [(2, "a"), (2, "b"), (1, "c")]
    return heapsort(list(data), key=lambda t: t[0])[0]


def measure(n, trials=30, seed=7):
    rnd = random.Random(seed + n)
    total = 0
    for _ in range(trials):
        data = [rnd.randint(1, 10 ** 6) for _ in range(n)]
        total += heapsort(list(data))[1]
    return {"n": n, "heap_random_c": total / trials,
            "heap_sorted_c": heapsort(list(range(1, n + 1)))[1]}


if __name__ == "__main__":
    print("Перевірок:", random_tests())
    print("Стійкість:", stability_demo())
    for n in (10, 50, 100, 200, 400):
        print(measure(n))
