Advent of Code 2019
---
[![Build Status](https://github.com/gumballhead/aoc2019/workflows/build/badge.svg)](https://github.com/gumballhead/aoc2019/actions)
[![Coverage Status](https://coveralls.io/repos/github/gumballhead/aoc2019/badge.svg?branch=HEAD)](https://coveralls.io/github/gumballhead/aoc2019?branch=HEAD)
[![Python Version](https://img.shields.io/github/pipenv/locked/python-version/gumballhead/aoc2019)](https://www.python.org/)

Solutions to [Advent of Code 2019](https://adventofcode.com/2019).

### Setup
You'll need to [install pipenv](https://github.com/pypa/pipenv#installation) to run the code.

Though not required, it's handy to use [direnv](https://direnv.net/) to add the scripts in `bin` to your `PATH`, so you can run them directly, eg: `tests`.

To do so, add an `.envrc` file to the project root:

```bash
PATH=./bin:$PATH
AOC_SESSION_TOKEN="get your session token from the adventofcode.com cookie"
```

The `bin/init` script will automatically create an `.envrc` within each puzzle solution.


### Commands
```bash
# Run and verify all solutions
bin/solutions

# Run all unit tests with coverage
bin/tests

# Lint project code
bin/lint

# Initialize a puzzle for day 4
# You must set AOC_SESSION_TOKEN to download the puzzle input.
bin/init day4
```
