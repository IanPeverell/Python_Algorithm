def QuickSort(L):
    if len(L)<=1 :
        return L
    return QuickSort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + QuickSort([ge for ge in L[1:] if ge >= L[0]])
