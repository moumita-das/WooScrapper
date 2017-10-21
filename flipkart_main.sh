INPUT="./.env"
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read -r line
do
	if [[ "$line" == "STATUS=uninstalled" ]]; then
		sudo bash setup.sh
		sed -i 's/uninstalled/installed/' .env
	fi
	python  flipkart.py
done < $INPUT
