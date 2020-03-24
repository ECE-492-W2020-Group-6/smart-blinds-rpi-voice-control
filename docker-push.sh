# Date: Mar 17, 2020
# Author: Ishaat Chowdhury
# Contents: bash script to push docker images to DockerHub
# Source common definitions
source common.sh

# Push images to registry
docker push $PRE_BUILD_STAGE_IMAGE
docker push $BUILD_STAGE_IMAGE
docker push $RPI_IMAGE
