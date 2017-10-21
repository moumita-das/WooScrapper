sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install python3-setuptools
sudo easy_install3 pip
pip3 install BeautifulSoup4 lxml selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.16.1-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.16.1-linux64.tar.gz		
sed -i 's/uninstalled/installed/' .env
