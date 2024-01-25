# qsort implementation for strings
import random

import graphviz


def test_small_arr():
    arr = [4, 2, 5, 1, 3]
    print('test_small:\n unsorted arr:', arr)
    qsort = QuickSortTester(arr)
    qsort.qsort(0, len(arr) - 1)
    qsort.print()


class QuickSortTester:

    class Stats:

        class MsgContainer:
            calls = []
            def __init__(self, call_info=None):
                self.call_info = call_info

            def add_call(self, call):
                self.calls.append(call)
            def print_call_stack(self):
                for call in self.calls:
                    print(call.entry)

        class CallEntry:
            A = []
            n = 0
            p = 0
            r = 0
            rec_level = 0
            call_n = 0
            alfa = 0.0
            parent_call = 0
            is_calling_qsort = True
            call_id = ''
            msg_format = ''
            entry = ''

            def __init__(self, A, n, p, r, rec_level, call_n, is_calling_qsort, msg_format):
                self.A = A
                self.n = n
                self.p = p
                self.r = r
                self.rec_level = rec_level
                self.call_n = call_n
                self.is_calling_qsort = is_calling_qsort
                self.call_id = 'qsort(%s,%s)' % (p, r)
                self.msg_format = msg_format

                self.entry = ''
                if self.is_calling_qsort:
                    self.entry = self.entry + '>>>'
                else:
                    self.entry = self.entry + '<<<'

                str_format = self.msg_format % (self.p, self.r, self.p, self.r, self.rec_level, str(self.A))
                self.entry = self.entry + ' ' + str_format
            def get_attr_as_log_entry(self):
              return self.entry

        A = []
        p = 0
        q = 0
        rec_level = 0
        call_n = 0
        alfa = 0.0
        msg_container = None


        def __init__(self, A, p, q, rec_level, cal_n):
            self.A = A
            self.p = p
            self.q = q
            self.rec_level = rec_level
            self.cal_n = cal_n
            self.msg_container = self.MsgContainer()

        def set_attr(self, p, q, rec_level, cal_n):
            self.p = p
            self.q = q
            self.rec_level = rec_level
            self.cal_n = cal_n

        def add_stat(self, p, q, rec_level, cal_n):
            self.stats.msg_stack.append('>>> qsort(%s, %s) \n where p = %s r = %s rec_level = %s \n arr: %s' %
                                        (p + 1, r + 1, p + 1, r + 1, self.stats.rec_level, str(self.A)))

            self.stats.set_attr(p, r, self.stats.rec_level + 1, self.stats.cal_n + 1)
            call = self.CallEntry(self.A, )

    A = []
    stats = None

    def insert_stats(self, stat, stat_entry, left_right):
        if stat is None:



    def __init__(self, A):
        self.A = A
        self.stats = self.Stats(1, len(A), 1, 1)

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
        # self.stats.print_stats()

        self.stats.msg_stack.append('>>> qsort(%s, %s) \n where p = %s r = %s rec_level = %s \n arr: %s' %
                                    (p+1, r+1, p+1, r+1, self.stats.rec_level, str(self.A)))

        self.stats.set_attr(p, r, self.stats.rec_level + 1, self.stats.cal_n + 1)
        if p < r:
            q = self.part(p, r)
            self.qsort(p, q - 1)
            self.stats.msg_stack.append('<<< qsort(%s, %s) \n where p = %s r = %s rec_level = %s \n arr: %s' %
                                        (p+1, r+1, p+1, r+1, self.stats.rec_level, str(self.A)))
            self.stats.set_attr(p, q - 1, self.stats.rec_level - 1, self.stats.cal_n)
            self.qsort(q + 1, r)
            self.stats.set_attr(q + 1, r, self.stats.rec_level - 1, self.stats.cal_n)
            self.stats.msg_stack.append('<<< qsort(%s, %s) \n where p = %s r = %s rec_level = %s \n arr: %s' %
                                        (p+1, r+1, p+1, r+1, self.stats.rec_level, str(self.A)))

    def viz_qsort(self, p, r):
        dot = graphviz.Digraph()



    def print(self):
        print('sorted array:', self.A)
        print('call stack:\n')
        for msg in self.stats.msg_stack:
            print(msg, '\n')
