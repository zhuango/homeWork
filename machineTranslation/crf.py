# /usr/bin/python3

import numpy as np

class Sample():
    def __init__(self, data, seqLength, seqStates):
        self.seqLength = seqLength
        self.seqStates = seqStates
    
    # all 0-base.
    def getFeature(self, seqNum, y1State, y2State = None):
        pass

class CRF:
    def __init__(self, nodeFeatureSize, edgeFeatureSize, N, K):
        self.mWnode = np.random.uniform(-1, 1, nodeFeatureSize)
        self.mWedge = np.random.uniform(-1, 1, edgeFeatureSize)
        self.mObservationStateSize = N
        self.mLabelStateSize = K

    # def LogPotentials(self, nodeFeatures, edgeFeatures):
    #     sumNodeFeatures = np.sum(nodeFeatures, 1)
    #     sumedgeFeatures = np.sum(edgeFeatures, 1)
    #     nodeLogPotentials = np.dot(self.mWnode, sumNodeFeatures)
    #     edgeLogPotentials = np.dot(self.mWedge, sumedgeFeatures)
        
    #     return (nodeLogPotentials, edgeLogPotentials)

    # log distribution of the graph.
    def LogPotentialTable(self, sequence):
        seqLength = sequence.Length
        getFeature = sequence.GetFeature
        logPotential0 = np.zeros(self.mLabelStateSize)
        logPotentials = np.zeros((seqLength-1, self.mLabelStateSize, self.mLabelStateSize))

        for i in xrange(0, self.mLabelStateSize):
            logPotential0[i] = np.dot(self.mWnode, getFeature(0, i))

        for i in xrange(1, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                for k in xrange(0, self.mLabelStateSize):
                    logPotentials[i-1][j][k] = np.dot(self.mNode, getFeature(i, j)) + np.dot(self.mWedge, getFeature(i, j, k))
        
        return (logPotential0, logPotentials)
    
    def forward(self, logPotential0, logPotentials, seqLength):
        messages = np.zeros((seqLength, self.mLabelStateSize))
        messages[0] = logPotential0
        for i in xrange(1, seqLength):
            integralPotentials = np.exp(logPotentials[i-1]).sum(0)
            messages[i] = np.log(integralPotentials) + messages[i-1]
        return messages

    def backward(self, logPotentials, seqLength):
        messages = np.zeros((seqLength, self.mLabelStateSize))
        for i in reversed(xrange(seqLength-1, 0)):
            integralPotentials = np.exp(logPotentials[i+1]).sum(0)
            messages[i] = np.log(integralPotentials) + messages[i+1]

    def LogLikelihood(self, sequence):
        seqLength = sequence.Length
        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        messages = self.forward(logPotential0, logPotentials, seqLength)
        logNormalized = np.log(np.exp(messages[seqLength-1]).sum())

        logLikelihood = logPotential0[seqStates[0]]
        for i in xrange(1, seqLength):
            y1 = seqStates[i-1]
            y2 = seqStates[i]
            logLikelihood += logPotentials[i][y1][y2]
        logLikelihood -= logNormalized
        return logLikelihood

    def gradientOfNormalizedRespectW(self, sequence):
        seqLength  = sequence.Length
        getFeature = sequence.GetFeature
        
        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        forwardMessages  = self.forward(logPotential0, logPotentials, seqLength)
        backwardMessages = self.backward(logPotentials, seqLength)
        logNormalized    = np.log(np.exp(forwardMessages[seqLength-1]).sum())

        WnodeGradient = np.zeros_like(self.mWnode)
        WedgeGradient = np.zeros_like(self.mWedge)

        for i in xrange(0, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                WnodeGradient += numpy.exp(forwardMessages[i] + backwardMessages[i] - logNormalized) * getFeature(i, j)
        
        for i in xrange(1, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                for k in xrange(0, self.mLabelStateSize):
                    WnodeGradient += numpy.exp(forwardMessages[i]+ logPotentials[i] + backwardMessages[i] - logNormalized) * getFeature(i, j, k)

        return (WnodeGradient, WedgeGradient)

    def Sample(self, sequence):
        seqLength = sequence.Length
        getFeature = sequence.GetFeature

        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        labels = np.zeros(seqLength)

        pathMatrix = np.zeros((seqLength, self.mLabelStateSize))
        w = logPotential0
        for i in xrange(1, seqLength):
            w = logPotentials[i]+ numpy.reshape(w, (3, 1))
            pathMatrix[i] = w.argmax(0)
            w = w.max(0)
        labels[-1] = w.argmax()
        for i in reversed(xrange(0, seqLength - 1)):
            labels[i] = pathMatrix[i][labels[i + 1]]
        return labels

    def SGA(self, sequences ,iterations=20, a0=10, validate=None):
        rate = 0.1
        for i in xrange(0, len(sequences)):
            sequence   = sequences[i]
            getFeature = sequence.GetFeature
            
            (WnodeGradient, WedgeGradient) = self.gradientOfNormalizedRespectW(sequence)
            self.mWnode -= WnodeGradient * rate
            self.mWedge -= WedgeGradient * rate

            for j in xrange(0, sequence.Length):
                for k in xrange(0, self.mLabelStateSize):
                    self.mWnode += sequence.GetFeature(j, k) * rate

            for j in xrange(1, sequence.Length):
                for k in srange(0, self.mLabelStateSize):
                    for l in xrange(0, self.mLabelStateSize):
                        self.mWedge += sequence.GetFeature(j, k, l) * rate