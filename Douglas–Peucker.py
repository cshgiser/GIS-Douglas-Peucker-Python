import math

class Douglas_Peucker:
    REMOVETAG = []
    def __init__(self, demical):
        self.demical = demical

    def getResult(self, line):
        self.compressLine(line)
        return [line[i] for i in range(len(line)) if line[i] not in self.REMOVETAG]

    def compressLine(self, line):
        if len(line) == 2:
            return
        startP = line[0]
        endP = line[-1]

        A, B, C = self.getParams(startP, endP)

        maxD = -1
        maxIndex = 0
        for i in range(1, len(line) - 1):
            dist = self.distance_point2line(A, B, C, line[i])
            if dist > maxD:
                maxD = dist
                maxIndex = i

        if maxD < self.demical:
            for i in range(1, len(line) - 1):
                self.REMOVETAG.append(line[i])
            # compressLine([startP, endP], demical)
        else:
            self.compressLine(line[: maxIndex + 1])
            self.compressLine(line[maxIndex:])

    def distance_point2line(self, A, B, C, point):
        x0 = point[0]
        y0 = point[1]
        return math.fabs(A * x0 + B * y0 + C) / math.sqrt(A ** 2 + B ** 2)

    def getParams(self, startP, endP):
        if endP[0] - startP[0] == 0:  # 垂线
            return -1, 0, startP[0]
        else:
            k = (endP[1] - startP[1]) / (endP[0] - startP[0])
            A = k
            B = -1
            C = startP[1] - A * startP[0]
        return A, B, C


if __name__=='__main__':
    """"""
    line = [[2,2], [2, 5], [4, 5], [2, 10], [8, 9], [2, 16], [5, 17], [4, 18], [11, 16], [8, 19]]
    dp = Douglas_Peucker(2.5)
    print(dp.getResult(line))
