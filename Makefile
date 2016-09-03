run:
	FILENAME=accounts-$(date +'%Y%m%d-%H%M').txt \
		ptc2 --email YOUR_EMAIL@gmail.com --compact -o ${FILENAME} -m 5 \
		&& python tos.py ${FILENAME} \
		&& python convert.py ${FILENAME}

