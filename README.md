This repository contains code for voice control for the smart blinds capstone project.

# Setup
### Install System Dependencies

`sudo apt install -y git build-essential libatlas3-base libgfortran5 portaudio19-dev python3-dev`

### Install Application Dependencies

`pip3 install -r requirements.txt`

### Download Models

`./download-models.sh`

### Install Docker Buildx (optional)

Install docker buildx if needing to build/run tests using docker.

# Usage
### Running Natively on Host OS
To run the voice control script:

`python3 src/voice_control.py`

### Running Using Docker

#### Build Docker Image

`./docker-build.sh`

#### Run Voice Control Script

Note: this doesn't work properly since docker container doesn't recognize microphone

`./docker-run.sh`

To see output:

`docker logs --follow rpi-voice-control`

To run an interactive container as other container runs for debugging:

`./docker-run-interactive.sh`

#### Kill Container

`./docker-kill.sh`

#### Push image to Docker (optional)

This script should usually only be run the CI/CD system.

`./docker-push.sh`

Note: requires you to run `docker login` before you run this script.
