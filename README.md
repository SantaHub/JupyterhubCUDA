# JupyterhubCUDA

## GPU Activation

 - install the proprietary and tested NVIDIA Driver in additional drivers option in software & update
 - Reboot to take effect
 - `nvidia-smi` should list the GPUs you have.
 - since we are using docker images we dont have to install CUDA on host machine

 - install for docker
 ```
sudo apt update
sudo apt install -y git curl docker
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list && sudo apt update
sudo apt install -y nvidia-docker2
sudo systemctl restart docker
```
Test with 
```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

# Get tensorflow image 


Ref : https://hub.docker.com/r/tensorflow/tensorflow/
```

docker run --rm -it --gpus all -p 8000:8000 -p 8787:8787  --name datalab  tensorflow/tensorflow bash

```

# Installing Jupyterhub

```
 apt install npm
 pip install jupyterhub
 npm install -g configurable-http-proxy
```

# Verifying CUDA installation in Jupyterhub

```
import tensorflow as tf
tf.config.list.physical_devices('GPU')
tf.test.is_build_with_cuda()
```

### Tensorflow 
```
import tensorflow as tf
tf.config.list_physical_devices('GPU')
tf.test.is_gpu_available()

```

### Torch

```
import torch
torch.cuda.is_available()
torch.cuda.device_count()
torch.cuda.get_device_name(0)

```

# Install R Server

```

sudo apt install -y r-base gdebi-core wget
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2021.09.1-372-amd64.deb
sudo gdebi rstudio-server-2021.09.1-372-amd64.deb

sudo rstudio-server verify-installation

```

Login to RServer : http://localhost:8787/

# Adding new User

```
adduser student

```

# Start Services

Add this to bashrc.
```
rstudio-server restart
jupyterhub
```

# Saving docker images

Commit changes on image with a tag
```
docker commit <IAMGE_ID/IMAGE_NAME> <NEW-IMAGE-NAME>
docker commit 0fd419771dcd jupyterHubDL

```
