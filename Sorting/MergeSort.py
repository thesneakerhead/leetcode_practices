def mergeSort(arr):
    if len (arr) > 1:

        mid = len(arr)//2
        print("mid:",mid)
        L = arr[:mid]
        R = arr[mid:]
        print (L)
        print (R)
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        #merge step
        print(L)
        print(R)
        #1.) Copy smallest element to first element of sub array arr[]
        print(arr)
        while i < len(L) and j < len(R):
            if L[i] < R[j]: 
                arr[k] = L[i]   
                i += 1        
            else:
                arr[k] = R[j]   
                j += 1
            
            print(arr,'in')
            k += 1
            print("i:",i,"j:",j,"k:",k)

        #2.) Copy remaining elements of L[] or R[] to arr[]
        while i < len(L):
            arr[k]=L[i]
            i += 1
            k += 1
            print(arr,"mid")
        
        while j < len(R):
            arr[k]=R[j]
            j += 1
            k += 1
            print(arr,"mid2")

        print(arr,"out")

arr = [12, 13, 11, 5, 6, 7]
mergeSort(arr)
print(arr)