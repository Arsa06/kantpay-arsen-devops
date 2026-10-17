#!/bin/bash

if [ -f information.txt ]; then
    echo "Information file exists."
    cat information.txt
else
    echo "Information file does not exist."
fi

