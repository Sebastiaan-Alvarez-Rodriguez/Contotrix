# Contotrix
Contotrix is a fast, OS independent framework to efficiently compare different HTML parsers,
using multiprcessing, resource measuring, and large-scale result analysis.

## Installing
To be able to run all parts of this framework, the follwing needs to be installed
 1. Python 3.6 or greater
 2. Python's matplotlib library
 3. Python vaex library for result analysis

## Execution
Go to the top directory of this framework and type
```bash
python3 run.py
```

## Usage
After starting this framework, you should get a commandline tool.
At any point, type 'h' or 'help' to get a list of commands you can use.  

To install a parsers, use `install <name(s)>`.
 > Note: Parsers can have additional requirements, which are made clear when trying to install these parsers. Pay attention during installation to avoid runtime crashes

To download a dataset, use either the `commoncrawl` or `crawl` command.
The `commoncrawl` command downloads crawled webpages from the [CommonCrawl](https://commoncrawl.org/) project.
The `crawl` command crawls the web on its own, given a starting position.


To execute parsers, use `exec <repeats> <name(s)>`.
You will be asked about timeouts, how many cores to run on, etcetera.
Timeouts are important, because some parsers may take several hours to parse a seemingly simple HTML page in some conditions, and you might not want to wait on this.

To generate graphs, type `graph(s)` to go to the graphs-submodule.
This submodule is responsible for generating all kinds of interesting data from generated output.

To generate incorrect HTML, type `malform(er)` to go to the malformer-submodule.
This submodule inserts minor and major errors in given HTML pages in a random fashion.

## Adding support for a parser
Supporting a parser is very simple.
There needs to be a directory in installers folder.
The name of the directory is the name of your parser.
It cannot and should not contain spaces, '/', '\' (for platform independence).
In the directory should be at least 3 files:
 1. `install.py`: File with a function `install(location, fs)`. Function is called when user wants to install your tool to given `location`. `fs` is an object to interact with the filesystem. see `lib/fs.py`.
 It should return `True` on succesful install, otherwise `False`
 2. `execute.py`: File with a function `execute(location, fs)`. Function is called when user wants to execute your tool, which is installed at `location`. It should return a list, containing the entire call of your function. See `installers/goparser` for a simple example.
 3. `config.xml`: File containing a `<deps>` section. In this section, use `<d>My installation requirement v1.0</d>` to denote installation requirements. These are displayed to the user on installation

What you further have in installer directory is not important and up to you.
It should likely contain source code for the parser.
See `installers/goparser` for a simple example.
