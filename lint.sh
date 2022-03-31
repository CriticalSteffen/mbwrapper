#!/bin/bash

paths="mbwrapper tests setup.py"
isort $paths
black -l 79 $paths
pycodestyle $paths
pydocstyle $paths
for p in $(echo $paths); do
    pylint $p
done