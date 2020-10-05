# Pelican for Python directory for personal website

This is my personal site. It has been built with Pelican, using the Pelican Boostrap 3 theme.

## Create Output
Run the following command in the anaconda command line to assemble the website in the HTML submodule:

```
pelican -s pelicanconf.py
```

## Preview

go to output path
```
cd ./felixbrunner.github.io
```
set up virtual server
```
python -m http.server
```
open in browser

http://localhost:8000/
