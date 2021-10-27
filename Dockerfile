# Creating a jupyterhub image
FROM jupyterhub/jupyterhub

# Required for Jupyterhub authentication and notebook spawning
RUN pip install dockerspawner oauthenticator

# make sure to have this on the build folder
COPY jupyterhub_config.py .