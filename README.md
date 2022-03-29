# Pelican for Python directory for my personal website

This repository generates my website. It is built with Pelican, and currently uses the Pelican Boostrap 3 theme.

## Create Output
The Makefile contains several options to generate the HTML output.
- make compile: compile the static files for the website once
- make regenerate: keep compiling the website when there is a content change
- make localhost: set up a local test website that updates its content
- make publish (not tested): compile website and push to github pages

## Alternative Preview Method
- go to output path
- set up virtual server `python -m http.server`
- open [localhost:8000](http://localhost:8000/) in browser

<!-- RENAME TO BEEWITS -->