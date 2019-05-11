a [1,3,5,8,7,9,2]

[i for i in a]

f= lambda x: x*10
[f(i) for i in a]

[(lambda x: x*10) (i) for i in a if i > 5]

