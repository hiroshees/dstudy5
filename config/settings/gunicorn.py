# Non logging stuff
bind = "127.0.0.1:8080"
workers = 3

# Access log - records incoming HTTP requests
#accesslog = "/home/ec2-user/workspace_python/dstudy5/logs/gunicorn/access.log"

# Error log - records Gunicorn server goings-on
#errorlog = "/home/ec2-user/workspace_python/dstudy5/logs/gunicorn/error.log"

# Whether to send Django output to the error log 
capture_output = True

# How verbose the Gunicorn error logs should be 
loglevel = "info"

