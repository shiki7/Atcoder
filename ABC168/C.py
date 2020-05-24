from math import pi, cos
A, B, H, M = map(int, input().split())
theta = abs(30*H + M/2 - 6*M) * pi/180
print((A**2+B**2-2*A*B*cos(theta))**(1/2))
