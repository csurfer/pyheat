# pyheat

[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/pyheat/master/LICENSE)

Profilers are extremely helpful tools. They help us dig deep into code, find and
understand performance bottlenecks. But sometimes we just want to lay back, relax
and still get a gist of the hot zones in our code.

> A picture is worth a thousand words.

So, instead of presenting the data in tabular form, if presented as a heatmap visualization, it makes comprehending the time distribution in the given program much easier and quicker. That is exactly what is being done here !

![pyheatmap](readme-res/pyheatmap.png)

## Features

:star: Simple CLI interface.

:star: No complicated setup.

:star: Heatmap visualization to view hot zones in code.

## Setup

With `pip` installed on your system, execute

```bash
git clone https://github.com/csurfer/pyheat.git
cd pyheat && pip install -r requirements.txt
```

## Usage

To view heatmap of a python file use:
```bash
python pyheat --pyfile <path_to_python_file>
```
You can test it out using:
```bash
python pyheat --pyfile test_program.py # Provided in this repository.
```
To view help use:
```bash
python pyheat --help
```

## Contributing

### Bug Reports and Feature Requests
Please use [issue tracker](https://github.com/csurfer/pyheat/issues) for reporting bugs or feature requests.

### Development
Pull requests are most welcome.
