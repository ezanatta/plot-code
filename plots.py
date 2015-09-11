import numpy as np
import pylab


#photometric parameters (fitted by galfit)
bn = 7.67   #constant of the sersic profile
n = 4.0   #sersic index
re = 12.8952 #effective radius (pix)
rs1 = 30.1882    #disk scale lenght (exp1)  (pix)
rs2 = 13.6473    #disk scale lenght (exp2)  (pix)
Se =  9.8046  #surface brightness at effective radius   (mag/arcmin2)
So = 7.4003  #surface brightness at center of fitting region (first exp disk)  (mag/arcmin2)
So2 = 7.9018   #surface brightness at center of fitting region (second exp disk) (mag/arcmin2)

#reading the ellipse fit data stored in an ASCII file
rad2 = np.loadtxt('model.dat', usecols=(1,))
rr = np.loadtxt('model.dat', usecols=(2,))
#calculating the log of quantities and correcting the ellipse fit to match the curve of the profiles
rr = np.log(rr)
rr = ((rr)/(2.0))
rad2 = rad2/60
lograd2 = np.log(rad2)
nr = rad2.size


comp = np.linspace(0,0,nr)       #complete profile used in GALFIT
srsc = np.linspace(0,0,nr)       #sersic profile (with n set below)
exp1 = np.linspace(0,0,nr)       #exponential profile 1
exp2 = np.linspace(0,0,nr)       #exponential profile 2

#calculating intensities
for i in range(0, nr):
    comp[i] = Se*np.exp(-bn*((rad2[i]/(re/60))**1/4)-1)+So*np.exp(-rad2[i]/(rs1/60))+So2*np.exp(-rad2[i]/(rs2/60))   
    srsc[i] = Se*np.exp(-bn*((rad2[i]/(re/60))**1/4)-1)
    exp1[i] = So*np.exp(-rad2[i]/(rs1/60))
    exp2[i] = So2*np.exp(-rad2[i]/(rs2/60))
#calculating the log of everything

logcomp = np.log(comp)
logsrsc = np.log(srsc)
logexp1 = np.log(exp1)
logexp2 = np.log(exp2)
#plots
pylab.plot(lograd2, rr, marker='D', linestyle='None', markersize=2, label="Ellipse Fit")
pylab.plot(lograd2, logcomp, label= "complete profile", color='red')
pylab.plot(lograd2, logsrsc, label = "sersic profile", color='green')
pylab.plot(lograd2, logexp1, label = "exponential profile 1", color='b')
pylab.plot(lograd2, logexp2, label = "exponential profile 2", color='m')
pylab.autoscale(enable=True, axis='both',tight=False)
pylab.legend(loc='lower left')
pylab.ylabel('log(S(r)) (mag/arcmin^2)')
pylab.xlabel('log(r) (arcmin)')
pylab.show()
pylab.savefig('model_VS_ellipse.png')
