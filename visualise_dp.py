from process_dp import show_mat
from dynamic_programming import dp_func, dna_needle_man, dna_water_man


A = input("Enter first sequence A: ")
B = input("Enter second sequence B: ")
algo = int(input("Enter algorithm number:\n1. Needleman Wunsch\n2. Smith Waterman\n"))
type = int(input("Enter Sequence Type:\n1. DNA\n2. Protein\n"))
print()
func = dna_needle_man
title = "Needleman Wunsch DNA Alignment Matrix"
if type == 1:
    if algo == 1:
        pass

    elif algo == 2:
        func = dna_water_man
        title = "Smith Waterman DNA Alignment Matrix"

elif type == 2:
    if algo == 1:
        pass
    elif algo == 2:
        pass

mat, maxi = dp_func(A, B, func)
show_mat(mat, A, B, title)
print(maxi)


# TEST CASE
# CAGGTAGTG
# CTAGTAG
# 1
# 1
