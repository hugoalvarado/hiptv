
local:
	# python --version
	# pyenv shell 3.8.6
	node run-cypress.js
	cp ustvgotoken.js web
	python -m http.server --directory ./web 88

s3updatetoken:
	# node run-cypress.js
	python get_token/get_token.py > ustvgotoken.js
	aws s3 cp ustvgotoken.js s3://tv.hugoalvarado.net/ --profile hugo102
	aws s3 cp web/index.html s3://tv.hugoalvarado.net/ --profile hugo102
	aws s3 cp web/player.css s3://tv.hugoalvarado.net/ --profile hugo102

