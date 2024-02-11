<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="https://tse3.mm.bing.net/th/id/OIG4.HFlOnfv06WiEnWWrmTD8?pid=ImgGn" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Weighted Fair Queueing Implementation using Python</h3>

  <p align="center">
    A Queuing problem solver
    <br />
    <a href="linkedin.com/in/ali-fathi-vafegh-84bb0a274/">My Linkedin</a>
  </p>
</div>

# Description

This project is a simple implementation of Weighted Fair Queueing in Network Congestion Control for 'n' active flows using python.
WFQ is a network scheduling algorithm that assigns different weights to different flows of packets, and prioritizes them accordingly.
WFQ ensures fair access to network resources and enhances the quality of service.

## Tools

- Python 3.11

## Implementation

The code is divided into 2 scripts: **main** and **header**; which have the main run script and the functions respectfully.

> Each segment of code includes comments for better understanding

### Main script

The main script can be run in 2 ways:

- Running a demo example which is in respect of a figure demonstrated below.
- Running the script with pseudo-random variables

By having **demo_example** variable assigned to 1, we can run the example.

![Example Problem](https://github.com/ShamsAli-fathi/Weighted-Fair-Queueing-Implementation-using-Python/blob/main/DemoExample.png)

If not, we run our pseudo-random code.

```python
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
```

It is done by choosing a fixed number of flows and assigning a number range for **Arrival Time**, **Packet Length**, **Number of Packets in a Flow** and **Weight**; which then a random int number is chosen within this range.

The initialized _flow_list_ variable holds all the information of packets, including the flow they belong to. _finish_list_ on the other hand holds the final computed finish time for packets. This list is used for sorting later on.

## Header Script

All the functions are put in _Header Script_.

The very first function is to generate packets with the given specs.

```python
def packetGenerate(flow_id, arrival, length):
    packet = {"flow": flow_id, "arrival_time": arrival, "length": length}
    return packet
```

Packet's information is stored as a dictionary. These dictionaries are then appended to _flow_list_:

```python
flow_list[0].append(packetGenerate(1, 1, 1))
```

The following function is used in our demo example. It is worth mentioning that we can also manually fabricate our own example with definite numbers with this function.

```python
def demoExample()
```

The following function is for computing the finish time of each packet and sorting it afterwards.

```python
def calculateFinishTime(flow_list, finish_list, weight):

    for i in range(len(flow_list)):     # Loop through flow level
        finishTime = 0
        for j in range (len(flow_list[i])):     # Loop through each packet in a flow
            finishTime = max(finishTime, flow_list[i][j].get("arrival_time")) + flow_list[i][j].get("length") / weight[i]
            finish_list[i].append(finishTime)

    return orderPackets(flow_list, finish_list)

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
```

### Example Output

![Solution](https://github.com/ShamsAli-fathi/Weighted-Fair-Queueing-Implementation-using-Python/blob/main/DemoOutput.png)

## Acknowledgments/References

- [Advanced Network Course - S. H. Rastegar](https://www.linkedin.com/in/seyed-hamed-rastegar-2b2682ab/?originalSubdomain=ir)
