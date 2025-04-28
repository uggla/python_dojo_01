# About

This repository is designed for organizing a Python Craft Dojo — a
collaborative coding workshop where participants focus on improving their
programming skills through practice and discussion.

The goal of this dojo is not just to solve a problem, but to emphasize clean
code, good design practices, and refactoring techniques. The repository
provides:

    A simple Python exercise as a starting point.

    A structure for iteratively improving the solution during the session.

It’s meant to be a lightweight framework for running a craft dojo where
participants can learn, experiment, and share coding best practices in a
friendly environment.

# My presentations using reveal.js

## Organization

- Main branch contains the slides.
- Other branches contain the code evolution.

**Changes on slides must be done on the main branch.**

## Get and build presentations

1. Requirements

- git
- python3
- npm

2. Clone the repo with the sub modules (reveal.js).

```
git clone --recurse-submodules https://github.com/uggla/python_dojo_01
cd python_dojo_01/reveal.js
npm install
cd..
```

## Build the presentation with staticjinja (optional)

Run staticjinja within the `slides` directory: `uv tool run staticjinja build`.

Note: `uv tool run staticjinja watch` can be run and it will rebuild the presentation as soon as it will detect a change in the templates folder.

## Modify a presentation

Change the presentation .html file.

**Warning**, if **staticjinja** is used change the file **into the templates directory** not the one at the presentation root directory.

## Serve presentations

To serve the presentation locally, run:

```bash
./server.py
```

from the root of the project. Then, open your browser and navigate to [http://localhost:8000](http://localhost:8000).

The `server.py` script builds the presentation using **staticjinja** and serves it.

For live updates, use the `--watch` option:

```bash
./server.py --watch
```

This will rebuild the presentation automatically whenever changes are detected and continue serving it.
