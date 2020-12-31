import numpy as np;

layer_sizes = (2,3,2);
weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:], layer_sizes[:-1])]
print(weight_shapes);
