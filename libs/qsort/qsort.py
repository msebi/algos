# qsort implementation for strings

class QuickSort:
    A = []

    def __init__(self, A):
        self.A = A

    def part(self, p, r):
        x = self.A[r]
        i = p - 1
        for j in range(p, r, 1):
            if self.A[j] <= x:
                i = i + 1
                tmp = self.A[i]
                self.A[i] = self.A[j]
                self.A[j] = tmp
        tmp = self.A[i + 1]
        self.A[i + 1] = self.A[r]
        self.A[r] = tmp
        return i + 1

    def qsort(self, p, r):
        if p < r:
            q = self.part(p, r)
            self.qsort(p, q - 1)
            self.qsort(q + 1, r)

    def print(self):
        print(self.A)
