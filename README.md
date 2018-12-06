# pyheat

[![pypiv](https://img.shields.io/pypi/v/py-heat.svg)](https://pypi.python.org/pypi/py-heat)
[![pyv](https://img.shields.io/pypi/pyversions/py-heat.svg)](https://pypi.python.org/pypi/py-heat)
[![Build Status](https://travis-ci.org/csurfer/pyheat.svg?branch=master)](https://travis-ci.org/csurfer/pyheat)
[![Coverage Status](https://coveralls.io/repos/github/csurfer/pyheat/badge.svg?branch=master)](https://coveralls.io/github/csurfer/pyheat?branch=master)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/pyheat/master/LICENSE)
[![Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/csurfer)

Profilers are extremely helpful tools. They help us dig deep into code, find and understand performance bottlenecks. But sometimes we just want to lay back, relax and still get a gist of the hot zones in our code.

> A picture is worth a thousand words.

So, instead of presenting the data in tabular form, if presented as a heatmap visualization, it makes comprehending the time distribution in the given program much easier and quicker. That is exactly what is being done here !

## Demo

![Demo](http://i.imgur.com/qOeXUPR.png)

## Scroll Demo

![ScrollDemo](https://i.imgur.com/5IdH8AG.gif)

## Features

- Simple CLI interface.
- No complicated setup.
- Heatmap visualization to view hot zones in code.
- Ability to export the heatmap as an image file.
- Ability to scroll, to help view heatmap of large py files.

## Setup

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
# To view the heatmap.
pyheat <path_to_python_file>
# To output the heatmap as a file.
pyheat <path_to_python_file> --out image_file.png
pyheat --help
```

### As a module

```python
from pyheat import PyHeat
ph = PyHeat(<file_path>)
ph.create_heatmap()
# To view the heatmap.
ph.show_heatmap()
# To output the heatmap as a file.
ph.show_heatmap('image_file.png')
```

## Contributing

### Bug Reports and Feature Requests

Please use [issue tracker](https://github.com/csurfer/pyheat/issues) for reporting bugs or feature requests.

### Development

Pull requests are most welcome.

### Buy the developer a cup of coffee!

If you found the utility helpful you can buy me a cup of coffee using

[![Donate](https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
