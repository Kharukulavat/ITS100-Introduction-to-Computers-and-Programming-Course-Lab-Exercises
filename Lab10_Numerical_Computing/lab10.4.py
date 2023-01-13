#ITS100 Lecture10 Numerical Computing Lab10.4
import numpy as np
data = np.loadtxt('sales.tsv', delimiter='\t', dtype=float)
branch = data[:,0] #Every row in the first column is branch
sale = data[:,1:] #Every row and every colmun except the first column are sales
sumsale = np.sum(sale, axis = 1) #axis 1 ; sum every column in the same row
sorted_ss = np.sort(sumsale) 
argsort_ss = np.argsort(sumsale) #index of sorted sumsale

for i in range(data.shape[0]): #shape[0] is to count the rows
  # shape[1] is to count the columns
  print("Branch %d --> %.2f"%(branch[argsort_ss[-1-i]],sorted_ss[-1-i]))
#branch[argsort_ss[-1-i]] we want to sort by the highest to lowest so we use argsort with the negative index to sort ; then we -i to order from back to front

#sorted_ss[-1-i] use the same method as sorting branch