# Zackary Cleveland PHYS3000
# Attempted proficiencies: P1.e-g
import chargePlotter as plt
import netForcesChargeSystem as nfcs

# Run nfcs.simulate_coulombs_law('PATH') Ex: nfcs.simulate_coulombs_law('C:/Users/Zackary Cleveland/OneDrive -
# Wentworth Institute of Technology/2024 Spring/progressReport2/read_files/charge_list2.txt')

PATH = r'C:\Users\Zack\PycharmProjects\PHYS3000_Portfoio\Charges Txt Prompt\charge_list.txt'

nfcs.simulate_coulombs_law(PATH)
plt.init_plot(PATH)