# Neural-Networks-Intro  

This repository is intended to present a highly accessible introduction to neural networks, building upon first principles. In my personal study of neural networks, I have found loads of excellent resources (some of which I'll link to), but have been forced to pull these resources together in order to understand the big picture. This introduction will build up from simple linear regression to convolutional and even recurrent neural networks, with the end goal of providing a reasonably comprehensive picture of how, why, and when neural networks work. 

Similar to the experience that [Andrej Karpathy describes](http://karpathy.github.io/neuralnets/) (see paragraph 2), neural networks became much less of a mystery to me when I started writing code and stopped paying as much attention to long, detailed mathematical derivations. To that end, this introduction will introduce as much math as is necessary to code up the neural network architectures discussed, and little more (hopefully). That does mean that it will involve derivative calculations (a lot of them), but it will only include those that will then be translated to code.

The plan for the organization of this introduction is to have four "mini-books", each of which builds off of the last: 

1. [**Shallow Neural Networks**](https://github.com/sallamander/neural-networks-intro/tree/master/mini-books/shallow-neural-networks)
2. **Deep Neural Networks** 
3. **Convolutional Neural Networks** 
4. **Recurrent Neural Networks**

I'll fill the details in as I have them - this is a work in progress. 

## Following Along

To follow along with the repository interactively, you can do one of two things: 

1. Fire up the Binder below. This will launch a Jupyter notebook that serves this repository through a Docker Container, and will allow you to run everything from within your browser. The potential downside is that any changes you make will not be saved when you shutdown your browser. This should work with Python 2 or 3, but please open up an issue if it doesn't!

 [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/sallamander/neural-networks-intro) 

2. Clone this repository, and then add it to your `PYTHONPATH`.
 
 Clone the repository: 

 ```bash
git clone https://github.com/sallamander/neural-networks-intro/ 
```

 Add the following line to your `.bashrc` or `.bash_profile`

 ```bash    
export PYTHONPATH="/Users/sallamander/projects/neural-networks-intro:$PYTHONPATH"
```

 **Note**: You will have to change `/Users/sallamander/projects` to point to the location of wherever you clone the repository to.

## Current Status

I have finished the first mini-book (see the [README](https://github.com/sallamander/neural-networks-intro/tree/master/mini-books/shallow-neural-networks/README.md) for details), and am about to dive into the second one.

I'm hopeful that I can have that one done in 1-2 months; these are taking a little more time than I thought they would. 

## Comments or Suggestions?

I'd love to get some feedback as I'm working on this (especially on whether anybody finds it useful/helpful). Please feel free to open an issue to leave feedback, propose changes and/or additions, etc. 
