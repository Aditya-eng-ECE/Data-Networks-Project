import numpy as np
import matplotlib.pyplot as plt
n = 30
t = 2000
Pi_min =0.02
Pi_max = 0.1
g = np.arange(1000, 10000, 10)
c = 0.8
ri_max=4
ri_min=(c+1)/c
r = np.zeros((n, t+1))
p = np.zeros((n, t+1))
p[:,0]= np.random.uniform(low=Pi_min, high=Pi_max, size=(n,))
Q = np.zeros(t + 1)
H = np.zeros((n, t + 1))
sump=np.zeros((1, t+1))
for i in range(0, t):
for j in range(0, n):
if Q[i] > 0:
p[j][i] = ((H[j][i] / Q[i]) - (1 / g[j]))
if (p[j][i]<=0):
p[j][i]=Pi_min
elif(p[j][i]>Pi_max):
p[j][i]= Pi_max
elif (Q[i] == 0):
p[j][i] = Pi_max
if (H[j][i] <= 0):
r[j][i] = ri_max
elif (H[j][i] > 0):
r[j][i] = ri_min
sump =np.sum(p,axis=0)
pc= np.log(1 + g[j] * p[j][i])
H[j][i + 1] = max(H[j][i] + r[j][i] - np.log(1 + g[j] * p[j][i]), 0)
Q[i + 1] = max(Q[i] + sump[i] - 2.5, 0)
R = np.sum(r, axis=0)
print('Power:', p)
print('Data Rate:', r)
print('Sum Data rate:', R)
print('Queue value of Q:', Q)
print('Queue value of H:', H)
# Plot theoretical values
plt.plot(R, 'rx', label='Sum rate')
# Add axis labels and legend
plt.xlabel('t')
plt.ylabel('Sum rate (in bps)')
plt.legend()
plt.show()
plt.plot(Q, 'rx', label='Q size vs t')
# Add axis labels and legend
plt.xlabel('T')
plt.ylabel('Size of Queue Q')
plt.legend()
plt.show()
plt.plot(H[1], 'rx', label='H size vs t')
plt.xlabel('T')
plt.ylabel('Size of Queue H')
plt.legend()
plt.show()
