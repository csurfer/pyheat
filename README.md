# pyheat

[![Build Status](https://travis-ci.org/csurfer/pyheat.svg?branch=master)](https://travis-ci.org/csurfer/pyheat)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/pyheat/master/LICENSE)
[![Coverage Status](https://coveralls.io/repos/github/csurfer/pyheat/badge.svg?branch=master)](https://coveralls.io/github/csurfer/pyheat?branch=master)

Profilers are extremely helpful tools. They help us dig deep into code, find and
understand performance bottlenecks. But sometimes we just want to lay back, relax
and still get a gist of the hot zones in our code.

> A picture is worth a thousand words.

So, instead of presenting the data in tabular form, if presented as a heatmap visualization, it makes comprehending the time distribution in the given program much easier and quicker. That is exactly what is being done here !

![pyheatmap](http://i.imgur.com/qOeXUPR.png)

## Features

:star: Simple CLI interface.

:star: No complicated setup.

:star: Heatmap visualization to view hot zones in code.

## Setup

With `pip` installed on your system, execute

### Using pip

```bash
pip install py-heat
```

### Directly from the repository

```bash
git clone https://github.com/csurfer/pyheat.git
python pyheat/setup.py install
```

## Usage

### As a command

```bash
pyheat --pyfile <path_to_python_file>
```

To view help use:

```bash
pyheat --help
```

### As a module
```python
from pyheat import PyHeat
ph = PyHeat(<file_path>)
ph.create_heatmap()
ph.show_heatmap()
```

## Contributing

### Bug Reports and Feature Requests
Please use [issue tracker](https://github.com/csurfer/pyheat/issues) for reporting bugs or feature requests.

### Development
Pull requests are most welcome.
