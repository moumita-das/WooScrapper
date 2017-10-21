INPUT="./.env"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read -r line
do
	if [[ "$line" == "STATUS=uninstalled" ]]; then
		sudo apt-get update
		sudo apt-get -y upgrade
		sudo apt-get install -y python3-pip urllib bs4 lxml selenium
		wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz
		sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.16.1-linux64.tar.gz -O > /usr/bin/geckodriver'
		sudo chmod +x /usr/bin/geckodriver
		rm geckodriver-v0.16.1-linux64.tar.gz
		sed -i 's/uninstalled/installed/' .env
	fi
	python  flickr.py
done < $INPUT
