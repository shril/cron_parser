# Technical Task - Cron Expression Parser

### Requirements

Write a command line application or script which parses a cron string and expands each field to show the times at which it will run.
You should only consider the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command, and you do not need to handle the special time strings such as "@yearly". The input will be on a single line.

The cron string will be passed to your application as a single argument.
```bash
$ your-program "d"
```

### Setup

1. Install Python 3.10+ locally using Anaconda or other distributions.
2. Install `virtualenv` using pip.
   - `pip install virtualenv`
3. Create a virtual environment named, `cron-env`
   - `python -m venv cron-env`
4. Activate `cron-env` environment.
   - `source cron-env/bin/activate`
5. Install libraries in `requirements.txt`.
   - `pip install -r requirements.txt`

### Running

To run the program, follow the commands below

```bash
cd src/cron_parser/
python main.py "*/15 0 1,2,3,15 */2 1-5 /usr/bin/find"
```

### Testing

To test the library, from the root folder run

```bash
pytest
```

