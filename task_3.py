import csv
import random
import timeit


def insertion_sort(data):
    """
    Сортування вставками.
    Складність у середньому та найгіршому
    випадку: O(n^2).
    """
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while (
            j >= 0
            and arr[j] > key
        ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge(left, right):
    """
    Злиття двох відсортованих списків.
    """
    result = []

    i = 0
    j = 0

    while (
        i < len(left)
        and j < len(right)
    ):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(data):
    """
    Рекурсивне сортування злиттям.
    Складність: O(n log n).
    """
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2

    left = merge_sort(
        data[:middle]
    )

    right = merge_sort(
        data[middle:]
    )

    return merge(
        left,
        right
    )


def timsort(data):
    """
    Вбудоване сортування Python.
    Python використовує Timsort.
    """
    return sorted(data)


def create_nearly_sorted(size):
    """
    Створює майже відсортований список.
    """
    data = list(range(size))

    swaps = max(
        1,
        size // 100
    )

    for _ in range(swaps):
        i = random.randrange(size)
        j = random.randrange(size)

        data[i], data[j] = (
            data[j],
            data[i]
        )

    return data


def create_datasets(size):
    """
    Створює різні типи наборів даних.
    """
    random_data = [
        random.randint(
            0,
            size * 10
        )
        for _ in range(size)
    ]

    sorted_data = list(
        range(size)
    )

    reversed_data = list(
        range(
            size,
            0,
            -1
        )
    )

    nearly_sorted = create_nearly_sorted(
        size
    )

    return {
        "random": random_data,
        "sorted": sorted_data,
        "reversed": reversed_data,
        "nearly_sorted": nearly_sorted
    }


def measure_time(
    sorting_function,
    data,
    repeats=3
):
    """
    Вимірює середній час роботи алгоритму.
    """
    total_time = timeit.timeit(
        lambda: sorting_function(data),
        number=repeats
    )

    return total_time / repeats


def save_results(results):
    """
    Зберігає результати у CSV-файл.
    """
    with open(
        "sorting_results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "size",
            "dataset",
            "algorithm",
            "time_seconds"
        ])

        for row in results:
            writer.writerow(row)


def main():
    random.seed(42)

    sizes = [
        1000,
        3000,
        5000
    ]

    algorithms = {
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Timsort": timsort
    }

    results = []

    print(
        "Порівняння алгоритмів сортування"
    )

    print(
        "=" * 70
    )

    for size in sizes:

        datasets = create_datasets(
            size
        )

        print(
            f"\nРозмір масиву: {size}"
        )

        for dataset_name, data in datasets.items():

            print(
                f"\nТип даних: "
                f"{dataset_name}"
            )

            for algorithm_name, function in algorithms.items():

                execution_time = measure_time(
                    function,
                    data
                )

                results.append([
                    size,
                    dataset_name,
                    algorithm_name,
                    execution_time
                ])

                print(
                    f"{algorithm_name:16} "
                    f"{execution_time:.6f} с"
                )

    save_results(results)

    print(
        "\nРезультати збережено "
        "у sorting_results.csv"
    )

    print(
        "\nВисновок:"
    )

    print(
        "Insertion sort добре працює "
        "на невеликих або майже "
        "відсортованих масивах, але "
        "значно сповільнюється зі "
        "збільшенням розміру випадкових "
        "і зворотно відсортованих даних."
    )

    print(
        "Merge sort демонструє більш "
        "стабільну продуктивність завдяки "
        "складності O(n log n)."
    )

    print(
        "Timsort зазвичай показує "
        "найкращі результати, особливо "
        "на вже відсортованих та майже "
        "відсортованих даних."
    )


if __name__ == "__main__":
    main()