import torch
from small_unittest_for_torch import MyTorchTest

##################
# how to initialize
x = torch.tensor([5.5, 3])
print(x)
y = x.new_ones((2, 2, 2, 2))
print(y)
z = x.new_ones(5, 3, dtype=torch.float32)
print(z)
a = torch.randn_like(z, dtype=torch.float)
print(a)

##################
# operators
####
# checking all shapes of add

res1 = a + z
res2 = torch.add(a, z)
res3 = torch.empty(5, 3)
torch.add(a, z, out=res3)
a.add_(z)
m = MyTorchTest()
m.tensorAssertEqual(a, res1)
m.tensorAssertEqual(a, res2)
m.tensorAssertEqual(a, res3)

####
# checking shape and in-place operands
old_shape = z.size()
z_t = z.t()
m.tensorAssertShape(z, old_shape)

z.t_()
m.tensorAssertShape(z, z_t.shape)

####
# resize
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
m.tensorAssertShape(x, (4, 4))
m.tensorAssertShape(y, (16,))
m.tensorAssertShape(z, (2, 8))

##################
# numpy bridge
b = a.numpy()
c = torch.from_numpy(b)
m.tensorAssertEqual(a, c)
a.add_(1)
m.tensorAssertEqual(a, c)
# it shows that there is always a shallow copy on numpy bridges

##################
# pytorch and matplot differences
# pytorch expects color channels to be first dimension of tensor. but matplot expects it to
#   be the last one (or not being displayed at all)

##################
# parameters of model
# assume a model which inherits nn.module class. model.parameter shows all parameters that
#   model has got (weights, biases, etc)  # noqa

##################
#
