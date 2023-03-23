# Overview

[![License](https://img.shields.io/github/license/angarc/bulk-mv)]()
[![Issues](https://img.shields.io/github/issues/angarc/bulk-mv)]()
[![codecov](https://img.shields.io/codecov/c/github/angarc/bulk-mv)]()
[![build](https://img.shields.io/github/actions/workflow/status/angarc/bulk-mv/build.yml)]()
[![PyPI](https://img.shields.io/pypi/v/bulk-mv)](https://pypi.org/project/bulk-mv/)


bulk-mv is an interactive tool that does what the `mv` command does, but for mulitiple files, with the ability to do more like adding and deleting files as well.

# Installation

```
pip install bulk-mv
```

# Usage

When you run `bmv [path]`, a vim buffer with a representation of the file tree starting at the directory at `[path]` will open.

Something like this:

```
web/
web/pages/
web/pages/a.html
web/pages/b.html
web/static/
web/static/main.css
web/static/main.js
web/images/ 
web/images/photo.jpg
web/images/delete_me.jpg
```

## Creating new files/directories

You can add files or directories using the `+` operator. It works by typing `+ path/to/new/file.txt` on a new line.
If any directories along the path to this new file don't exist, bmv will create them.

```
+ web/fonts/

web/
web/pages/
...
```

## Deleting files/directories

You can delete files or directories using the `-` operator. It works by typing `- path/to/new/file.txt` on a new line.

```
web/
...
web/images/photo.jpg
- web/images/delete_me.jpg
```


## Renaming files/directories

You can rename files or directories using the `->` operator. 

```
web/
web/pages/
web/pages/a.html -> web/pages/c.html
web/pages/b.html -> web/pages/d.html
```


## Moving files/directories

You can move files or directories using the `=>` operator. Moving files to paths with non-existent directories *will not be created automatically*.
Use the `add` operator to do it first.

```
web/
web/static/
web/images/ => web/static/images/
web/images/photo.jpg
web/images/delete_me.jpg
```

## Putting it all together.

Say you wanted to:

1. Delete the `delete_me.jpg` file.
2. Move the `images` folder to the `static` folder.
3. Rename `main.js` to `script.js`
4. Create a `web/fonts/` folder

You would write:

```
+ web/fonts/

web/
web/pages/
web/pages/a.html
web/pages/b.html

web/static/
web/static/main.css
web/static/main.js -> web/static/script.js

web/images/ => web/static/images/
web/images/photo.jpg
- web/images/delete_me.jpg
```

When you save and quit vim, `bmv` will perform all the operations.

## Order of operations

Operations are given the following precedence:

1. add
2. delete
3. rename
4. move


