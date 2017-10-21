INPUT="./.env"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read -r line
do
	if [[ "$line" == "STATUS=uninstalled" ]]; then
		sudo apt-get update
		sudo apt-get -y upgrade
		sudo apt-get install -y python3-pip urllib csv bs4 lxml
		sed -i 's/uninstalled/installed/' .env
	fi
	python  flipkart.py
done < $INPUT
