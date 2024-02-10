# Zackary Cleveland PHYS3000

import kinematicEquations as ke

y_max = 30e-2
key = True

while key:
    yn = 'y'
    v0 = input('Specify the initial velocity the toy generates on launch from the ground (m/s)')
    if ke.vertical_delta_y(v0) > y_max:
        print('The toy would bounce too high,' , (ke.vertical_delta_y(v0)*1e2), 'cm please specify a smaller v0')

    elif ke.vertical_delta_y(v0) <= y_max:
        yn = input((v0, 'm/s satisfies the maximum height criteria, would you like to specify another v0? y(es) or n('
                        'o)?'))
    if yn == 'n' or yn == 'N':
        key = False
    elif yn == 'y' or yn == 'Y':
        continue
    else:
        print("Please only specify y or n or a velocity when prompted")
