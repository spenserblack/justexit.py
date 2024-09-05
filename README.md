# `justexit.py`

```python-console
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
```

Do you get this often? I get this about once a day. It's a habit from Shell and Ruby that I
just can't break. With this tool, you can call `exit` from your Python console and it will
*actually exit :tada:*

## Installation

First, download [`justexit.py`](justexit.py) somewhere. Then, wherever you define environment
variables (e.g. `.bashrc`), define the `PYTHONSTARTUP` variable to point to the path of
`justexit.py`. For example:

```bash
# .bashrc
export PYTHONSTARTUP="$HOME/justexit.py"
```

Then, next time you're in an interactive Python console, you can just type `exit` and it will
actually exit.

```python-console
>>> exit
```
