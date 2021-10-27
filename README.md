# JupyterhubCUDA

## GPU Activation

 - install the proprietary and tested NVIDIA Driver in additional drivers option in software & update
 - Reboot to take effect
 - `nvidia-smi` should list the GPUs you have.
 - since we are using docker images we dont have to install CUDA on host machine

 - install for docker
 ```
sudo apt install curl
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list 

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list 
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo apt-get install nvidia-container-runtime

sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl status docker

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