import csv
import numpy as np
import matplotlib.pyplot as plt

alum_path = r'C:\COMP3000\PHYS3000_ENV\MECH2500\Data_Alum_Tension.csv'
brass_path = r'C:\COMP3000\PHYS3000_ENV\MECH2500\Data_Brass_Tension.csv'
steel_path = r'C:\COMP3000\PHYS3000_ENV\MECH2500\Record Lab 5 steel_1.csv'

steel_len = 61545
alum_len = 88
brass_len = 96

data_brass = np.loadtxt(brass_path, 'str', delimiter=',')
for i in range(brass_len):
    for j in range(4):
        h = str.strip(data_brass[i,j], '"')
        data_brass[i,j] = h

data_steel = np.loadtxt(steel_path, 'str', delimiter=',')
for i in range(steel_len):
    for j in range(4):
        h = str.strip(data_steel[i,j], '"')
        data_steel[i,j] = h

data_alum = np.loadtxt(alum_path, 'str', delimiter=',')
for i in range(alum_len):
    for j in range(4):
        h = str.strip(data_alum[i,j], '"')
        data_alum[i,j] = h

area = .35 ** 2 * np.pi * .25

data_steel = data_steel.astype(dtype=float)
data_alum = data_alum.astype(dtype=float)
data_brass = data_brass.astype(dtype=float)

stress_steel = data_steel[:,1] * (1 / area)
strain_steel = data_steel[:,3]
stress_alum = data_alum[:,1] * (1 / area)
strain_alum = data_alum[:,3]
stress_brass = data_brass[:,1] * (1 / area)
strain_brass = data_brass[:,3]

steel_ult = [strain_steel[stress_steel.argmax()],stress_steel.max()]
brass_ult = [strain_brass[stress_brass.argmax()],stress_brass.max()]
alum_ult = [strain_alum[stress_alum.argmax()],stress_alum.max()]

ult_steel_annotation = "The ultimate strength is: " + str("{:.3E}".format(stress_steel.max())) + " psi"
ult_brass_annotation = "The ultimate strength is: " + str("{:.3E}".format(stress_brass.max()))+ " psi"
ult_alum_annotation = "The ultimate strength is: " + str("{:.3E}".format(stress_alum.max())) + " psi"

steel_yield = [strain_steel[10000],stress_steel[10000]]
brass_yield = [strain_brass[41],stress_brass[41]]
alum_yield = [strain_alum[44],stress_alum[44]]

yield_steel_annotation = "The yield strength is: " + str("{:.3E}".format(steel_yield[1])) + " psi"
yield_brass_annotation = "The yield strength is: " + str("{:.3E}".format(brass_yield[1])) + " psi"
yield_alum_annotation = "The yield strength is: " + str("{:.3E}".format(alum_yield[1])) + " psi"

#alum yield 38000 index 44
#brass yield 35000 index 41
#steel yeild 70000 index 100000

mod_elas_steel = "{:.3E}".format(float((stress_steel[8000]-stress_steel[5000]))/float((strain_steel[8000]-strain_steel[5000])))
mod_elas_alum = "{:.3E}".format(float((stress_alum[20]-stress_alum[5]))/float((strain_alum[20]-strain_alum[5])))
mod_elas_brass = "{:.3E}".format(float((stress_brass[32]-stress_brass[10]))/float((strain_brass[32]-strain_brass[10])))

annotation_brass = 'Modulus of Elasticity = ' + mod_elas_brass + ' psi'
annotation_alum = 'Modulus of Elasticity = ' + mod_elas_alum + ' psi'
annotation_steel = 'Modulus of Elasticity = ' + mod_elas_steel + ' psi'

fig,ax = plt.subplots()
fig.suptitle('Steel Tension Test Data Analysis')
ax.plot(strain_steel, stress_steel, label="Steel Stress and Strain data from Instron")
ax.scatter(steel_ult[0], steel_ult[1], s=15, color='red', label='Ultimate Strength')
ax.scatter(steel_yield[0], steel_yield[1], s=15, color='green', label='yield strength')
ax.set_xlabel('Strain (in/in)')
ax.set_ylabel('Stress (psi)')
ax.ticklabel_format(style='plain')
ax.annotate(annotation_steel,xy=(strain_steel[8000],stress_steel[8000]), xytext=(strain_steel[28000],stress_steel[8000]), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate(ult_steel_annotation,xy=steel_ult, xycoords='data',xytext=(1.5, 1.5), textcoords='offset points',label='Ultimate Strength')
ax.annotate(yield_steel_annotation,xy=steel_yield, xycoords='data',xytext=(1.5, 1.5), textcoords='offset points',label='Yield Strength')
ax.legend()

fig2,ax2 = plt.subplots()
fig2.suptitle('Brass Tension Test Data Analysis')
ax2.plot(strain_brass, stress_brass, label="Brass Stress and Strain data from Instron")
ax2.scatter(brass_ult[0], brass_ult[1], s=15, color='red',label='Ultimate Strength')
ax2.scatter(brass_yield[0], brass_yield[1], s=15, color='green',label='Yield Strength')
ax2.set_xlabel('Strain (in/in)')
ax2.set_ylabel('Stress (psi)')
ax2.ticklabel_format(style='plain')
ax2.annotate(annotation_brass,xy=(strain_brass[32],stress_brass[32]), xytext=(strain_brass[60],stress_brass[32]), arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate(ult_brass_annotation,xy=brass_ult, xycoords='data',xytext=(-55.5, 1.5), textcoords='offset points')
ax2.annotate(yield_brass_annotation,xy=brass_yield, xycoords='data',xytext=(1.5, 1.5), textcoords='offset points')
ax2.legend()

fig3,ax3 = plt.subplots()
fig3.suptitle('Aluminum Tension Test Data Analysis')
ax3.plot(strain_alum, stress_alum, label="Aluminum Stress and Strain data from Instron")
ax3.scatter(alum_ult[0], alum_ult[1], s=15, color='red', label='Ultimate Strength')
ax3.scatter(alum_yield[0], alum_yield[1], s=15, color='green', label='Yield Strength')
ax3.set_xlabel('Strain (in/in)')
ax3.set_ylabel('Stress (psi)')
ax3.ticklabel_format(style='plain')
ax3.annotate(annotation_alum,xy=(strain_alum[20],stress_alum[20]), xytext=(strain_alum[52],stress_alum[20]), arrowprops=dict(facecolor='black', shrink=0.05))
ax3.annotate(ult_alum_annotation,xy=alum_ult, xycoords='data',xytext=(-30.5, -15.5), textcoords='offset points')
ax3.annotate(yield_alum_annotation,xy=alum_yield, xycoords='data',xytext=(1.5, 1.5), textcoords='offset points')
ax3.legend()

plt.show()




