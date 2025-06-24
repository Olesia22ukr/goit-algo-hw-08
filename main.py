import heapq
from typing import List

# Завдання 1: мінімізація витрат на з'єднання кабелів
def min_cost_connect_cables(lengths: List[int]) -> int:
    """
    Об'єднує кабелі за мінімальної вартості.
    Кожне з'єднання коштує суму довжин двох найкоротших.
    Використовує мін-купу (heapq).
    """
    if len(lengths) <= 1:
        return 0

    heapq.heapify(lengths)
    total_cost = 0

    while len(lengths) > 1:
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)
        cost = a + b
        total_cost += cost
        heapq.heappush(lengths, cost)
        print(f"З’єднуємо {a} + {b} = {cost}, загальні витрати = {total_cost}")

    return total_cost

# Додаткове завдання: об'єднання k відсортованих списків
def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків в один за допомогою мін-купи.
    Витягує мінімальний поточний елемент із головного вузла кожного списку.
    """
    heap = []
    result = []

    # Перший елемент кожного списку з інформацією: (value, index списку, позиція)
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        # Якщо є наступний елемент — додаємо його в купу
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result

if __name__ == "__main__":
    # Демонстрація рішення першого завдання
    cables = [4, 3, 2, 6]
    print("Кабелі:", cables)
    cost = min_cost_connect_cables(cables.copy())
    print("Мінімальні загальні витрати:", cost)

    # Демонстрація merge_k_lists
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists)
    print("Відсортований список:", merged)