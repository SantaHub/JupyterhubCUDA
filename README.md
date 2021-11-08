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

## Login to Jupyterhub

Using PAM authenticator. So needs to create users in image.
 - Run default jupyterhub image 
 ```
 docker run -d -p 8000:8000 --name jupyterhub jupyterhub/jupyterhub jupyterhub
 ```
 - Go to image bash
 ```
docker exec -it jupyterhub bash
```
 - add new user
 ```
 adduser student
 ```
- add jupyter notebook for spawning
```
 pip install notebook
```

 Login as student at http://localhost:8000


## Verifying CUDA installation in Jupyterhub

```
import tensorflow as tf
tf.config.list.physical_devices('GPU')
tf.test.is_build_with_cuda()
```

## Saving docker images

Commit changes on image with a tag
```
docker commit <IAMGE_ID/IMAGE_NAME> <NEW-IMAGE-NAME>
docker commit 0fd419771dcd hub-with-student
```

## Jupyterhub image creation 

 - The dockerfile and config file are in the same repo
 - Build docker image. use sudo docker build or add user to docker group

 ``` 
 sudo usermod -aG docker $USER
 docker build --rm -t jupyterhub_custom .
 ```
 
- run the docker image
```
docker run --rm --gpus all jupyterhub jupyterhub_server
```

 
Ref : https://tustunkok.github.io/tutorial/notes-to-myself/vps/2020/05/16/how-to-create-a-gpu-powered-containerized-multi-user-jupyterhub-research-server.html