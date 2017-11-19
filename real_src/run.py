from liblo import *

import sys
import time
import training
import ffn

# muse-io --device Muse-509D --osc-eeg-urls osc.udp://localhost:5000

class MuseServer(ServerThread):
    curr_type =0
    curr_activ =[]
    n_size = 300
    net = #MAKE NEW NET
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

    #receive accelrometer data
    @make_method('/muse/acc', 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        print "%s %f %f %f" % (path, acc_x, acc_y, acc_z)

    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        arr = [l_ear, l_forehead,r_forehead,r_ear]
        curr_activ.append(arr)
        if len(curr_activ) == n_size:
            inp = training.normalize(curr_activ)
            outp = tranining.get_out_ind(inp)
            curr_type = outp
            curr_activ =[]
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    #handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print "Unknown message \
        \n\t Source: '%s' \
        \n\t Address: '%s' \
        \n\t Types: '%s ' \
        \n\t Payload: '%s'" \
        % (src.url, path, types, args)

try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
