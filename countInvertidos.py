#Problema Contagem de inversões adptando o mergeSort

#Variavel global para guardar as inversões
invertidos = 0
tamanhoArray = len(arr)

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
    #Invertendo pois queremos de forma decrescente
		while i < len(L) and j < len(R):
			if L[i] > R[j]:
				arr[k] = L[i]
				i += 1
        if (len(L) + len(R) == tamanhoArray):
          invertidos = invertidos + len(R) - j
        else:
          invertidos += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list

def merge(arr):
    mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		L = mergeSort(L)
		R = mergeSort(R)
    
            
