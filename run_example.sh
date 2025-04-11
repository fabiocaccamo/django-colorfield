#!/usr/bin/env bash
set -Eeo pipefail

source venv/bin/activate


function show_help {
    echo """
    ================================================================

    Run example app.

    Usage:
        ./run_example.sh [options]

    Options:
        -h | --help         shows this message.
        -s | --setup        setups database, runs db migrations.
        -a | --admin        setups app, creates initial super user.
        -r | --run          runs server

    ================================================================
    """
}


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
            setup="yes"
            shift
        ;;

        -a | --admin )
            admin="yes"
            shift
        ;;

        -r | --run )
            run="yes"
            shift
        ;;

        * )
            shift
        ;;
    esac
done


if [[ "${setup}" == "yes" ]]; then
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
