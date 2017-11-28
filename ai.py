

import numpy as np 
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable
 
#Creating the architecture of the neural network

class Network(nn.module):#inheriting from the parent module class of nn.module
    
    def __init__(self, input_size, nb_action):#inputsize=input neurons, nb_action=output neurons
        super(Network, self).__init__()
        self.input_size = input_size
        self.nb_action = nb_action
        self.fc1 = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30, nb_action)