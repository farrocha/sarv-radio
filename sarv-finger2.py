
import warnings
import json
import sys
warnings.filterwarnings("ignore")

from dejavu2 import Dejavu
from dejavu2.recognize import FileRecognizer, MicrophoneRecognizer


#load config from a JSON file (or anything outputting a python dictionary)
#with open("/home/sarv/Donwloads/dejavu/dejavu.cnf.SAMPLE") as f:
#   config = json.load(f)

print "parametros..."
for arg in sys.argv:
    print arg

archivo_mp3 = sys.argv[1]
archivo_destino = sys.argv[2]

print "Procesaremos " + archivo_mp3 + " y las huellas quedaran en " + archivo_destino

djv = Dejavu()
djv.fingerprint_file(archivo_mp3,archivo_destino,1000)




