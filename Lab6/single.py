import threading 
import time

# Global variables for Queue, Data and parameters
task_queue = []
sortedData = []
totalTime = 0
idleTime = 0
# Flag check whether all items are produced
flag=False
# FinalFlag checks whether all the produced items are consumed
finalFlag=False
cumilativeDepartureTime = []
departureTime = []


# Producer funciton which takes in item from the extracted data and add it to the task queue when the arrival time equals the current time and sets busy time
def produce():
    global idleTime,task_queue,sortedData,totalTime,flag,finalFlag
    # initializing time = 0
    gTime = 0

    while(True):
        # if there is no item to be produced from the extracted data producer function exits
        if(not sortedData or len(sortedData)==0):
            flag=True
            return
        # if the arrival time of first item in the data is less than current time then it is added to the queue and removed from data
        if(gTime >= sortedData[0][0]):
            task_queue.append(sortedData[0])
            del sortedData[0]
        gTime+=1
        time.sleep(0.02)

#Consumer function consumes the items present in the task queue one by one when the time arrives and the server is not busy     
def consume():
    #initializing time,busytime and avg queue length
    gTime=0
    busyTime=0
    avgQueLength = 0
    global idleTime,task_queue,sortedData,totalTime,flag,finalFlag,departureTime,cumilativeDepartureTime
    
    while(True):
        avgQueLength += len(task_queue)
        # if the whole data is produced and all data is consumed as well print all the parameters and stop
        if(flag and len(task_queue)==0):
            finalFlag = True
            print("Idle Time = "+str(idleTime))
            print("Average Queue Length = "+str(avgQueLength*1.0/gTime))
            print("Departure Time = "+str(departureTime))
            print("Cumilative Departure Time = "+str(cumilativeDepartureTime))
            return
        # if task queue is not empty and if the first element in the queue is less than current time and if the server is not busy, the item is consumed
        if(len(task_queue)>0 and task_queue[0][0]<gTime and gTime>=busyTime):
            task = task_queue[0]
            busyTime = gTime + task[1]
            departureTime.append(gTime-1)
            if(len(cumilativeDepartureTime)!=0):
                cumilativeDepartureTime.append(departureTime[len(departureTime)-2]+gTime-1)
            else:
                cumilativeDepartureTime.append(gTime-1)
            print("Task Started at t = "+str(gTime-1)+ " and will be completed at t = "+str(busyTime-1))
            del task_queue[0]
        # at any point of time if busytime is less than current time, it means the server is not busy and the idle time is incremented
        if(gTime>=busyTime):
            idleTime+=1
        gTime+=1
        time.sleep(0.02)
  
if __name__ == "__main__": 
    global sortedData
    # extracting data from input file
    f = open("input.txt", "r")
    n = int(f.readline())
    data = []
    for i in range(n):
        line = f.readline()
        inp = line.split()
        d = []
        for item in inp:
            d.append(int(item))
        data.append(d)

    # converting inter-arrival time to arrival time    
    prev = 0
    for item in data:
        arrTime = prev + item[0]
        sortedData.append([arrTime,item[1]])
        prev = arrTime
    print("Data : "+str(sortedData))

    # creating threads for producer and consumer
    t1 = threading.Thread(target=produce) 
    t2 = threading.Thread(target=consume) 
    
    #executing threads
    t1.start() 
    t2.start() 