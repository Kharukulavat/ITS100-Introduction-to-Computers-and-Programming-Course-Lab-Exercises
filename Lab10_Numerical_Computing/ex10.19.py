import numpy as np

data = np.loadtxt('sales.tsv', delimiter='\t', dtype=float)
#print(data.shape) to check the shape of our data
branch = data[:,0]

#remove the branch number
Sales = data[:,1:] #Removed the first column

#sum sale amount per branch
sum_perbranch = np.sum(Sales, axis = 1) #sum every column in the same row
for i in range(data.shape[0]): #data.shape[0] = the number of rows of 'data'
  print("Branch%d --> %.2f"%(data[i,0],sum_perbranch[i]))
#data[i,0] >> each branch

print()

#sum sale amount per product
products = ['A','B','C']
sum_perproduct = np.sum(Sales, axis = 0) #sum every row in the same column
for i in range(Sales.shape[1]): #data.shape[1] = the number of columns of 'data'
  print("product %s --> %.2f"%(products[i],sum_perproduct[i]))


#Find the branch number with the highest sale amount
sorted_sum_perbranch = np.sort(sum_perbranch)
print("The highest sale amount = %.2f"%(sorted_sum_perbranch[-1]))

argsorted_sum_perbranch = np.argsort(sum_perbranch) #get the index of sum per branch, which is index of branch
print("The branch with the highest sale amount = %d"%data[argsorted_sum_perbranch[-1],0]) #The highest amount is the last index of sorted sum per branch and get the branch from column 0 in that highest amount row