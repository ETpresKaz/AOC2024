with open('Day_2.txt') as f:
    num_arr = f.read()


def is_safe(elem):
    increasing = all(elem[i] < elem[i + 1] for i in range(len(elem) - 1))
    decreasing = all(elem[i] > elem[i + 1] for i in range(len(elem) - 1))

    if not increasing and not decreasing:
        return False

    for i in range(len(elem) - 1):
        diff = abs(elem[i] - elem[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


def process_input(num_arr):
    data = [list(map(int, line.split())) for line in num_arr.splitlines()]
    safe = sum(1 for elem in data if is_safe(elem))

    return safe




safe = process_input(num_arr)
print(safe)


def process_with_missing_numbers(num_arr):
    data = [list(map(int, line.split())) for line in num_arr.splitlines()]
    safe_count = 0

    for elem in data:
        for i in range(len(elem)):
            modified_elem = elem[:i] + elem[i+1:]
            if is_safe(modified_elem):
                safe_count += 1
                break

    return safe_count


safe_with_missing = process_with_missing_numbers(num_arr)
print(safe_with_missing)