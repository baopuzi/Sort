# 冒泡排序
def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
# 选择排序
def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

# 快速排序
def quick_sort(arr):
    if arr==[]:
        return []
    else:
        first=[arr[0]]
        left=quick_sort([x for x in arr[1:] if x<=arr[0]])
        right=quick_sort([y for y in arr[1:] if y>arr[0]])
    return left+first+right
    
# 插入排序
def insert_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr 
    
if __name__=="__main__":
    list=[1,3,9,10,2,1,3,5,4,2]
    print('排序前结果为：',end='')
    for i in list:
        print(i,end=' ')
    print('\n排序后结果为：',end='')
    
    #测试各种排序方法
    for i in (bubble_sort(list)):
        print(i,end=' ')

  
