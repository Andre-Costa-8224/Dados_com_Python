import numpy as np

for c in range(5):
	print(f'{np.random.rand():.2}')
	print(f'{np.random.randn():.2}')
	print(f'{np.random.randint(100)}')
	
print(np.random.randint(5,50,10))

print(np.zeros((5,4)),'\n\n',np.ones((5,4)),'\n\n',np.eye(4))
arr = np.random.randint(1,100, size=(4,4))
print()
print(arr,'\n\n',arr[1:][0,2])