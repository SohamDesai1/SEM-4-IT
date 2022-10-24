import math

class MyMathLibrary:

    @staticmethod
    def calculateEuclideanDistance(x1, x2, y1, y2):
        xMinus = x2 - x1
        yMinus = y2 - y1
        internalCalc = xMinus**2 + yMinus**2
        euclidDistance = math.sqrt(internalCalc)
        return euclidDistance