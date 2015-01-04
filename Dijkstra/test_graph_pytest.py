import unittest, mock

from Graph import Graph


class testGraph(unittest.TestCase):
  
    def setUp(self):
        self.graph = Graph()
    
    # @unittest.skip("jeszcze nie mamb")
    def testCreateSpecyficGraphFromFile(self):
        readFromFileMock = mock.Mock(return_value = """ 
            0 1 3\n
            0 4 3\n
            1 2 1\n
            2 3 3\n
            2 5 1\n
            3 1 3\n
            4 5 2\n
            5 3 1\n
            5 1 6""") #zakladanie werifikatora
        readFromFileMock("testGraf.txt") #gen
        readFromFileMock.assert_called_once_with("testGraf.txt") #sciaganie werifikatora
        self.graph.createGraphFromStr(readFromFileMock.return_value)
        self.assertEqual(6, self.graph.getNumberOfVertex())
        self.assertEqual(9, self.graph.getNumberOfEdges())

    # @unittest.skip("jeszcze nie mamb")
    def testAddEdge(self):
        s = [1, 2, 3]
        self.graph.addEdge(s)
        self.assertEqual([1], self.graph.getVertex())
        self.assertEqual([[2]], self.graph.getConnectFromVertex(1))
        self.assertEqual([3], self.graph.getEdgeFromVToVx(1, 2))


if __name__ == '__main__':
  unittest.main()
