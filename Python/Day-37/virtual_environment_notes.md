# Virtual Environments in Python

## What is a Virtual Environment?

A virtual environment is an isolated, self-contained directory that holds a
specific Python interpreter along with its own set of installed packages,
separate from the system-wide Python installation and from any other
project's environment. When a virtual environment is active, commands like
`python` and `pip` operate only within that isolated space instead of
affecting the global Python setup.

## Why It Is Useful

- **Dependency isolation** — Each project can have its own package versions
  without conflicting with other projects on the same machine.
- **Avoids version conflicts** — Project A might need `requests==2.20` while
  Project B needs `requests==2.31`. Virtual environments let both coexist.
- **Reproducibility** — Combined with `requirements.txt`, anyone can recreate
  the exact same environment on another machine.
- **Clean system Python** — Prevents cluttering or breaking the global/system
  Python installation with project-specific packages.
- **Safe experimentation** — Packages can be installed, upgraded, or removed
  without risk, and the whole environment can simply be deleted and
  recreated if something goes wrong.

## How to Create One

```bash
python -m venv venv
```

This creates a new folder named `venv` (the name is customizable) containing
a copy/link of the Python interpreter and a fresh, empty set of packages.

## How to Activate It

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Once activated, the terminal prompt usually shows the environment name (e.g.
`(venv)`) to indicate it is active.

## How to Deactivate It

```bash
deactivate
```

This works the same way on all platforms and returns the terminal to using
the system Python.

## How to Install Packages

With the virtual environment activated, use `pip` as usual:

```bash
pip install requests
```

The package is installed only inside the active virtual environment.

## How to Generate a `requirements.txt`

To capture all currently installed packages (and their versions) in the
environment:

```bash
pip freeze > requirements.txt
```

This file lists every installed package, e.g.:

```
requests==2.31.0
certifi==2024.2.2
```

## How to Install Dependencies From It

On a new machine or a fresh environment, install everything listed in
`requirements.txt` in one step:

```bash
pip install -r requirements.txt
```

## Why Every Professional Python Project Should Use Virtual Environments

- Keeps project dependencies isolated and conflict-free.
- Makes projects portable and reproducible across different machines and
  environments (dev, staging, production).
- Enables collaborators to set up the exact same environment quickly via
  `requirements.txt`.
- Prevents "it works on my machine" issues caused by mismatched package
  versions.
- Considered a standard best practice in professional Python development and
  expected in any serious codebase.
