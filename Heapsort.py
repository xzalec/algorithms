
import math

def _left(i):
	return 2 * i + 1

def _right(i):
	return 2 * i + 2

def _compare(a,b):
	return a > b

def print_tree(A):
	height = int(math.log(len(A), 2)) + 1
	size = 1
	for x in range(0,height):
		for i in range(0, size):
			n = 2**x + i - 1
			if n < len(A):
				print A[n],
				print '   ',
		print ''
		size *=2


def max_heapify(A,i,heapsize):
	l = _left(i)
	r = _right(i)

	if l < heapsize and _compare(A[l], A[i]):
		largest = l
	else:
		largest = i
	if r < heapsize and _compare(A[r], A[largest]):
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

def reverse(A):
	size = len(A)
	for i in range(0, size/2):
		tmp = A[i]
		A[i] = A[size - 1 - i]
		A[size - 1 - i] = tmp

if __name__ == '__main__':
	A = [4,1,3,2,16,9,10,14,8,7]
	heapsort(A)
	print A
	reverse(A)
	print A


	B = [45,3,645,23,7,45,123,4342,787,5,90]
	heapsort(B)
	print B

	C = [32,3432,56437,78,5341,675,2434,897,4,675,234,65,23,564,213,546,234,546,23,56,2341,564,44,5,45,3,4,5,656,234,34,564]
	heapsort(C)
	print C
