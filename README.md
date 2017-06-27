# Neural-Networks-Intro  

This repository is intended to present a highly accessible introduction to neural networks, building upon first principles. In my personal study of neural networks, I have found loads of excellent resources (some of which I'll link to), but have been forced to pull these resources together in order to understand the big picture. This introduction will build up from simple linear regression to a basic neural network.

Similar to the experience that [Andrej Karpathy describes](http://karpathy.github.io/neuralnets/) (see paragraph 2), neural networks became much less of a mystery to me when I started writing code and stopped paying as much attention to long, detailed mathematical derivations. To that end, this introduction will introduce as much math as is necessary to code up the neural network architectures discussed, and little more (hopefully). That does mean that it will involve derivative calculations (a lot of them), but it will only include those that will then be translated to code.


## Following Along

To follow along with the repository in browser, you can simply click through the repository. Note that the image links will not render properly, because I chose to use HTML `<img>` tags in order to style some of the images (and it appears that IPython notebooks won't render those correctly on GH). The images are farily helpful, so it's recommended you follow along interactively via one of the options listed below.

To follow along with the repository interactively (and have the images render appropriately), you can do one of two things: 

1. Fire up the Binder below. This will launch a Jupyter notebook that serves this repository through a Docker Container, and will allow you to run everything from within your browser. The potential downside is that any changes you make will not be saved when you shutdown your browser. This should work with Python 2 or 3.

 [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/sallamander/neural-networks-intro) 

 *Note*: This appears to have become a little dated since it was originally put together, and support will not be maintained for this option since it relies on Binder.

2. Clone this repository, and then open the HTML files in each chapter in your browser, or pull open the notebooks.
 
 Clone the repository: 

 ```bash
git clone https://github.com/sallamander/neural-networks-intro/ 
```

 If working with the notebooks, add the following line to your `.bashrc` or `.bash_profile`

 ```bash    
export PYTHONPATH="/Users/sallamander/projects/neural-networks-intro:$PYTHONPATH"
```

 **Note**: You will have to change `/Users/sallamander/projects` to point to the location of wherever you clone the repository to.

## Comments or Suggestions?

Please feel free to open an issue to leave feedback, propose changes and/or additions, etc. 
