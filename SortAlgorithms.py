class SortAlgorithms:

    def selection_sort(self, ls):
        """
        완성된듯?
        :param ls: list to sort
        :return: sorted list with selection sort
        """
        count = 0
        min_selected = 0
        print(ls)
        for i in range(len(ls)):
            min_selected = i
            for j in range(i + 1, len(ls)):
                count += 1
                print('what you looking at? ', ls[min_selected], ls[j])
                print('min is ? ', min_selected)
                if ls[min_selected] > ls[j]:
                    min_selected = j
            ls[i], ls[min_selected] = ls[min_selected], ls[i]
        print(count, '회 비교')
        print(ls)
        return ls

    def bubble_sort(self, ls):
        print(ls)
        count = 0
        for i in range(len(ls) - 1, 0, -1):
            for j in range(i):
                if i == j:
                    continue
                count += 1
                print('what you looking at? ', ls[j], ls[j + 1])
                if ls[j] > ls[j + 1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
        print(count, '회 비교')
        print(ls)
        return ls

    def insertion_sort(self, ls):
        print(ls)
        count = 0
        for i in range(1, len(ls)):
            for j in range(i, 0, -1):
                count += 1
                print('what you looking at? ', ls[j], ls[j - 1])
                if ls[j] < ls[j - 1]:
                    ls[j], ls[j - 1] = ls[j - 1], ls[j]
        print(count, '회 비교')
        print(ls)
        return ls

    def merge_sort(self, ls):
        """
        복습할것
        """

        def merge_sort_recursive(left, right):

            if right - left < 2:
                return

            mid = (right + left) // 2
            merge_sort_recursive(left, mid)
            merge_sort_recursive(mid, right)
            merge(left, mid, right)

            return ls

        def merge(left, mid, right):
            tp = []
            low, top = left, mid
            print("before sort ls", ls)
            while low < mid and top < right:
                if ls[low] < ls[top]:
                    tp.append(ls[low])
                    low += 1
                else:
                    tp.append(ls[top])
                    top += 1

            while low < mid:
                tp.append(ls[low])
                low += 1
            while top < right:
                tp.append(ls[top])
                top += 1
            for i in range(left, right):
                ls[i] = tp[i - left]
            print("index of left, mid, right:", left, mid, right)
            print("temp ls", tp)
            print("real ls", ls)
            print("-=-=-=-=-=-=-")

        return merge_sort_recursive(0, len(ls))

    def quick_sort(self, ls):
        """
        아무리봐도 복습필요
        """

        def sort(left, right):
            print('기준 리스트', ls)
            print('재귀 시작 :', left, right)
            if right <= left:
                return
            mid = partition(left, right)
            sort(left, mid - 1)
            sort(mid, right)
            return ls

        def partition(left, right):
            print('-=-=-=-=-start=-=-=-=-=-=')
            pivot = (left + right) // 2
            while left <= right:
                print('피벗 :', pivot, ',피벗 인덱스 :', ls[pivot])
                print('최소 :', left, ', 최대 :', right)
                print('최소인덱스 :', ls[left], ', 최대인덱스 :', ls[right])
                while ls[left] < ls[pivot]:
                    left += 1
                while ls[right] > ls[pivot]:
                    right -= 1
                if left <= right:
                    ls[left], ls[right] = ls[right], ls[left]
                    left, right = left + 1, right - 1
                    print('-=- break전 변환값 :', left, right)

            print(left)
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print()
            return left

        return sort(0, len(ls) - 1)

    def heap_sort(self, lists):

        def heapify(ls, index, HEAP_SIZE):
            largest = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < HEAP_SIZE and ls[left_index] > ls[largest]:
                largest = left_index
            if right_index < HEAP_SIZE and ls[right_index] > ls[largest]:
                largest = right_index
            if largest != index:
                ls[largest], ls[index] = ls[index], ls[largest]
                print("h")
                heapify(ls, largest, index)

        def sort(ls):
            for i in range(len(ls)):
                heapify(ls, i, len(ls))
            print(ls)
            for i in range(len(ls) - 1, 0, -1):
                ls[0], ls[i] = ls[i], ls[0]
                heapify(ls, 0, i)
            return ls

        return sort(lists)

    def counting_sort(self, arr):
        counts = [0] * (max(arr) + 1)
        result = [0] * len(arr)

        for num in arr:
            counts[num] += 1
        for num in range(1, len(counts)):
            counts[num] += counts[num - 1]
        for num in arr:
            index = counts[num]
            result[index - 1] = num
            counts[num] -= 1
        return result

    def examples(self):
        ls = [3, 2, 4, 6, 12, 15, 17, 456, 5678956, 345, 232457, 285, 243, 34572, 45, 1327345, 7, 234634, 72346, 3457, ]
        ls1 = [10, 5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
        self.counting_sort(ls1)
        return self.quick_sort(ls)


a = SortAlgorithms()
b = a.examples()
print(b)
