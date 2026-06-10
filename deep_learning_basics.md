1. Neural Network :
A Neural Network is a computing system inspired by the structure and functioning of the human brain. It consists of interconnected nodes called neurons that process information, learn patterns from data, and make predictions.
Each neuron receives input, processes it using weights and biases, applies an activation function, and passes the output to the next layer.
Neural networks are the foundation of Deep Learning and are widely used for solving complex problems such as image recognition, speech processing, and natural language understanding.

eg.:Face recognition in smartphones .
    Voice assistants like Siri and Google Assistant .
    Self-driving cars detecting objects on the road .

2.Layers in Neural Networks :
A neural network is structured in layers, and each layer has a specific role.
Input Layer :
The input layer is the first layer of a neural network. It receives raw data and passes it to the next layer for processing.
Each node represents one feature in the dataset.
No computation happens here.
It simply forwards data.

Eg.:
If we are predicting house prices:
Input features = size, location, number of rooms.

Hidden Layer :
Hidden layers are the core of a neural network where learning happens.
They perform mathematical transformations on inputs.
They extract patterns and features from data.
A network with many hidden layers is called a Deep Neural Network.
eg.:Example:
In image recognition:
First layer detects edges
Middle layers detect shapes
Deep layers detect objects like faces

Output Layer:
The output layer produces the final result of the model.
It depends on the type of problem:
Binary classification → 1 neuron (0 or 1)
Multi-class classification → multiple neurons
Regression → single continuous value

Example:
Email classification → Spam / Not Spam
Digit recognition → 0–9 classification

3. Activation Functions :
Activation functions introduce non-linearity into the model. Without them, the neural network would behave like a simple linear model.
ReLU (Rectified Linear Unit)

Formula:

f(x) = max(0, x)
If input is negative → output is 0
If input is positive → output is same value

Advantages:

Fast computation
Reduces vanishing gradient problem
Most commonly used activation function

Sigmoid Function

Formula:

1 / (1 + e^(-x))
Output range: 0 to 1
Converts values into probabilities

Advantages:
Good for binary classification
Disadvantages:
Vanishing gradient problem
Slower convergence

Tanh Function

Formula:

(-1 to +1 output)
Similar to sigmoid but centered around zero
Advantages:
Better than sigmoid for hidden layers
Helps with negative and positive values
Disadvantages:
Still suffers from vanishing gradient problem

Softmax Function :
Softmax converts raw outputs into probabilities that sum to 1.

Example:
Class A → 0.1
Class B → 0.7
Class C → 0.2
Advantages:
Best for multi-class classification

4. Training Concepts in Neural Networks :
Training is the process where the model learns patterns from data by adjusting weights.
Epoch :

An epoch is one complete pass through the entire training dataset.

Example:

If dataset has 1000 samples:
1 epoch = model sees all 1000 samples once
 More epochs → better learning
Too many epochs → overfitting

Batch Size :
Batch size is the number of samples processed before updating model weights.
Example:
Dataset = 1000 samples
Batch size = 100
Model updates weights 10 times per epoch

Small batch size → better generalization
Large batch size → faster training

Learning Rate:

Learning rate controls how much the model updates weights during training.
High learning rate → fast but unstable learning
Low learning rate → slow but accurate learning
Finding the right learning rate is very important for performance.

Loss Function:

A loss function measures how wrong the model’s predictions are.
Goal: Minimize loss
Common loss functions:
Mean Squared Error (Regression)
Cross-Entropy Loss (Classification)
Lower loss = better model performance

Optimizer :

An optimizer updates model weights to reduce loss.
Popular optimizers:
SGD (Stochastic Gradient Descent)
Adam (most commonly used)
RMSProp
Adam optimizer is widely used because it adapts learning rate automatically

Gradient Descent :

Gradient Descent is the core algorithm used to train neural networks.
Steps:
Model makes prediction
Calculate error (loss)
Compute gradient (direction of error)
Update weights
Repeat until loss is minimized
This process helps the model gradually improve accuracy.

