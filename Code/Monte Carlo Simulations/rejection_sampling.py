import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu_ps = 30
sigma_ps = 10
mu_ps2 = 80
sigma_ps2 = 20

mu_q = 50
sigma_q = 30

def P_star(x):
    p_x = norm.pdf(x,mu_ps,sigma_ps) + norm.pdf(x,mu_ps2,sigma_ps2)
    return(p_x)

def Q(x):
    q_x = norm.pdf(x,mu_q,sigma_q)
    return(q_x)

def Rejection_Sampling_MixtureNormals(M,c):
    accepted_values = []

    for i in range(M):
        x = np.random.normal(mu_q, sigma_q)
        u = np.random.uniform(0,c * Q(x))

        if u <= P_star(x):
            accepted_values.append(x)

    return(np.array(accepted_values))

x = np.arange(-10,150)
c = max(P_star(x) / Q(x))
X_accepted = Rejection_Sampling_MixtureNormals(M = 100000, c = c)

counts, bins, ignored = plt.hist(
    X_accepted, 
    x, 
    density = True,
    color = 'purple',
    label = 'accepted samples')
plt.title("""Rejection Sampling for Mixture of Normal Distribution with 
          Unif(0,cQ(x))""")
plt.ylabel("Probability")
plt.show()