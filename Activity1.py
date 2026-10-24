import matplotlib.pyplot as plt

bsl_men=[88,90,129,122,100,150,113,135,80,130,111,85,92]
bsl_women=[99,96,87,123,143,150,149,88,91,99,101,118,134]

t=[bsl_men,bsl_women]
color=['b','r']
label=['men','women']
bins=[80,100,125,150]
plt.xlabel('Total no. of Patients')
plt.ylabel('Blood Sugar Level')
plt.hist(t,bins=bins,color=color,label=label,orientation='horizontal')
plt.title('Blood Sugar Levels')
plt.legend()
plt.grid(True)
plt.show()