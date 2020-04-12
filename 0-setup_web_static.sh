#!/usr/bin/env bash
sudo apt-get install update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown ubuntu:ubuntu -R /data/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
FILE=/etc/nginx/sites-available/default
REDIRECT_STRING="location /hbnb_static {\n alias /data/web_static/current; \n}\n"
sudo sed -i "39i $REDIRECT_STRING" $FILE
sudo service nginx restart

