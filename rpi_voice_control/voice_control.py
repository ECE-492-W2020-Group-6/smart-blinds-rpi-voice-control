"""
Date: Mar 17, 2020
Author: Ishaat Chowdhury
Contents: Voice Control Code for Raspberry Pi

Adapted from:
    - https://github.com/mozilla/DeepSpeech-examples/blob/r0.6/mic_vad_streaming/mic_vad_streaming.py
"""

import time, logging
from datetime import datetime
import os
import deepspeech
import numpy as np
from halo import Halo
from rpi_voice_control.audio.audio import VADAudio
from rpi_voice_control.voice_parser import VoiceParser
from rpi_voice_control.command.command_factory import CommandFactory
from rpi_voice_control.constants import *

logging.basicConfig(level=20)

def main(ARGS):
    # Load DeepSpeech model
    if os.path.isdir(ARGS.model):
        model_dir = ARGS.model
        ARGS.model = os.path.join(model_dir, 'output_graph.pb')
        ARGS.lm = os.path.join(model_dir, ARGS.lm)
        ARGS.trie = os.path.join(model_dir, ARGS.trie)

    print('Initializing model...')
    logging.info("ARGS.model: %s", ARGS.model)
    model = deepspeech.Model(ARGS.model, ARGS.beam_width)
    if ARGS.lm and ARGS.trie:
        logging.info("ARGS.lm: %s", ARGS.lm)
        logging.info("ARGS.trie: %s", ARGS.trie)
        model.enableDecoderWithLM(ARGS.lm, ARGS.trie, ARGS.lm_alpha, ARGS.lm_beta)

    # Start audio with VAD
    vad_audio = VADAudio(aggressiveness=ARGS.vad_aggressiveness,
                         device=ARGS.device,
                         input_rate=ARGS.rate,
                         file=ARGS.file)
    print("Listening (ctrl-C to exit)...")
    frames = vad_audio.vad_collector()

    # Stream from microphone to DeepSpeech using VAD
    spinner = None
    if not ARGS.nospinner:
        spinner = Halo(spinner='line')
    stream_context = model.createStream()
    wav_data = bytearray()
    for frame in frames:
        if frame is not None:
            if spinner: spinner.start()
            logging.debug("streaming frame")
            model.feedAudioContent(stream_context, np.frombuffer(frame, np.int16))
            if ARGS.savewav: wav_data.extend(frame)
        else:
            if spinner: spinner.stop()
            logging.debug("end utterence")
            if ARGS.savewav:
                vad_audio.write_wav(os.path.join(ARGS.savewav, datetime.now().strftime("savewav_%Y-%m-%d_%H-%M-%S_%f.wav")), wav_data)
                wav_data = bytearray()
            text = model.finishStream(stream_context).strip()
            parsed_text = VoiceParser.parse(text) 
            command = CommandFactory.build(parsed_text, ip=ARGS.ip, port=ARGS.port)
            print("-" * 80)
            print(f"Recognized: {text}")
            print(f"Parsed: {parsed_text}")
            print(f"Command: {command}")
            print("-" * 80)
            if command is not None:
                command.run()
            stream_context = model.createStream()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Stream from microphone to DeepSpeech using VAD")

    parser.add_argument('-v', '--vad_aggressiveness', type=int, default=3,
                        help="Set aggressiveness of VAD: an integer between 0 and 3, 0 being the least aggressive about filtering out non-speech, 3 the most aggressive. Default: 3")
    parser.add_argument('--nospinner', action='store_true',
                        help="Disable spinner")
    parser.add_argument('-w', '--savewav',
                        help="Save .wav files of utterences to given directory")
    parser.add_argument('-f', '--file',
                        help="Read from .wav file instead of microphone")
    parser.add_argument('-m', '--model', default=DEFAULT_MODEL_PATH,
                        help=f"Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)")
    parser.add_argument('-l', '--lm', default=DEFAULT_LM_PATH,
                        help=f"Path to the language model binary file. Default: {os.path.abspath(DEFAULT_LM_PATH)}")
    parser.add_argument('-t', '--trie', default=DEFAULT_TRIE_PATH,
                        help=f"Path to the language model trie file created with native_client/generate_trie. Default: {os.path.abspath(DEFAULT_TRIE_PATH)} ")
    parser.add_argument('-d', '--device', type=int, default=None,
                        help="Device input index (Int) as listed by pyaudio.PyAudio.get_device_info_by_index(). If not provided, falls back to PyAudio.get_default_device().")
    parser.add_argument('-r', '--rate', type=int, default=DEFAULT_SAMPLE_RATE,
                        help=f"Input device sample rate. Default: {DEFAULT_SAMPLE_RATE}. Your device may require 44100.")
    parser.add_argument('-la', '--lm_alpha', type=float, default=LM_ALPHA,
                        help=f"The alpha hyperparameter of the CTC decoder. Language Model weight. Default: {LM_ALPHA}")
    parser.add_argument('-lb', '--lm_beta', type=float, default=LM_BETA,
                        help=f"The beta hyperparameter of the CTC decoder. Word insertion bonus. Default: {LM_BETA}")
    parser.add_argument('-bw', '--beam_width', type=int, default=BEAM_WIDTH,
                        help=f"Beam width used in the CTC decoder when building candidate transcriptions. Default: {BEAM_WIDTH}")
    parser.add_argument('-p', '--port', type=int, default=DEFAULT_RPI_SERVER_PORT,
                        help=f"Port of RPI server. Default: {DEFAULT_RPI_SERVER_PORT}")
    parser.add_argument('-i', '--ip', type=str, default=DEFAULT_RPI_SERVER_IP,
                        help=f"IP address of RPI server. Default: {DEFAULT_RPI_SERVER_IP}")

    ARGS = parser.parse_args()
    if ARGS.savewav: os.makedirs(ARGS.savewav, exist_ok=True)
    main(ARGS)
