Advent of Code 2019
---
[![Build Status](https://github.com/gumballhead/aoc2019/workflows/build/badge.svg)](https://github.com/gumballhead/aoc2019/actions)
[![Coverage Status](https://coveralls.io/repos/github/gumballhead/aoc2019/badge.svg?branch=master)](https://coveralls.io/github/gumballhead/aoc2019?branch=master)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

Solutions to [Advent of Code 2019](https://adventofcode.com/2019).

### Setup
You'll need to [install pipenv](https://github.com/pypa/pipenv#installation) to run the code.

To activate the git hooks:
```bash
git config core.hooksPath .githooks
```

If you want to use the [init](bin/init) and [instructions](bin/instructions) scripts, you should set the `AOC_SESSION_TOKEN` environment variable to the session token in your [adventofcode.com](https://adventofcode.com) cookie.

Though not required, it's handy to use [direnv](https://direnv.net/) to set your session token and add the scripts in `bin` to your `PATH` so you can run them directly, eg: `tests`.

To do so, add an `.envrc` file to the project root:
```bash
export PATH=./bin:$PATH
export AOC_SESSION_TOKEN="your session token"
```

The `bin/init` script will automatically create an `.envrc` within each solution.


### Commands
```bash
# Run and verify all solutions
bin/solutions

# Run all unit tests with coverage
bin/tests

# Lint project code
bin/lint

# Initialize solution for first day
bin/init day1
```
