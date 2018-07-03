import matplotlib.pyplot as plt

#x_values = [1,2,3,4,5]
#y_values = [1,8,27,64,125]
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,s= 10 , c = 'red')

plt.show()
