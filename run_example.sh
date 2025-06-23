#!/usr/bin/env bash
set -Eeo pipefail


function show_help {
    echo """
================================================================

Run example app.

Usage:
    ./run_example.sh [options]

Options:
    -h | --help     shows this message.
    -s | --setup    setups database, runs db migrations.
    -a | --admin    setups app, creates initial super user.
    -r | --run      runs server

================================================================
"""
}


function gen_random_string {
    # This requires openssl installed > https://www.openssl.org/
    openssl rand -hex 32 | tr -d "\n"
}


# Generate a random secret key for the example app if missing
export DJANGO_SECRET_KEY="${DJANGO_SECRET_KEY:-$(gen_random_string)}"


action="no"
setup="no"
admin="no"
run="no"

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h | --help )
            show_help
            exit 0
        ;;

        -s | --setup )
            action="yes"
            setup="yes"
            shift
        ;;

        -a | --admin )
            action="yes"
            admin="yes"
            shift
        ;;

        -r | --run )
            action="yes"
            run="yes"
            shift
        ;;

        * )
            shift
        ;;
    esac
done


if [[ "${action}" == "no" ]]; then
    show_help
    exit 0
fi

if [[ "${setup}" == "yes" ]]; then
    python3 manage.py makemigrations
    python3 manage.py migrate
fi

if [[ "${admin}" == "yes" ]]; then
    python3 manage.py createsuperuser
fi

# Error: That port is already in use.
# sudo lsof -t -i tcp:8000 | xargs kill -9
if [[ "${run}" == "yes" ]]; then
    python3 manage.py runserver
fi
