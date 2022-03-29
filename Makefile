
help:
	@echo 'Makefile for pelican website                                              '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make install                        install all necessary dependencies '   
	@echo '   make requirements                   compile requirements.txt           '
	@echo '   make compile                        generate the web site once         '
	@echo '   make regenerate                     regenerate the web site upon change'
	@echo '   make publish                        publish on github pages            '
	@echo '   make localhost                      serve site at http://localhost:8000'
	@echo '   make publish                        upload the web site via gh-pages   '
	@echo '                                                                          '

install:
	pip install --upgrade pip wheel pip-tools
	pip-sync requirements/requirements.txt
	# pip install -e .

requirements:
	pip install pip-tools
	pip-compile requirements.in

compile:
	pelican $(CURDIR)/content -s pelicanconf.py -o $(CURDIR)/felixbrunner.github.io

regenerate:
	pelican -r $(CURDIR)/content -s pelicanconf.py -o $(CURDIR)/felixbrunner.github.io

localhost:
	pelican -lr $(CURDIR)/content -s pelicanconf.py --relative-urls -o $(CURDIR)/felixbrunner.github.io -p 8000

publish:
	pelican $(CURDIR)/content -s publishconf.py -o $(CURDIR)/felixbrunner.github.io
	cd ./felixbrunner.github.io
	git add .
	git checkout -b make-publish
	git commit -m "make publish"
	git push origin/make-publish
	# create mr
	cd ..

.PHONY: install requirements compile regenerate localhost publish