#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    localnetMeans = (20,35,30,35) # LAN length of outage (mins)
    wanMeans = (25, 32, 34, 20) # WAN length of outage (min)
    ind = np.arange(N) # the x locations for the groups
    width = 0.35 # the width of the bars: can also be len(x) sequence

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary boii")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4",))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # display the graph 
    # uncomment the below line if you have a gui
    # plt.show()
    plt.savefig("/home/student/mycode/graphing/2018summary.png")

if __name__ == "__main__":
    main()
