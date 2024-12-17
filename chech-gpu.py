import torch
print(torch.backends.mps.is_available(), torch.backends.mps.is_built())

import tensorflow as tf
print(tf.config.list_physical_devices("GPU"))