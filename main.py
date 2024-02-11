import header
import copy
import random

if __name__ == '__main__':

    # if demo_example is 1, this script will run the solution for a given demo example
    # If 0, it generates packets with random specs
    demo_example = 1


    if demo_example == 0:
        flow_list = []
        weight = []

        # Number of flows
        numberOfFlows = 4
        for i in range(numberOfFlows):
            flow_list.append([])
        finish_list = copy.deepcopy(flow_list)

        ### Define Specs for packets
        arrivalTime_range = (1,20)      # (lower, upper) range
        length_range = (1,10)
        numberOfPacketsPerFlow = (2,4)      # determines number of packets that exist in each flow
        weight_range = (1,2)

        ### Create flows with packets
        for i in range(len(flow_list)):
            weight.append(random.randint(weight_range[0], weight_range[1]+1))
            for j in range(random.randint(numberOfPacketsPerFlow[0], numberOfPacketsPerFlow[1]+1)):
                flow_list[0].append(header.packetGenerate(
                    i,
                    random.randint(arrivalTime_range[0], arrivalTime_range[1]+1),
                    random.randint(length_range[0], length_range[1]+1)
                ))

        sortedFinish_list, sortedFlow_list = header.calculateFinishTime(flow_list, finish_list, weight)

    else:
        weight = [1, 1, 2]

        flow_list, finish_list = header.demoExample()
        sortedFinish_list, sortedFlow_list = header.calculateFinishTime(flow_list, finish_list, weight)

    print("Sorted Packets:\n")
    for x in range(len(sortedFinish_list)):
        print(sortedFlow_list[x], "   Finish Time: ", sortedFinish_list[x])