import numpy as np

A, B, H, M = map(int, input().split())
H_kakudo = (H * 60 + M) / (12 * 60) * np.pi * 2
M_kakudo = M / 60 * 2 * np.pi
HM_kakudo = abs(H_kakudo - M_kakudo)
ans = A**2 + B**2 - 2*(A*B*np.cos(HM_kakudo))
print(np.sqrt(ans))