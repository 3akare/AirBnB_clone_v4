#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

# Install Nginx Web Server
sudo apt -y update
sudo apt install -y nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
printf %s "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data/

touch default
printf %s "server {
        listen 80;
        listen [::]:80;
        add_header X-Served-By $HOSTNAME;

        root /var/www/school;
        index index.html;

        location /redirect_me {
            return 301 https://youtube.com;
        }

        location /hbnb_static/ {
            alias /data/web_static/current/;
            index index.html;
        }

        error_page 404 /404.html;
        location = /404.html {
            root /var/www/school/errors/;
        }
}
" > default

# Remove and replace existing configurations
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default
sudo mv default /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart
