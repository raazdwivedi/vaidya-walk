import numpy as np
import pwalk

print dir(pwalk)

d = 2

A1 = np.eye(d)
A2 = -np.eye(d)
b1 = np.ones(d) * 1.
b2 = np.zeros(d) + 1

A = np.concatenate((A1, A2), axis=0)
b = np.concatenate((b1, b2), axis=0)
r = 0.5
nb_samples = 10

initialization = np.zeros(d)


dikinSamples = pwalk.generateDikinWalkSamples(initialization, A, b, r, nb_samples)

print dikinSamples

vaidyaSamples = pwalk.generateVaidyaWalkSamples(initialization, A, b, r, nb_samples)

print vaidyaSamples

johnSamples = pwalk.generateJohnWalkSamples(initialization, A, b, r, nb_samples)

print johnSamples
