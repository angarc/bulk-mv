![cover_photo](./branding/logo.png)

# Overview

[![License](https://img.shields.io/github/license/angarc/bulk-mv)]()
[![Issues](https://img.shields.io/github/issues/angarc/bulk-mv)]()
[![codecov](https://img.shields.io/codecov/c/github/angarc/bulk-mv)]()
[![build](https://img.shields.io/github/actions/workflow/status/angarc/bulk-mv/build.yml)]()
[![PyPI](https://img.shields.io/pypi/v/bulk-mv)](https://pypi.org/project/bulk-mv/)
[![Docs](https://img.shields.io/readthedocs/bulk-mv)](https://bulk-mv.readthedocs.io/en/latest/)

bulk-mv is an interactive tool that does what the `mv` command does, but for mulitiple files, with the ability to do more like adding and deleting files as well.

# Installation

```
pip install bulk-mv
```

# Usage

When you run `bmv <path>`, a bulk-mv (bmv) file will open in a vim buffer, representing the file tree starting in the directory located at `<path>`.

Then, you can make your modifications in the vim buffer, and run `:wq` to perform the changes.

Suppose your directory file tree was this:

```tree
.
├── README.md
└── web
    ├── public
    │   └── photos
    │       └── logo.png
    └── static
        ├── javascript
        │   ├── auth.js
        │   └── main.js
        └── styles
            └── main.css
```

Then running `bmv <path>` will open up the following bmv file in a vim buffer:

```bmv
[./] {
  README.md
  [web] {
    [public] {
      [photos] {
        logo.png
      }
    }
    [static] {
      [styles] {
        main.css
      }
      [javascript] {
        auth.js
        main.js
      }
    }
  }
}
```

## Creating new files/directories

You can add files or directories using the `+` operator. 

Here's how to use it to add new files and directories

```bmv
[./] {
  README.md
  [web] {
    [public] {
      [photos] {
        logo.png
      }
    }

    + [templates] {
      + [dashboard] {
        dashboard.html
        admin.html
      }

      index.html
      about.html
    }

    [static] {
      [styles] {
        main.css
        + dashboard.css
      }
      [javascript] {
        auth.js
        main.js
      }
    }
  }
}
```

Notice how you can add multiple nested directories. If you want to add a single file
you need to type `+ new_file.txt` in the directory block where you want it.

If you create a new directory with (also new) files inside of it, you don't need to use
the `+` operator to add them. But for new nested directories, you do need to use the `+` operator.

## Deleting files/directories

You can delete files or directories using the `-` operator. 

You can delete entire directories or files like this:

```bmv
[./] {
  README.md
  [web] {
    [public] {
      [photos] {
        logo.png
      }
    }
    [static] {
      - [styles] {
        main.css
      }
      [javascript] {
        - auth.js
        main.js
      }
    }
  }
}
```

Running this would delete the `./web/static/javascript/auth.js` file as well as the `./web/static/styles/` folder (and of course everything in it).

## Renaming files/directories

You can rename files or directories using the `>` operator. 

```bmv
[./] {
  README.md
  [web] {
    [public] {
      [photos > images] {
        logo.png
      }
    }
    [static] {
      [styles] {
        main.css
      }
      [javascript] {
        auth.js
        main.js > script.js
      }
    }
  }
}
```

Running this would change rename the `./web/public/photos/` directory to `./web/public/images/`, and it rename `./web/static/javascript/main.js` to `./web/static/javascript/script.js`

## Moving files/directories

You can move files or directories using the `>>` operator. Moving files to paths with non-existent directories *will not be created automatically*.

```bmv
[./] {
  README.md >> ./web
  [web] {
    [public] {
      [photos >> ./web/static] {
        logo.png
      }
    }
    [static] {
      [styles] {
        main.css
      }
      [javascript] {
        auth.js
        main.js
      }
    }
  }
}

```

Running this would move `./README.md` to `./web/README.md`, and move `./web/public/photos/` to `./web/static/photos`.

You currently have to specify the full path to the directory you want to move the file/directory to starting from root path of the file tree (in this case, it's `./`).

## Putting it all together.

Of course, you can mix and match these operations all in one go. Just note the order of operations to avoid making a mistake, like moving a file to a directory that you haven't created yet, for example.

Operations are given the following precedence:

1. add
2. delete
3. rename (files first, then directories)
4. move (files first, then directories)

## Caveat

So far, bulk-mv only works on files/directories with [POSIX Portable filenames/dirnames](https://www.ibm.com/docs/en/zos/2.2.0?topic=locales-posix-portable-file-name-character-set).

In the future version, I want bulk-mv to support any type of support filenames on Mac OS, Linux, and Windows.