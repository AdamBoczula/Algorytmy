from FileManagement import FileManagement
import random


class Graph:
  
    vertex = {}


    def addEdge(self, line):
        try:
            self.vertex[int(line[0])].append({int(line[1]) : int(line[2])})
        except KeyError:
            self.vertex[int(line[0])] = [{int(line[1]) : int(line[2])}]


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
        retVal = 0
        for elem in self.vertex.values():
            retVal += len(elem)
        return retVal


    def getVertex(self):
        return self.vertex.keys()


    def getConnectFromVertex(self, vertexId):
        retVal = []
        for elem in self.vertex[vertexId]:
            retVal.append(elem.keys())
        return retVal


    def getEdgeFromVToVx(self, v1, v2): 
        matches = [ x for x in self.vertex[v1] if [v2] == x.keys() ]
        return matches[0].values()
