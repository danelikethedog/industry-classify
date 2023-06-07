# Industry Classification

## Setup

Install the following

* Python3: https://www.python.org/downloads/

In this directory, run the following:

```bash
# Creates a virtual environment to keep python dependencies to this project only (avoids clashing)
python3 -m venv .env
source .env/bin/activate

# Install the necessary packages
pip3 install torch torchvision torchaudio
pip3 install transformers
```

## Run the Code

```bash
python3 ./classify.py
```
