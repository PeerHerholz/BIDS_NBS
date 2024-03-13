#Generate Dockerfile.

#!/bin/sh

 set -e

generate_docker() {
  docker run --rm kaczmarj/neurodocker:0.7.0 generate docker \
             --base ubuntu:22.04 \
             --pkg-manager apt \
             --arg DEBIAN_FRONTEND=noninteractive \
             --miniconda \
               version=latest \
               conda_install="python=3.10" \
               pip_install="pandas seedir pybids" \
               create_env='bidsnbs' \
               activate=true \
            --copy . /home/bidsnbs \
            --run-bash "source activate bidsnbs && cd /home/bidsnbs && pip install -e ." \
            --env IS_DOCKER=1 \
            --workdir '/tmp/' \
            --entrypoint "/neurodocker/startup.sh  bidsnbs"
}

# generate files
generate_docker > Dockerfile

# check if images should be build locally or not
if [ $1 = local ]; then
    echo "docker image will be build locally"
    # build image using the saved files
    docker build -t bidsnbs:local .
else
  echo "Image(s) won't be build locally."
fi            


