# Date: Mar 24, 2020
# Author: Ishaat Chowdhury
# Contents: Downloads models used for voice recognition

#!/bin/bash
set -Eeuo pipefail

if [ ! -f deepspeech-0.6.1-models.tar.gz ]; then
    echo "Downloading Models..." 
    curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz 
fi

echo "Extracting Models..."
mkdir -p models
tar xvf deepspeech-0.6.1-models.tar.gz -C models --strip-components 1
