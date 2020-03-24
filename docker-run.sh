# Date: Mar 17, 2020
# Author: Ishaat Chowdhury
# Contents: bash script to run docker container

# Get common definitions
source common.sh

# Run image in daemon mode
# Give contianer access to host's audio devices
docker run -p 5000:5000 -it -d --name $CONTAINER_NAME --privileged --group-add=audio -v /dev/snd/:/dev/snd/ $RPI_IMAGE
