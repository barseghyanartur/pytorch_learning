# Playing with PyTorch
This repository is my playground for getting to know [PyTorch](https://pytorch.org/ "PyTorch") library of python.
Mainly I've gone through PyTorch's [60 minutes blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html "blitz") and [Aakash NS's webinar](https://www.youtube.com/watch?v=GIsg-ZUy0MY "webinar's video").
To install all of your requirements, just run the command below in your terminal:
<br>
``` pip install -r requirements.txt ```
## Code Components Description
### [small_unittest_for_torch](https://github.com/s-mostafa-a/pytorch_learning/blob/master/small_unittest_for_torch.py)
This is a small and useful unittest for the tensors generated by models. It has two responsibilities: 
* check the shape of a tensor
* check if two tensors are equal in values

The first one will be quite useful if you are creating a novel structure of neural networks. Shape checking for tensor will provide a pretty decent prevention to future unwanted results or bugs.
### [basics](https://github.com/s-mostafa-a/pytorch_learning/tree/master/basics)
This directory has got all details I've extracted from tutorials. Especially in the notes.py file, I've written some comments which I think they can be helpful for all my future projects.

### [linear_regression](https://github.com/s-mostafa-a/pytorch_learning/tree/master/linear_regression)
This one has got two files, which I've implemented linear regression with two approaches: [with](https://github.com/s-mostafa-a/pytorch_learning/blob/master/linear_regression/linear_regression_with_nn_package.py) and [without](https://github.com/s-mostafa-a/pytorch_learning/blob/master/linear_regression/linear_regression_without_nn_package.py) nn class of torch. 
<br>
Both are quite simple codes, but it was necessary for me to know what is going on inside the nn.Linear class. Also, the Dataset is a random matrix in which columns are some random features.
### [logistic_regression](https://github.com/s-mostafa-a/pytorch_learning/tree/master/logistic_regression)
At this directory, I've written two classifications for the MNIST dataset. They do the same thing logically, but they are different in implementation.
[The one with _not_best_practice ending](https://github.com/s-mostafa-a/pytorch_learning/blob/master/logistic_regression/mnist_classification_not_best_practice.py) is all written by myself, and [the other one](https://github.com/s-mostafa-a/pytorch_learning/blob/master/logistic_regression/mnist_classification_best_practice.py) is from Aakash's webinar with some modifications.
### [simple_deep_neural_net](https://github.com/s-mostafa-a/pytorch_learning/tree/master/simple_deep_neural_net)
Things implemented here are just like the above's, but instead of a linear model, I've put a [DNN model](https://github.com/s-mostafa-a/pytorch_learning/blob/master/simple_deep_neural_net/dnn_model.py) with just one hidden layer, which is so simple.
### [simple_convolutional_neural_net](https://github.com/s-mostafa-a/pytorch_learning/tree/master/simple_convolutional_nerual_net)
Here is also something like the simple deep neural network, two ways of implementation, which are logically the same. The difference between them with simple deep neural nets are just in the models.
### [simple_generative_adversarial_net](https://github.com/s-mostafa-a/pytorch_learning/tree/master/simple_generative_adversarial_net)
This one is quite different from the above models. To be completed! (both implementation and documentation)