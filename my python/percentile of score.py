# stat in python 
from scipy import stats
a=[10,20,30,40,50,60,72]
res=stats.percentileofscore(a,25)
print(res)
