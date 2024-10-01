# pelican 
PY?=
PELICANOPTS=

# paths
BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/felixbrunner.github.io
CONFFILE=$(BASEDIR)/beewits/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/beewits/publishconf.py

# github pages
GITHUB_PAGES_BRANCH=user-page
GITHUB_USER_PAGE=git@github.com:felixbrunner/felixbrunner.github.io.git
GITHUB_USER_PAGE_BRANCH=main
GITHUB_USER_PAGE_REMOTE=$(GITHUB_USER_PAGE)/$(GITHUB_USER_PAGE_BRANCH)

help:
	@echo 'Makefile for pelican website                                              '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make install                        install all necessary dependencies '   
	@echo '   make requirements                   compile requirements.txt           '
	@echo '   make compile                        generate the web site once         '
	@echo '   make clear                          clear output directory             '
	@echo '   make regenerate                     regenerate the web site upon change'
	@echo '   make publish                        publish on github pages            '
	@echo '   make localhost                      serve site at http://localhost:8000'
	@echo '   make publish                        upload the web site via gh-pages   '
	@echo '                                                                          '

install:
	pip install --upgrade pip wheel pip-tools
	pip-sync requirements/requirements.txt
	pip install -e "git+https://github.com/getpelican/pelican-plugins/#egg=pelican-tipue-search&subdirectory=tipue_search"
	pip install -e .
	if ! [ -d "./pelican-themes" ]; then git clone https://github.com/getpelican/pelican-themes; fi
	if ! [ -d "./pelican-plugins" ]; then git clone https://github.com/getpelican/pelican-plugins; fi
	git fetch $(GITHUB_USER_PAGE) $(GITHUB_USER_PAGE_BRANCH):$(GITHUB_PAGES_BRANCH)

requirements:
	pip install --upgrade pip wheel pip-tools
	pip-compile requirements/requirements.in

compile:
	pelican "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clear:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	pelican -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

localhost:
	pelican -lr $(CURDIR)/content -s "$(CONFFILE)" --relative-urls -o "$(OUTPUTDIR)" -p 7931

publish:
	pelican "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
	ghp-import -o "$(OUTPUTDIR)" -b $(GITHUB_PAGES_BRANCH) -m "publish updated pelican generated site"
	git push $(GITHUB_USER_PAGE) $(GITHUB_PAGES_BRANCH):$(GITHUB_USER_PAGE_BRANCH)

.PHONY: install requirements compile clear regenerate localhost publish