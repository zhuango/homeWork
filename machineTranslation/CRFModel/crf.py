# /usr/bin/python3

import numpy as np
from collections import defaultdict

class Sample(object):
    LabelTable = {}
    WordsTable = defaultdict(lambda:np.zeros(50))
    def __init__(self, s, labels=None):
        self.sequence = list(s)
        self.Labels = labels
        self.Length = len(s)

    def GetFeature(self, seqNum, y1State, y2State = None):
        """ Create the vector of active indicies for this label setting. """
        # label-label-token; bigram features
        #for f in self.sequence[t].attributes:
        #    yield '[%s,%s,%s]' % (yp,y,f)
        # label-token; emission features
        word0  = self.sequence[seqNum]
        label0 = self.LabelTable[y1State]

        if y2State != None:
            word1  = self.sequence[seqNum-1]
            label1 = Sample.LabelTable[y2State]
            f0 = 1 if label0 == 'a' and label1 == 'n' else 0
            f1 = 1 if label0 == 'p' and label1 == 'p' else 0
            feature = np.append(Sample.WordsTable[word0] - Sample.WordsTable[word1], [f0, f1])
            return feature
        else:
            feature = Sample.WordsTable[word0]
            return feature
            

class CRF:
    def __init__(self, nodeFeatureSize, edgeFeatureSize, labelStateSize):
        self.mWnode = np.random.uniform(0, 1, nodeFeatureSize)
        self.mWedge = np.random.uniform(0, 1, edgeFeatureSize)
        self.mLabelStateSize = labelStateSize

    # def LogPotentials(self, nodeFeatures, edgeFeatures):
    #     sumNodeFeatures = np.sum(nodeFeatures, 1)
    #     sumedgeFeatures = np.sum(edgeFeatures, 1)
    #     nodeLogPotentials = np.dot(self.mWnode, sumNodeFeatures)
    #     edgeLogPotentials = np.dot(self.mWedge, sumedgeFeatures)
        
    #     return (nodeLogPotentials, edgeLogPotentials)

    # log distribution of the graph.
    def LogPotentialTable(self, sequence):
        seqLength = sequence.Length
        logPotential0 = np.zeros(self.mLabelStateSize)
        logPotentials = np.zeros((seqLength-1, self.mLabelStateSize, self.mLabelStateSize))

        for i in xrange(0, self.mLabelStateSize):
            logPotential0[i] = np.dot(self.mWnode, sequence.GetFeature(0, i))

        for i in xrange(1, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                for k in xrange(0, self.mLabelStateSize):
                    node = np.dot(self.mWnode, sequence.GetFeature(i, j))
                    edge = np.dot(self.mWedge, sequence.GetFeature(i, j, k))
                    logPotentials[i-1][j][k] = node + edge
        
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
            integralPotentials = np.exp(logPotentials[i]).sum(0)
            messages[i] = np.log(integralPotentials) + messages[i+1]
        return messages

    def LogLikelihood(self, sequence):
        seqLength = sequence.Length
        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        messages = self.forward(logPotential0, logPotentials, seqLength)
        logNormalized = np.log(np.exp(messages[seqLength-1]).sum())

        logLikelihood = logPotential0[seqStates[0]]
        for i in xrange(1, seqLength):
            y1 = seqStates[i-1]
            y2 = seqStates[i]
            logLikelihood += logPotentials[i-1][y1][y2]
        logLikelihood -= logNormalized
        return logLikelihood

    def gradientOfNormalizedRespectW(self, sequence):
        seqLength  = sequence.Length
        
        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        forwardMessages  = self.forward(logPotential0, logPotentials, seqLength)
        backwardMessages = self.backward(logPotentials, seqLength)
        logNormalized    = np.log(np.exp(forwardMessages[seqLength-1]).sum())

        WnodeGradient = np.zeros_like(self.mWnode)
        WedgeGradient = np.zeros_like(self.mWedge)

        for i in xrange(0, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                WnodeGradient += np.exp(forwardMessages[i][j] + backwardMessages[i][j] - logNormalized) * sequence.GetFeature(i, j)

        for i in xrange(1, seqLength):
            for j in xrange(0, self.mLabelStateSize):
                for k in xrange(0, self.mLabelStateSize):
                    WedgeGradient += np.exp(forwardMessages[i-1][j] + logPotentials[i-1][j][k] + backwardMessages[i][k] - logNormalized) * sequence.GetFeature(i, j, k)

        return (WnodeGradient, WedgeGradient)

    def Sample(self, sequence):
        seqLength = sequence.Length
        sequence.GetFeature = sequence.sequence.GetFeature

        (logPotential0, logPotentials) = self.LogPotentialTable(sequence)
        labels = np.zeros(seqLength)

        pathMatrix = np.zeros((seqLength, self.mLabelStateSize))
        w = logPotential0
        for i in xrange(1, seqLength):
            w = logPotentials[i]+ np.reshape(w, (3, 1))
            pathMatrix[i] = w.argmax(0)
            w = w.max(0)
        labels[-1] = w.argmax()
        for i in reversed(xrange(0, seqLength - 1)):
            labels[i] = pathMatrix[i][labels[i + 1]]
        return labels

    def SGA(self, sequences ,iterations=20, a0=10, validate=None):
        rate = 0.1
        for iter in xrange(0, iterations):
            print("Iteration: " + str(iter))
            for i in xrange(0, len(sequences)):
                sequence   = sequences[i]
                (WnodeGradient, WedgeGradient) = self.gradientOfNormalizedRespectW(sequence)
                self.mWnode -= WnodeGradient * rate
                self.mWedge -= WedgeGradient * rate

                for j in xrange(0, sequence.Length):
                    for k in xrange(0, self.mLabelStateSize):
                        self.mWnode += sequence.GetFeature(j, k) * rate

                for j in xrange(1, sequence.Length):
                    for k in xrange(0, self.mLabelStateSize):
                        for l in xrange(0, self.mLabelStateSize):
                            self.mWedge += sequence.GetFeature(j, k, l) * rate