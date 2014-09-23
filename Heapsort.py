
import math

def _left(i):
	return 2 * i + 1

def _right(i):
	return 2 * i + 2

def max_heapify(A,i,heapsize):
	l = _left(i)
	r = _right(i)
	if l < heapsize and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r < heapsize and A[r] > A[largest]:
		largest = r
	if largest != i:
		tmp = A[i]
		A[i] = A[largest]
		A[largest] = tmp
		max_heapify(A, largest,heapsize)

def build_max_heap(A):
	n = len(A)/2 - 1
	for x in range(n, -1, -1):
		max_heapify(A,x,len(A))


def heapsort(A):
	build_max_heap(A)
	n = len(A)
	size = n
	for i in range(n-1,0,-1):
		tmp = A[0]
		A[0] = A[i]
		A[i] = tmp
		size -= 1
		max_heapify(A,0,size)

A = [4,1,3,2,16,9,10,14,8,7]
heapsort(A)
print A