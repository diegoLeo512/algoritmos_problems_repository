

def merge_sort(array: list[int]):
    
    if len(array) == 1:
        return array
    elif len(array) == 2:
        return [array[0],array[1]] if array[0]< array[1] else [array[1],array[0]]
    
    n=int(len(array)/2)
    left = merge_sort(array[:n])
    right = merge_sort(array[n:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    if i < len(left):
        result=result+left[i:]
            
    if j < len(right):
        result=result+right[j:]
    return result
        
        