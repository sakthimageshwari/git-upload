# bubble sort
arr=[1,4,5,3,10]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]<arr[j+1]:
            continue
        elif arr[j]>arr[j+1]:
            tem=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=tem
print(arr)            