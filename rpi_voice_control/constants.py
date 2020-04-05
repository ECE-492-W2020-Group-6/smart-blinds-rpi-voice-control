import os

BEAM_WIDTH = 500
DEFAULT_SAMPLE_RATE = 44100
LM_ALPHA = 0.75
LM_BETA = 1.85

dir_path = os.path.dirname(os.path.realpath(__file__))
DEFAULT_MODEL_PATH = os.path.join(dir_path, "../models/output_graph.tflite")
DEFAULT_LM_PATH = os.path.join(dir_path, "../models/lm.binary")
DEFAULT_TRIE_PATH = os.path.join(dir_path, "../models/trie")
DEFAULT_RPI_SERVER_PORT = 5000
DEFAULT_RPI_SERVER_IP = "127.0.0.1"
