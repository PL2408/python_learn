import sys

tp = (1, 25, 888)  # Ax00098
ls = [1, 25, 888]  # Ax06097

print('Size of Tuple:', sys.getsizeof(tp))
print('Size of List:', sys.getsizeof(ls))

tp = tp + (999,)  # Ax20098

ls[1] = 35
ls[2] = tp[1]

# print("Tuple:", tp)
# print("List:", ls)

# for i in tp:
#     print(i)

# -----------------------
import time

tp = ()
ls = []

rng = 2000

curr_time = time.time()
for i in range(rng):
    ls.append(i)
print("Time for List:", time.time() - curr_time)

curr_time = time.time()
for i in range(rng):
    tp = tp + (i,)
print("Time for List:", time.time() - curr_time)

print('Size of Tuple:', sys.getsizeof(tp))
print('Size of List:', sys.getsizeof(ls))
