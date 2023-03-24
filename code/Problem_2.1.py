#--------------------------------------------------Importing the required libraries-------------------------------------------------
from matplotlib.pyplot import *

#------------------------------------------------------Defining the variables-------------------------------------------------------
t = 31.84                                                                    #Shortest Time
Ψ = 35                                                                       #Rotation about x axis
Θ = 15                                                                       #Rotation about y axis
Φ = 20                                                                       #Rotation about z axis    
ωx = [1]*33                                                                  #Angular speed about x direction
ωx[0] = 0
ωy = [0.641]*33                                                              #Angular speed about y direction
ωy[0] = 0
ωz = [0.4614]*33                                                             #Angular speed about z direction
ωz[0] = 0

Ψ_instantaneous = [0]                                                        #To keep track of Ψ at the instance of time
Θ_instantaneous = [0]                                                        #To keep track of Θ at the instance of time
Φ_instantaneous = [0]                                                        #To keep track of Φ at the instance of time

#-------------------------------------------Loop to iterate angles at every instance of time----------------------------------------
for a in range(int(t)):
    Ψ_instantaneous.append(Ψ_instantaneous[-1] + Ψ/t)
    Θ_instantaneous.append(Θ_instantaneous[-1] + Θ/t)
    Φ_instantaneous.append(Φ_instantaneous[-1] + Φ/t)

Ψ_instantaneous.append(Ψ)
Θ_instantaneous.append(Θ)
Φ_instantaneous.append(Φ)

time = [i for i in range(int(t)+1)]
time.append(t)

#-----------------------------------------------------------Plotting the graphs------------------------------------------------------
#======== Ψ vs Time Plot ==========
plot(time, Ψ_instantaneous)
title('Ψ vs Time Plot')
xlabel('Time')
ylabel('Ψ')
xlim(0,t+1)
ylim(0,Ψ+1)
show()

#========== Θ vs Time Plot =========
plot(time, Θ_instantaneous)
title('Θ vs Time Plot')
xlabel('Time')
ylabel('Θ')
xlim(0,t+1)
ylim(0,Θ+1)
show()

#======== Φ vs Time Plot ===========
plot(time, Φ_instantaneous)
title('Φ vs Time Plot')
xlabel('Time')
ylabel('Φ')
xlim(0,t+1)
ylim(0,Φ+1)
show()

time[1] = 0                                                                 #Assuming the infinite acceleration, for the 0th second, omega will be at it's increased value.

#======== ωx vs Time Plot =========== 
plot(time, ωx)
title('ωx vs Time Plot')
xlabel('Time')
ylabel('ωx')
show()

#======== ωy vs Time Plot ===========
plot(time, ωy)
title('ωy vs Time Plot')
xlabel('Time')
ylabel('ωy')
show()

#======== ωz vs Time Plot ===========
plot(time, ωz)
title('ωz vs Time Plot')
xlabel('Time')
ylabel('ωz')
show()