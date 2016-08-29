# Moodle token Auth for jupyterhub

## How to use
1. config your jupyterhub config
```
c.JupyterHub.authenticator_class = 'moodleauth.NCKUAuthenticator'
```

2. comfirm your students' account are in your System User list.
( this version won't auto adduser to your system )

3. Start your jupyterhub service, then use moodle account to login.