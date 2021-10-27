import os

##Can Configure :
# DOCKER_JUPYTER_IMAGE : Jupyterlab image 
# DOCKER_NETWORK_NAME 
# DOCKER_NOTEBOOK_DIR

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.image = os.environ["DOCKER_JUPYTER_IMAGE"]
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
c.JupyterHub.hub_ip = os.environ["HUB_IP"]
c.Authenticator.admin_users = {'admin', 'bigParisi', 'parisi'}

from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator

# c.GitHubOAuthenticator.oauth_callback_url = \
#                     'http://<host_ip_addr>/hub/oauth_callback'
# c.GitHubOAuthenticator.client_id = '<client_id>'
# c.GitHubOAuthenticator.client_secret = '<client_secret>'

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {
          'jupyterhub-user-{username}': notebook_dir,
          'jupyterhub-shared': '/home/jovyan/work/shared',
          'jupyterhub-data': '/home/jovyan/work/data'
}

c.DockerSpawner.remove_containers = True
c.Spawner.default_url = '/lab'
