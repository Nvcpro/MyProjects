def write_array_to_file(fn,a):
    with open(fn,'w') as f:
        for i in a:
            f.write(str(i)+' ')
def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
def selection_sort(a):
    n=len(a)
    for i in range(n):
        mi=i
        for j in range(i+1,n):
            if a[j]<a[mi]:
                mi=j
        a[mi],a[i]=a[i],a[mi]     
def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        while i>0 and a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            i-=1
def binary_search(a,k,l,r):
    mid=(l+r)//2
    if a[mid]==k:
        return mid
    if l>r:
        return -1
    if k>a[mid]:
        return binary_search(a,k,mid+1,r)
    else:
        return binary_search(a,k,l,mid-1)