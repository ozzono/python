outer="@"
arr=["f"]
for i in range(len(arr)):
    if "d">arr[i]:
        arr.insert(i+1,outer)
    else:
        arr.insert(0,outer)
print(arr)