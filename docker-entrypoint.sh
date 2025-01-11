#!/bin/bash

poetry run task migrate
poetry run task start

exec "$@"
