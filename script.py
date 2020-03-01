#make sure you use this code in Jupyter notebook or it will not work
#each comment block should get its own cell

############## Gets all resources ###################
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./conservation_of_mass_data.csv')
print(data)
######################################################

############## Difference of Masses Graph #############
diffMassData = data['Difference of Masses(g)']
print(diffMassData)

openDiffData = [diffMassData[0], diffMassData[2], diffMassData[4]]
closedDiffData= [diffMassData[1], diffMassData[3], diffMassData[5]]
trailNames = ["","Trial One", "", "Trial Two","", "Trial Three"]

#Open System Graphs
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 3 # Number of sets of bars
w = 0.8 # Width of each bar

open_x = [t*element + w*n for element in range(d)]

f, ax = plt.subplots(1)
ax.set_ylim(bottom=1.2, top=1.8)
ax.set_xticklabels(trailNames)
plt.bar(open_x, openDiffData, color='#0f8ff7')

# Closed System Graphs 
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
w = 0.8 # Width of each bar

closed_x = [t*element + w*n for element in range(d)]

plt.bar(closed_x, closedDiffData, color='#f7aa0f')
plt.legend(["Open", "Closed"])
plt.title("Open VS. Closed Systems: Difference of Mass")
plt.ylabel("Initial and Final Mass Difference(g)")
plt.savefig('massDifference.png')
plt.show()
#######################################################

##### Open System Graph (Initial and Final Mass) ######
initialMassData = data['Initial Mass(g)']
finalMassData = data['Final Mass(g)']

openInitialData = [initialMassData[0], initialMassData[2], initialMassData[4]]
openFinalData = [finalMassData[0], finalMassData[2], finalMassData[4]]
trailNames = ["","Trial One", "", "Trial Two","", "Trial Three"]

#Initial Mass Graphs
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 3 # Number of sets of bars
w = 0.8 # Width of each bar

intial_x = [t*element + w*n for element in range(d)]

f, ax = plt.subplots(1)
ax.set_ylim(bottom=130, top=150)
ax.set_xticklabels(trailNames)
plt.bar(intial_x, openInitialData, color='#0f8ff7')

#Final Mass Graphs
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
w = 0.8 # Width of each bar

final_x = [t*element + w*n for element in range(d)]

plt.bar(final_x, openFinalData, color='#0febf7')
plt.legend(["Inital Mass", "Final Mass"])

plt.title("Open System Initial and Final Masses")
plt.ylabel("Mass(g)")
plt.savefig('openDifference.png')
plt.show()
#######################################################

#### Closed System Graph (Initial and Final Mass) ####
initialMassData = data['Initial Mass(g)']
finalMassData = data['Final Mass(g)']

closedInitialData = [initialMassData[1], initialMassData[3], initialMassData[5]]
closedFinalData = [finalMassData[1], finalMassData[3], finalMassData[5]]
trailNames = ["","Trial One", "", "Trial Two","", "Trial Three"]

#Closed System Graphs
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 3 # Number of sets of bars
w = 0.8 # Width of each bar

intial_x = [t*element + w*n for element in range(d)]

f, ax = plt.subplots(1)
ax.set_ylim(bottom=130, top=152)
ax.set_xticklabels(trailNames)
plt.bar(intial_x, closedInitialData, color='#f7aa0f')

#Closed System Graphs
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
w = 0.8 # Width of each bar

final_x = [t*element + w*n for element in range(d)]

plt.bar(final_x, closedFinalData, color='#f2e58f')
plt.legend(["Inital Mass", "Final Mass"])

plt.title("Closed System Initial and Final Masses")
plt.ylabel("Mass(g)")
plt.savefig('closedDifference.png')
plt.show()
#######################################################