
local:
	# python --version
	# pyenv shell 3.8.6
	node run-cypress.js
	cp ustvgotoken.js web
	python -m http.server --directory ./web 88

s3updatetoken:
	node run-cypress.js
	aws s3 cp ustvgotoken.js s3://tv.hugoalvarado.net/ --profile hugo102

