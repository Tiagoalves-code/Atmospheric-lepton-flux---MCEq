#standard imports
import matplotlib.pyplot as plt

from MCEq.geometry.density_profiles import *
us_obj = CorsikaAtmosphere('BK_USStd', None)
sps_obj = CorsikaAtmosphere('PL_SouthPole', 'January')
spw_obj = CorsikaAtmosphere('PL_SouthPole', 'August')
msps_obj = MSIS00Atmosphere('SouthPole', 'January')
mspw_obj = MSIS00Atmosphere('SouthPole', 'August')
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(111)
# set_theta will trigger integration and cache look-up
us_obj.set_theta(0.0)
sps_obj.set_theta(0.0)
spw_obj.set_theta(0.0)
msps_obj.set_theta(0.0)
mspw_obj.set_theta(0.0)

# obtain the depth value corresponding to the surface from obj.X_surf
x_vec = np.linspace(0, us_obj.max_X, 10000)
plt.plot(x_vec, 1e3 / us_obj.r_X2rho(x_vec),label='US Standard',lw=1.5,color='black')
plt.plot(x_vec, 1e3 / spw_obj.r_X2rho(x_vec),label='CKA, SP/Aug',lw=1.5,color='red')
plt.plot(x_vec, 1e3 / sps_obj.r_X2rho(x_vec),label='CKA, SP/Jan',lw=1.5,color='orange')
plt.plot(x_vec, 1e3 / mspw_obj.r_X2rho(x_vec),label='MSIS00, SP/Aug',lw=1.5,color='cyan')
plt.plot(x_vec, 1e3 / msps_obj.r_X2rho(x_vec),label='MSIS00, SP/Jan',lw=1.5,color='blue')

us_obj.set_theta(70.0)
sps_obj.set_theta(70.0)
spw_obj.set_theta(70.0)
msps_obj.set_theta(70.0)
mspw_obj.set_theta(70.0)
x_vec = np.linspace(0, us_obj.max_X, 10000)
plt.plot(x_vec, 1e3 / us_obj.r_X2rho(x_vec),label='_nolabel_',lw=1.5, ls='--', color='black')
plt.plot(x_vec, 1e3 / spw_obj.r_X2rho(x_vec),label='_nolabel_',lw=1.5, ls='--', color='red')
plt.plot(x_vec, 1e3 / sps_obj.r_X2rho(x_vec),label='_nolabel_',lw=1.5, ls='--', color='green')
plt.plot(x_vec, 1e3 / mspw_obj.r_X2rho(x_vec),label='_nolabel_',lw=1.5, ls='--', color='cyan')
plt.plot(x_vec, 1e3 / msps_obj.r_X2rho(x_vec),label='_nolabel_',lw=1.5, ls='--', color='blue')
plt.xlim([0,4000])
plt.legend(loc='lower right', frameon=False, fontsize=10)

plt.xlabel('Profundidade Inclinada $X$ em [g/cm$^2$]')
plt.ylabel(r'Densidade de Massa $\rho$ em [10$^{-3}$g/cm$^3$]')
plt.tight_layout()

plt.show()
