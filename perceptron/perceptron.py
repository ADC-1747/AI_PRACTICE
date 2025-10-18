print("This is perceptron.py")

import numpy as np

class Perceptron():
    def __init__(self,weights=np.array([]),bias=0,threshold=0):
        self.weights = weights
        self.bias = bias
        self.threshold = threshold
    def  __repr__(self):
        return f"Weights = {self.weights} , bias = {self.bias}, threshold = {self.threshold}"
    def step_activation(self,input=np.array([])):
        self.input_weight_check(input)
        product = self.weights * input
        biased = product + self.bias
        summation = sum(biased)
        return 0 if summation < self.threshold else 1
    def generate_output(self,activation,input=np.array([])):
        self.input_weight_check(input)
        if activation == "step":
            op = self.step_activation(input)
            print(f"output = {op} for input = {input} with {activation} as the activation function.")
            return op
        else:
            raise NameError(f"{activation} activation function is not available.")
    def delta_learning():
        pass
    def input_weight_check(self,input=np.array([])):
        if input.size != self.weights.size:
            raise ArithmeticError(f"Length of the input vector ({input.size}) is not equal to the length of weights ({self.weights.size}).")


or_gate = Perceptron(np.array([1,1]),0)
print(or_gate.generate_output("step",np.array([1,1])))
