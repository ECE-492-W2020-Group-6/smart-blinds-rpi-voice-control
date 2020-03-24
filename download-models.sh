# Date: Mar 24, 2020
# Author: Ishaat Chowdhury
# Contents: Downloads models used for voice recognition

#!/bin/bash
set -Eeuo pipefail

# Download archive of models
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz 

# Extract archive of models
mkdir models
tar xvf deepspeech-0.6.1-models.tar.gz -C models/
