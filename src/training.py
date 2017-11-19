import numpy as np
import ffn

generes = ["Blues", "Chill", "Classical", "Country", "EDM", "HipHop", "Pop", "Rock", "Romance"]
generes_vals = [[ 1,.7,.1,.4,.1, 0, 0,.2,.2],
                [.5, 1,.2,.3,.4,.2,.1, 0,.3],
                [.1,.2, 1,.2, 0, 0, 0, 0,.1],
                [.1,.3, 0, 1, 0, 0, 0,.2,.3],
                [.2, 0, 0, 0, 1,.7, 0,.2,.1],
                [.1,.2, 0,.4, 0, 1,.5,.2,.1],
                [.1,.3, 0,.2,.2,.4, 1, 0,.5],
                [.1, 0, 0,.1,.3,.1,.2, 1,.2],
                [.1,.2,.3,.3, 0, 0,.2, 0, 1]]
n_generes = len(generes)
generes_to_int = {g:i for i,g in enumerate(generes)}
int_to_generes = {i:g for i,g in enumerate(generes)}

# This method takes the average of n vectors
def vec_avg (vals):
    return np.mean(vals, axis=0)

# This method takes the standard deviation of n vectors, componentwise eg: stdev(a1, b1, ...), stdev(a2,...)...
def vec_std_dev (vals):
    return np.std(vals, axis=0)

# This method reads initial training data from a file
def read_data_from_file (filename):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    n_tests = int(contents[0])
    n_elements = int(contents[1])
    counter = 2
    data = np.zeros((n_tests, n_elements))
    for d in range(n_tests):
        for e in range(n_elements):
            data[d][e] = float(contents[counter])
            counter+=1
    return data

# This method reads the weights and biases of a neural network from a file
def read_net_from_file (filename):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    n_layers = int(contents[0])
    layer_sizes = []
    for x in range(n_layers):
        layer_sizes.append(int(contents[x+1]))

    counter = n_layers+1
    biases = [np.zeros(cl) for cl in layer_sizes[1:]]
    for x in range(1, n_layers):
        for y in range(layer_sizes[x]):
            biases[x-1][y] = float(contents[counter])
            counter+=1

    weights = [np.zeros((cl, pl)) for cl, pl in zip(layer_sizes[1:], layer_sizes[:-1])]
    for x in range(1, n_layers):
        for y in range(layer_sizes[x]):
            for z in range(layer_sizes[x-1]):
                weights[x-1][y][z] = float(contents[counter])
                counter+=1
    return (weights, biases)

# This method writes the weights and biases of a network into a file
def write_net_to_file (net, filename):
    file = open(filename, 'w')
    l_s = net.get_layer_sizes()
    file.write(str(len(l_s)))
    for x in l_s:
        file.write('\n' + str(x))
    b = net.get_biases()
    for x in b:
        for y in x:
            file.write('\n' + str(y))
    w = net.get_weights()
    for x in w:
        for y in x:
            for z in y:
                file.write('\n' + str(z))
    file.close()
    return "Success, wrote to " + filename

# This method takes the average of n vectors and the standard deviation of n vectors and puts them into one vector
def normalize (data, num):
    n_data = len(data)
    new_data = []
    for x in range(0, n_data, num):
        a = vec_avg(data[x:x+num])
        s = vec_std_dev(data[x:x+num])
        r = np.concatenate((a, s))
        new_data.append(r)
    return new_data

# This method sets the weights and biases for a feed forward neural network
def set_net_weights_biases (net, w, b):
    return net.set_weights_biases(w, b)

# This method performs stochastic gradient descent on a neural network
def perform_sgd (net, epochs, mini_batch_size, training_inputs, expected_outputs,
                                    step_size, lmbda = 0, test_input=None, test_output=None):
    net.stochastic_gradient_descent(epochs, mini_batch_size, training_inputs, expected_outputs,
                                    step_size, lmbda, test_input=None, test_output=None)

def to_one_hot (ind, length):
    a = np.zeros(length)
    a[ind] = 1
    return a

# This file returns a 2-tuple (data, expected)
def get_data (generes, generes_to_int):
    dir = '/home/max/Documents/Hackathons/HW4/Bella/training_data/MuseTraining/data/'
    flnm = ''
    data = []
    exp = []
    for x in generes:
        flnm = x + '_'
        for y in range(1,2):
            fl = flnm + str(y) + '_'
            for z in range(10):
                f = fl + str(z) + '.txt'
                d = normalize(read_data_from_file(dir+f), 300)
                for r in d:
                    data.append(r)
                    exp.append(np.array(generes_vals[generes_to_int[x]]))
    return data, exp

# This method returns the index of the highest activation from the outputs of a neural network given an input = inp
def get_out_ind (net, inp):
    out = net.feed_forward(inp)
    max = out[0]
    ind = 0
    for i, x in enumerate(out[1:]):
        if x > max:
            max = x
            ind = i
    return i

def update_net_set (setfilename, netfilename):
    file = open(netfilename, 'r')
    contents = file.read().splitlines()
    n_g = int(contents[0])
    if n_g==0:
        return "none"
    n_e = int(contents[1])
    n_c = np.zeros(n_g)
    counter = 2
    for x in range(n_g):
        n_c[x] = int(contents[counter])
        counter += 1
    data = []
    exp = []

    for x in n_c:
        for y in range(x):
            arr = np.zeros(n_e)
            for z in range(n_e):
                arr[z] = float(contents[counter])
                counter+=1
            data.append(arr)
            exp.append(to_one_hot(x, n_g))

    file.close()
    perform_sgd(net, 3, (int)(sum(n_c)/10), data, exp, .05, 0.001)
    write_net_to_file(netfilename)

# This method updates the data set in which the network can train on
def update_data_set (filename, new_data, song_ind):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    n_g = int(contents[0])
    if n_g == 0:
        return "none"
    n_e = int(contents[1])
    n_c = np.zeros(n_g)
    counter = 2
    for x in range(n_g):
        n_c[x] = int(contents[counter])
        counter += 1
    data = []

    for x in n_c:
        for y in range(x):
            arr = np.zeros(n_e)
            for z in range(n_e):
                arr[z] = float(contents[counter])
                counter+=1
            data.append(arr)

    for x in range(n_c[song_ind]-1):
        data[song_ind][x] = data[song_ind][x+1]

    data[song_ind][n_c[song_ind]-1] = new_data
    file.close()

    file = open(filename, 'w')
    file.write(str(n_g))
    file.write('\n' + str(n_e))
    for x in n_c:
        file.write('\n' + str(x))
    for d in data:
        for x in d:
            file.write('\n' + str(x))
    file.close()
    return "Wrote successfully"


net = ffn.Net([8, 70, 70, 9])
#w, b = read_net_from_file("neuralnet.txt")
#set_net_weights_biases(net, w, b)

data, exp = get_data(generes, generes_to_int)

for i, x in enumerate(data):
    data[i] = np.log(x)
    data[i] = data[i]/10


net.stochastic_gradient_descent(1000, 100, data, exp, 1, 0)
net.stochastic_gradient_descent(1000, 100, data, exp, .05, 0)
net.stochastic_gradient_descent(5000, 100, data, exp, .002, 0)

print(write_net_to_file(net, "neuralnet2.txt"))