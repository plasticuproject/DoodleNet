# Doodle Net
Convolutional Neural Network to convert crude sketches into faces.

## Requirements
* Linux (tested on Ubuntu 18.04)
* NVIDIA GPU with Compute Compability 3.X+
* NVIDIA Linux x86_64 Driver Version 390.46+
* Cuda Toolkit 9.1+
* cuDNN 7.1.3+
* libgpuarray
* GNU Make 4.1+
* cmake 3.10.2+
* Python 3.6.9+
    * python3-pip
        * cycler==0.10.0
        * Cython==0.29.15
        * h5py==2.10.0
        * Keras==2.3.1
        * Keras-Applications==1.0.8
        * Keras-Preprocessing==1.1.0
        * kiwisolver==1.1.0
        * Mako==1.1.2
        * MarkupSafe==1.1.1
        * matplotlib==3.2.0
        * numpy==1.18.1
        * opencv-python==4.2.0.32
        * pydot==1.4.1
        * pygame==1.9.6
        * pygpu==0.7.6+20.g9cec614
        * pyparsing==2.4.6
        * python-dateutil==2.8.1
        * PyYAML==5.3
        * scipy==1.4.1
        * six==1.14.0
        * Theano==1.0.4
        
## Build Environment Instructions
If you have not already, download and install the appropriate NVIDIA Drivers, Cuda Toolkit, and cuDNN library using the following links: </br>

**VIDEO DRIVER** https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa </br>
**CUDA TOOLKIT** https://developer.nvidia.com/cuda-toolkit </br>
**cuDNN** https://developer.nvidia.com/cudnn </br>
>**Note**: You may need to register an NVIDA Developer account to access the Cuda Toolkit and cuDNN downloads page. </br>

Inside a  python virtual environment, clone this repository and install the libraries in requirements.txt:
```
git clone https://github.com/plasticuproject/DoodleNet.git
cd DoodleNet
pip install -r requirements.txt
```
Install libgpuarray and pygpu:
```
git clone https://github.com/Theano/libgpuarray.git
cd libgpuarray
mkdir Build
cd Build
cmake .. -DCMAKE_BUILD_TYPE=Release
make
make install
cd ..
python setup.py build
python setup.py install
```

## Training A Model
To generate training data from the images in the `faces` directory, run the datagen.py script:
```
$ python datagen.py -h
usage: datagen.py [-h] [--test] [--sample [SAMPLE]]

Data Generator

optional arguments:
  -h, --help         show this help message and exit
  --test             use images in test folder instead of faces
  --sample [SAMPLE]  samples per image, default is 10)
```
You may use the images from the [faces94](https://cswww.essex.ac.uk/mv/allfaces/faces94.html) dataset I have provided, or you may use your own images by deleting the contents of the `faces` directory and placing your own images in there. You may also use the `--test` flag to use the 10 images inside the `test` directory to make sure everything is working, or to debug if you are having issues with VRAM capacity. </br>
If you would like to exponentially reduce the amount of images and training data you can run the remove_faces.py script. The faces94 data set used contains multiple pictures of individual people. Running this removes the multiples leaving roughly only one picture per person. It greatly reduces the size of the data set.

After generating the training data you can train your model with train.py:
```
$ python train.py -h
usage: train.py [-h] [--epoch [EPOCH]] [--batch [BATCH]]

Model Trainer

optional arguments:
  -h, --help         show this help message and exit
  --epoch [EPOCH]    number of epochs, default is 50
  --batch [BATCH]    batch size, default is 20)
```
This will produce a graph of your Network, a line graph of your training loss data, and your trained Neural Network Model.

## Using The Doodle Net Application
Just run:
```
python doodle.py
```
Right click the mouse and hold to draw on the left side of the screen and watch the results on the right side. Right click the mouse to clear the input.


