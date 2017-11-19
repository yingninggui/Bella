from liblo import *

import sys
import time
import training
import ffn
import numpy as np

# muse-io --device Muse-509D --osc-eeg-urls osc.udp://localhost:5000

class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        self.__curr_song_type = 0
        self.__predictions = []
        self.__curr_activ = []
        self.__n_size = 300

        self.__net = ffn.Net([8, 70, 70, 9])
        wbfilename = "neuralnet.txt"
        w, b = training.read_net_from_file(wbfilename)
        training.set_net_weights_biases(self.__net, w, b)

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

        arr = np.array([l_ear, l_forehead, r_forehead, r_ear])
        self.__curr_activ.append(arr)
        if len(self.__curr_activ) == self.__n_size:
            inp = training.normalize(self.__curr_activ)
            inp = np.log(inp)
            inp = inp/10
            outp = training.get_out_ind(self.__net, inp)
            print(outp)
            self.__curr_song_type = outp
            self.__predictions.append(outp)
            self.__curr_activ =[]
        #print(self.__curr_song_type)
        #print("djakslfhkjsdfhkjsdhfksjdfhlskdjfhslkdjfhasldkjfhsldkjf")
        #print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)

    # This method gets the current prediction for the next song type without resetting variables
    #   should be used if not changing to next song
    def get_next_song_type (self):
        cnt = np.zeros(9)
        for x in self.__predictions:
            cnt[x]+=1
        ind = 0
        max = cnt[0]
        for x in range(1,9):
            if cnt[x] > max:
                max = cnt[x]
                ind = x
        return x

    # This method gets the prediction for the next song and resetting variables
    #   should be used if changing song
    def next_song (self):
        x = self.get_next_song_type()
        self.__curr_song_type=0
        self.__predictions = []
        self.__curr_activ = []

        return x

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
