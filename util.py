import matplotlib.pyplot as plt

def read_file(f_name):
    f = open(f_name,"r")
    counts = []
    capitals = []
    for line in f:
        count, capital = line.replace("\r\n","").split(",")
        counts.append(count)
        capitals.append(capital)
    return counts, capitals


def plot(opt_name, b_name, a_name):
    counts, capitals = read_file(opt_name)
    a_counts, a_capitals = read_file(a_name)
    b_counts, b_capitals = read_file(b_name)

    plt.plot(a_counts, a_capitals)
    plt.plot(b_counts, b_capitals)
    plt.plot(counts, capitals)
    plt.show()