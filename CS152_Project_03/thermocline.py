'''
Jordan Smith
09/22/21
CS 152
This program will compute the thermocline of
Great Pond in July 2019
'''

def density(temps):
    '''
    (list) -> (float)
    returns density of water
    '''
    density_values = []
    for temp in temps:
        rho = 1000 * (1 - (temp + 288.9414) * (temp - 3.9863)**2 / (508929.2*(temp + 68.12963)))
        density_values.append(rho)
    return(density_values)

def thermocline_depth(temps, depths):
    '''
    (list,list) -> (float)
    returns thermocline depth of water
    '''
    rhos = density(temps)
    drho_dz = []
    for i in range(len(rhos)-1):
        drho_dz.append((rhos[i+1] - rhos[i]) / (depths[i+1] - depths[i]))
        #print(i)
        #print("temps: " + str(temps[i]))
        #print("rhos: " + str(rhos[i]))
        #print("derivatives: " + str(drho_dz[i]))
    max_drho_dz = -1.0
    maxindex = -1
    for i in range(len(drho_dz)):
        if(drho_dz[i] > max_drho_dz):
            max_drho_dz = drho_dz[i]
            maxindex = i
            thermoDepth = ((depths[maxindex] + depths[maxindex+1]) / 2)
    
    return(thermoDepth)

def main():
    '''
    No parameters
    Prints out the day of the month and the corresponding thermocline depth
    '''
    fields = [10,11,16,17,15,14,13,12]
    depths = [1,3,5,7,9,11,13,15]

    fp = open("Goldie2019July.csv","r")
    line = fp.readline()
    day = 0
    for line in fp:
        words = line.split(",")
        if("12:03" in words[0]):
            day += 1
    
            temps = []
            for i in range(len(depths)):
                temps.append(float(words[fields[i]]))

            thermo_depth = thermocline_depth(temps,depths)
            print(str(day) + ", " + str(thermo_depth))
            
    return

if __name__ == "__main__":
	main()

