import copy
import itertools

"""
This function generates a packet with assigned arrival time and its length and the flow it belongs to. 
"""
def packetGenerate(flow_id, arrival, length):
    packet = {"flow": flow_id, "arrival_time": arrival, "length": length}
    return packet

"""
This function specifically generates a set of packets for the demo example.
It can be changed manually to fabricate another example with different number of flows and packets. 
"""
def demoExample():
    flow_list = [[], [], []]        # shows the number of flows
    finish_list = copy.deepcopy(flow_list)      # copies the object but not the reference

    # Any number of packets for different flows can be generated.
    # ( Flow_id, arrival_time, length )

    flow_list[0].append(packetGenerate(0, 0, 8))
    flow_list[0].append(packetGenerate(0, 10, 6))
    flow_list[1].append(packetGenerate(1, 5, 6))
    flow_list[1].append(packetGenerate(1, 8, 9))
    flow_list[1].append(packetGenerate(1, 20, 8))
    flow_list[2].append(packetGenerate(2, 5, 10))
    flow_list[2].append(packetGenerate(2, 8, 8))
    flow_list[2].append(packetGenerate(2, 11, 10))

    return flow_list, finish_list

"""
This function computes the finish time of packets in respect to the flows they belong to while also calling the sorting function.
"""
def calculateFinishTime(flow_list, finish_list, weight):

    for i in range(len(flow_list)):     # Loop through flow level
        finishTime = 0
        for j in range (len(flow_list[i])):     # Loop through each packet in a flow
            finishTime = max(finishTime, flow_list[i][j].get("arrival_time")) + flow_list[i][j].get("length") / weight[i]
            finish_list[i].append(finishTime)

    return orderPackets(flow_list, finish_list)

"""
This functions sorts our packets.
"""
def orderPackets(flow_list, finish_list):
    flow_list = list(itertools.chain(*flow_list))      # flattens a nested array
    finish_list = itertools.chain(*finish_list)

    ### Sorts the finish_list while logging the changes in index order
    temp = list(enumerate(finish_list))
    temp.sort(key=lambda t: t[1])
    indexOrder_list = [t[0] for t in temp]
    sortedFinish_list = [t[1] for t in temp]
    ###

    sortedFlow_list = [list(flow_list)[i] for i in indexOrder_list]     #sorts flow_list with the given index order ( indexOrder_list )
    return sortedFinish_list, sortedFlow_list

