import time
import random
import matplotlib.pyplot as plt
from sorting_algs import selection_sort, insertion_sort, shell_sort, merge_sort
from sort_comparisons_count import selection_sort_comparisons, insertion_sort_comparisons, shell_sort_comparisons, merge_sort_comparisons


def count_time_random(sorting_method, comparison_method, power: int):
    time_sum = 0
    comparisons = 0
    for _ in range(5):
        arr = [random.randint(0, 2**power) for _ in range(2**power)]
        start = time.time()
        sorting_method(arr.copy())
        time_sum += time.time() - start
        comparisons += comparison_method(arr.copy())
    return time_sum / 5, comparisons // 5


def random_array_time():
    sorting_times = {"Selection sort": dict(), "Insertion sort": dict(), "Shell sort": dict(), "Merge sort": dict()}
    for i in range(7, 16):
        print(f"random Selection {i}")
        sorting_times["Selection sort"][2**i] = count_time_random(selection_sort, selection_sort_comparisons, i)
        print(f"random Insertion {i}")
        sorting_times["Insertion sort"][2**i] = count_time_random(insertion_sort, insertion_sort_comparisons, i)
        print(f"random Shell {i}")
        sorting_times["Shell sort"][2**i] = count_time_random(shell_sort, shell_sort_comparisons, i)
        print(f"random Merge {i}")
        sorting_times["Merge sort"][2**i] = count_time_random(merge_sort, merge_sort_comparisons, i)

    build_time_graph(sorting_times, "Experiment 1")
    build_comparisons_graph(sorting_times, "Experiment 1")
    return sorting_times


def count_time_sorted_reversed(sorting_method, comparison_method, power: int, reversed = False):
    comparisons = 0
    arr = [x for x in range(2**power)]
    if reversed:
        arr.reverse()
    start = time.time()
    sorting_method(arr.copy())
    sort_time = time.time() - start
    comparisons += comparison_method(arr.copy())
    return sort_time, comparisons


def sorted_array_time():
    sorting_times = {"Selection sort": dict(), "Insertion sort": dict(), "Shell sort": dict(), "Merge sort": dict()}
    for i in range(7, 16):
        print(f"sorted Selection {i}")
        sorting_times["Selection sort"][2**i] = count_time_sorted_reversed(selection_sort, selection_sort_comparisons, i)
        print(f"sorted Insertion {i}")
        sorting_times["Insertion sort"][2**i] = count_time_sorted_reversed(insertion_sort, insertion_sort_comparisons, i)
        print(f"sorted Shell {i}")
        sorting_times["Shell sort"][2**i] = count_time_sorted_reversed(shell_sort, shell_sort_comparisons, i)
        print(f"sorted Merge {i}")
        sorting_times["Merge sort"][2**i] = count_time_sorted_reversed(merge_sort, merge_sort_comparisons, i)


    build_time_graph(sorting_times, "Experiment 2")
    build_comparisons_graph(sorting_times, "Experiment 2")
    return sorting_times


def reversed_array_time():
    sorting_times = {"Selection sort": dict(), "Insertion sort": dict(), "Shell sort": dict(), "Merge sort": dict()}
    for i in range(7, 16):
        print(f"reversed Selection {i}")
        sorting_times["Selection sort"][2**i] = count_time_sorted_reversed(selection_sort, selection_sort_comparisons, i, True)
        print(f"reversed Insertion {i}")
        sorting_times["Insertion sort"][2**i] = count_time_sorted_reversed(insertion_sort, insertion_sort_comparisons, i, True)
        print(f"reversed Shell {i}")
        sorting_times["Shell sort"][2**i] = count_time_sorted_reversed(shell_sort, shell_sort_comparisons, i, True)
        print(f"reversed Merge {i}")
        sorting_times["Merge sort"][2**i] = count_time_sorted_reversed(merge_sort, merge_sort_comparisons, i, True)

    build_time_graph(sorting_times, "Experiment 3")
    build_comparisons_graph(sorting_times, "Experiment 3")
    return sorting_times


def count_time_repeated(sorting_method, comparison_method, power: int):
    time_sum = 0
    comparisons = 0
    for _ in range(3):
        arr = [random.randint(1, 3) for _ in range(2**power)]
        start = time.time()
        sorting_method(arr.copy())
        time_sum += time.time() - start
        comparisons += comparison_method(arr.copy())
    return time_sum / 3, comparisons // 3


def repeated_array_time():
    sorting_times = {"Selection sort": dict(), "Insertion sort": dict(), "Shell sort": dict(), "Merge sort": dict()}
    for i in range(7, 16):
        print(f"repeated Selection {i}")
        sorting_times["Selection sort"][2**i] = count_time_repeated(selection_sort, selection_sort_comparisons, i)
        print(f"repeated Insertion {i}")
        sorting_times["Insertion sort"][2**i] = count_time_repeated(insertion_sort, insertion_sort_comparisons, i)
        print(f"repeated Shell {i}")
        sorting_times["Shell sort"][2**i] = count_time_repeated(shell_sort, shell_sort_comparisons, i)
        print(f"repeated Merge {i}")
        sorting_times["Merge sort"][2**i] = count_time_repeated(merge_sort, merge_sort_comparisons, i)

    build_time_graph(sorting_times, "Experiment 4")
    build_comparisons_graph(sorting_times, "Experiment 4")
    return sorting_times


def build_time_graph(sorting_times, experiment):
    for sort_method in ["Selection sort", "Insertion sort", "Shell sort", "Merge sort"]:
        x = list(sorting_times[sort_method].keys())
        y = [sorting_times[sort_method][key][0] for key in x]

        plt.plot(x, y, label = sort_method)

    plt.yscale("log")
    plt.xlabel("Array length")
    plt.ylabel("Time")
    plt.title(f"{experiment} - time")
    plt.legend()
    plt.show()


def build_comparisons_graph(sorting_times, experiment):
    for sort_method in ["Selection sort", "Insertion sort", "Shell sort", "Merge sort"]:
        x = list(sorting_times[sort_method].keys())
        y = [sorting_times[sort_method][key][1] for key in x]

        plt.plot(x, y, label = sort_method)

    plt.yscale("log")
    plt.xlabel("Array length")
    plt.ylabel("Comparisons")
    plt.title(f"{experiment} - comparisons")
    plt.legend()
    plt.show()



def main():
    print(random_array_time())
    print(sorted_array_time())
    print(reversed_array_time())
    print(repeated_array_time())


if __name__ == "__main__":
    main()
