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
