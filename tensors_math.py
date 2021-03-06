'''
Presents basic tensor math operations. Adding, multiplication, matrix multiplication etc.

'''
from __future__ import print_function
import torch
import time

x = torch.empty(5, 3)
print(x)


r1, c1 = (150, 50)
r2, c2 = (150, 50)

a = torch.rand(r1, c1)
b = torch.rand(r2, c2)

t1 = time.perf_counter()

c = a*b

t2 = time.perf_counter()
print('cpu time={} result={}'.format(t2-t1, c.sum()))

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    print(device)

    print(torch.cuda.get_device_properties(0))
    a = a.cuda()
    b = b.cuda()
    torch.cuda.synchronize()
    torch.cuda.synchronize()

    t1 = time.perf_counter()

    c = a*b
    torch.cuda.synchronize()
    t2 = time.perf_counter()
    print('gpu time={} result={}'.format(t2-t1, c.sum()))
else:
    print('GPU not enabled')


# batch matrix matrix mulltiplication
import numpy as np

# b1 = torch.zeros(1, 1, 4).fill_(2) # [ [ [2,2,2,2] ] ]
# b2 = torch.zeros(1, 4, 3).fill_(1) # [ [ [1,1,1,1] ] ]

na = np.array([[1000, 100, 10, 1]], dtype=np.float32)
b1 = torch.from_numpy(na)
b1 = b1.unsqueeze(0)  # add 3 dim (batch dim)


na = np.arange(1, 13, dtype=np.float32)
na = na.reshape([4, 3])
b2 = torch.from_numpy(na)
b2 = b2.unsqueeze(0)  # add 3 dim (batch dim)

print(b1, b2)
batch_mul = torch.bmm(b1, b2)
print(batch_mul)

