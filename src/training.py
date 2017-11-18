import ffn
import numpy as np
import random

def vec_avg (vals):
    return np.mean(vals, axis=0)

def vec_std_dev (vals):
    return np.std(vals, axis=0)

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

def read_net_from_file (filename):
    file = open(filename, 'r')
    contents = file.read().splitlines()
    n_layers = int(contents[0])
    layer_sizes = []
    for x in range(n_layers):
        layer_sizes.append(float(contents[x+1]))

    counter = n_layers
    biases = [np.zeros(cl) for cl in layer_sizes[1:]]
    for x in layer_sizes[1:]:
        for y in layer_sizes[:-1]:
            biases[x][y] = contents[counter]
            counter+=1

    weights = [np.zeros((cl, pl)) for cl, pl in zip(layer_sizes[1:], layer_sizes[:-1])]
    for x in range(1, n_layers):
        for y in range(layer_sizes[x]):
            for z in range(layer_sizes[x-1]):
                weights[x][y][z] = float(contents[counter])
                counter+=1
    return (weights, biases)

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



def normalize (data, num):
    n_data = len(data)
    random.shuffle(data)
    new_data = []
    for x in range(0, n_data, num):
        a = vec_avg(data[x:x+num])
        s = vec_std_dev(data[x:x+num])
        r = np.concatenate((a, s))
        new_data.append(r)
    return new_data

net = ffn.Net([8, 50, 50, 9])
generes = ["Blues", "Chill", "Classical", "Country", "Eletronic/Dance", "Hip-Hop", "Pop", "Rock", "Romance"]
generes_to_int = {g:i for i,g in enumerate(generes)}
int_to_generes = {i:g for i,g in enumerate(generes)}

print(normalize([[1,0],[0,3],[5,11]], 3))

