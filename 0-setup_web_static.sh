#!/usr/bin/env bash
# sets up a web a web server

# install nginx
if ! command -v nginix &>/dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# create folders
sudo mkdir -p /data/web_static/{releases/test,shared}

# create a fake html template

echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# create a symbolix link
sudo ln -sf /data/web_static/releases/test/ data/web_static/current

# update nginix configuration
config_path="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static/ {s/\# alias/alias/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# sendfile on/sendfile on/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# expires/expires/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# add_header/ add_header/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# root/ root/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# index/ index/}' "$config_path"
sudo sed -i '/location \/hbnb_static/ {s/\# }/}/}' "$config_path"

# restart nginx
sudo service nginx restart

# exit successfully
exit 0
