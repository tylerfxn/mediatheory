#!/bin/zsh 

poetry run black .
poetry run ruff check .

