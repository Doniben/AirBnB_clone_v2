#!/usr/bin/env bash
# Stting up the web servers to deploy.
sudo apt_get update
sudo apt-get -y install nginx
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu -R /data/
sudo sed -i '48a\\n\tlocation hbnb_static/ {\n\t\talias /data/web_static/current;}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
