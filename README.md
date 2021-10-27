# JupyterhubCUDA

## GPU Activation

 - install the proprietary and tested NVIDIA Driver in additional drivers option in software & update
 - Reboot to take effect
 - `nvidia-smi` should list the GPUs you have.
 - since we are using docker images we dont have to install CUDA on host machine

 - install for docker
 ```
sudo apt install curl
sudo apt install docker
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt update
sudo apt install -y nvidia-docker2

sudo systemctl restart docker
```
Test with 
```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```


## Messing default hub image

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
 - Tried to login with new user student but had 
 `Spawn failed: Server at http://127.0.0.1:49199/user/student/ didn't respond in 30 seconds`


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