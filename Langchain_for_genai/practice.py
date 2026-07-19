arr=[{"name":"rajesh","age":29},{"name":"rahul","age":21},{"name":"prashant","age":30}]
ls=sorted(list(arr),key=lambda x:x['age'])
ms=list(map(lambda x:{"name":x['name'],"age":x['age']*10},arr))
fl=list(filter(lambda x:x['age'] != 29,arr))
st="wcncnioiommncleooi"
result={ch:st.count(ch) for ch in st}
print(result)
print(fl)
print(ms)
print(ls)
for res in arr:
    print(res["name"])
    
s=set([1,2,3,4])
print(s)
