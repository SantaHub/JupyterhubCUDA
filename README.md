# JupyterhubCUDA

## GPU Activation

 - install the proprietary and tested NVIDIA Driver in additional drivers option in software & update
 - Reboot to take effect
 - `nvidia-smi` should list the GPUs you have.
 - since we are using docker images we dont have to install CUDA on host machine

## Jupyterhub image creation 

Ref : https://tustunkok.github.io/tutorial/notes-to-myself/vps/2020/05/16/how-to-create-a-gpu-powered-containerized-multi-user-jupyterhub-research-server.html