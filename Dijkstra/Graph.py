from FileManagement import FileManagement
import random


class Graph:
  
    vertex = {}

    def addEdge(self, line):
        vertexId = self.findVertex(line[0])
        firstVertex = line[vertexId]
        if self.findVertex(vertexId) == False:
            self.vertex[int(firstVertex)] = []
        self.vertex[(int(firstVertex))].append({int(line[1]) : int(line[2])})

    def findVertex(self, vertexId):
        if self.vertex.keys() == []:
            return False
        for i in range(len(self.vertex.keys())):
            if self.vertex.keys()[i] is vertexId and self.vertex.keys() is not []: 
                return i
            else:
                return False

    def createGraphFromStr(self, graphStr):
        graphList = graphStr.split()
        lineOfGraphTxt = []
        for i in graphList:
            if len(lineOfGraphTxt) < 3:
                lineOfGraphTxt.append(i)
            elif len(lineOfGraphTxt) >= 3:
                self.addEdge(lineOfGraphTxt)
                lineOfGraphTxt = []
                lineOfGraphTxt.append(i)
        return self.vertex.keys()

    def getNumberOfVertex(self):
        return len(self.vertex.keys())

    def getNumberOfEdges(self):
        retValue = 0
        for element in self.vertex.keys():
            retValue += len(element)
        return retValue

    def getVertex(self):
        return self.vertex.keys()

    def getConnectFromVertex(self, vertexId):
        # return self.vertex[vertexId].keys()
        retVal = []
        for elem in vertex[vertexId]:
            retVal.append()
        print(self.vertex[vertexId][0].keys())

    def getEdgeFromVToVx(self, v1, v2):
        return self.vertex[v1][v2]
