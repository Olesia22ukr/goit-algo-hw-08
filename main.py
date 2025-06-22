import heapq

def merge_k_lists(lists):
    min_heap = []
    for i, sorted_list in enumerate(lists):
        for num in sorted_list:
            heapq.heappush(min_heap, num)
    merged_list = [heapq.heappop(min_heap) for _ in range(len(min_heap))]
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)