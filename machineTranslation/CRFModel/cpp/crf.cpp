#pragma once

#include <iostream>
#include <string>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

namespace CRFModel
{
    const int InvalidState = -1;
    typedef vector<int> VectorInt;
    typedef Vector<double> Vector;
    typedef std::auto_ptr<VectorInt > SmartVectorIntPointer;
    typedef Vector<Vector<double> > Matrix;

    class Sample
    {
        public:
            static map<string, int> LabelTable;
            static map<string, int> WordsTable;

            const vector<string> * const Sequence;
            const vector<int> *    const Labels;
            bool isDisposed = false;
            
            Sample(vector<string> *s, VectorInt *labels)
            :Sequence(s), Labels(labels)
            {
                for(auto &word in *Sequence)
                {
                    if (WordsTable.find(word) == WrodsTable.end())
                    {
                        WordsTable.insert(pair<string, int>(word, WordsTable.size()));
                    }
                }
            }
            ~Sample()
            {
                delete Sequence;
                delete Labels;
            }
            VectorInt* GetFeature(int seqNum, int y0State, int y1State = InvalidState)
            {
                string &word = (*mSequece)[seqNum];
                VectorInt *weightIndex = new VectorInt();
                int index = 0;
                int labelsize = LabelTable.size();
                
                if (InvalidState == y1State)
                {
                    index = WordsTable[word] * labelsize + y0State;
                }
                else
                {
                    index = WordsTable[word] * pow(labelsize, 2) + y0State * labelsize + y1State;
                }
                weightIndex->push_back(index);
                
                return weightIndex;
            }
            
        private:

    };
    class PotentialTable
    {
        public:
            double *const Log0;
            double *const Logs;
            const size_t Log0Size;
            const size_t LogsSize0;
            const size_t LogsSize1;
            const size_t LogsSize2;

            PotentialTable(log0Size, logsSize0, logsSize1, logsSize2)
            :
            Log0Size(log0Size),
            LogsSize0(logsSize0),
            LogsSize1(logsSize1),
            LogsSize2(logsSize2),
            Log0(new double[log0Size]),
            Logs(new double[logsSize0 * logsSize1 * logsSize2])
            {
            }

            ~PotentialTable()
            {
                delete[] Log0;
                delete[] Logs;
            }      

    };

    class CRFBin
    {
        public:
            CRFBin(int nodeFeatureSize, int edgeFeatureSize, int labelStateSize)
            {
                mWnode = new double[nodeFeatureSize];
                mWedge = new double[edgeFeatureSize];

                mNodeFeatureSize = nodeFeatureSize
                mEdgeFeatureSize = edgeFeatureSize
                mLabelStateSize  = labelStateSize;
            }
            
            PotentialTable *LogPotentialTable(Sample &sequence)
            {
                int    index = 0;
                double edge  = 0;
                double node  = 0;
                size_t seqLength = sequence.Sequence.size();
                PotentialTable *potentialTable = new PotentialTable(mLabelStateSize, seqLength-1, mLabelStateSize, mLabelStateSize);
                for(size_t i = 0; i < mLabelStateSize; ++i)
                {
                    potentialTable->Log0[i] = product(sequence.GetFeature(0, i));
                }
                for(size_t i = 1; i < seqLength; ++i)
                {
                    for(size_t j = 0; j < mLabelStateSize; ++j)
                    {
                        for(size_t k = 0; k < mLabelStateSize; ++k)
                        {
                            index = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 +
                                    j     * potentialTable->LogsSize2 + k;
                            node  = product(sequence.GetFeature(i, k));
                            edge  = product(sequence.GetFeature(i, j, k), false);
                            potentialTable->Logs[index] = node + edge;
                        }
                    }
                }
                return potentialTable;
            }

            double Loglikelihood(Sample &sequence)
            {
                size_t seqLength = sequence.Sequence.size();
                const vector<int> * const seqStates = sequence.Labels;

                PotentialTable * potentialTable = LogPotentialTable(sequence);
                Matrix *messages = forward(potentialTable, seqLength)
                
                double maxProb = max_element(messages->begin(), messages->end());
                double tempMargin = 0.0;
                for(int i = 0; i < mLabelStateSize; ++i)
                {
                    tempMargin += exp(messages[seqLength-1][i] - maxProb);
                }
                double logNormalizedTerm = log(tempMargin) + maxProb;
                double logLikelihood = potentialTable->Log0[seqStates[0]];
                int y1 = 0;
                int y2 = 0;
                int index = 0;
                for(i = 1; i < seqLength; ++i)
                {
                    y1 = seqStates[i-1];
                    y2 = seqStates[i];
                    index = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 +
                            y1    * potentialTable->LogsSize2 + y2;
                    logLikelihood += potentialTabl->Logs[index];
                }
                logLikelihood -= logNormalizedTerm;
                return logLikelihood;
            }

            VectorInt *Sample(Sample &sequence)
            {
                size_t seqLength = sequence.Sequence.size();
                int index = 0;
                double max = 0.0;
                double maxarg = 0;
                PotentialTable * potentialTable = LogPotentialTable(sequence);
                VectorInt *labels = new VectorInt(seqLength, 0);
                Matrix path(seqLength, VectorInt(seqLength, 0));
                double *tempPotential = new double[potentialTable->Log0Size];
                double *prevPotential = new double[potentialTable->Log0Size];
                double *currPotential = new double[potentialTable->Log0Size];
                double tempForSwap;
                copy(potentialtable->Log0, potentialTable->Log0+potentialTable->Log0Size, prevPotential);
                for(int i = 1; i < seqLength; ++i)
                {
                    for (int j = 0; j < mLabelStateSize; ++j)
                    {   
                        max = 0.0;
                        maxarg= 0;                     
                        index = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 + j;
                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            tempPotential[k] = prevPotential[k] + potentialTable->Logs[index + k*potentialTable->LogsSize2];
                            if (tempPotential[k] > tempPotential[maxarg])
                            {
                                maxarg = k;
                                max = tempPotential[k];
                            }
                        }
                        path[i-1][j] = maxarg;
                        currPotential[j] = max;
                    }
                    tempForSwap = currPotential;
                    currPotential = prevPotential;
                    prevPotential = tempForSwap;
                }
                maxarg= 0;   
                for(int i = 1; i < mLabelStateSize; ++i)
                {
                    if (prevPotential[i] > prevPotential[maxarg])
                    {
                        maxarg = i;
                    }
                }
                labels[labels->size()-1] = maxarg;
                for(int i = labels->size()-2; i >= 0; --i)
                {
                    labels[i] = pathMatrix[i][labels[i + 1]];
                }

                return labels;
            }
            void SGA(vector<Sample> &sequences, size_t iterations=20, double a0=1)
            {
                double oldLikelihood = -10000000000000000;
                size_t earlyStopCount = 3;
                size_t dataSize = sequences.size();
                for(int i = 0; i < iterations; ++i)
                {
                    double rate = a0 / (sqrt(iteration) + 1);
                    cout << "rate = " << rate << endl;
                    cout << "Iteration: " << i << endl;
                    for(int j = 0; j < dataSize; ++j)
                    {
                        update(sequences[j], rate);
                    }
                    
                    cout << "Cal loglikehood.." << endl;
                    double likelihood = 0.0;
                    for(int j = 0; j < dataSize; ++j)
                    {
                        likelihood += Loglikelihood(sequences[j]);
                    }
                    cout << "Loglihood: " << likelihood / dataSize << endl;
                    if (likelihood <= oldLikelihood)
                    {
                        earlyStopCount -= 1
                        if earlyStopCount == 0:
                            return
                    }
                    else
                    {
                        earlyStopCount = 3
                    }

                    oldLikelihood = likelihood
                }
            }
        private:
            double *mWnode;
            double *mWedge;
            double *mWnodeGradient;
            double *mWedgeGradient
            size_t  mLabelStateSize;
            size_t  mNodeFeatureSize;
            size_t  mEdgeFeatureSize;


            double product(VectorInt *indexVector, isNode=true)
            {
                double result = 0.0;
                double *w = NULL;
                if(isNode)
                {
                    w = mWnode;
                }
                else
                {
                    w = mWedge;
                }
                for(auto &index in *indexVector)
                {
                    result += w[index]
                }
                return result;
            }
            Matrix *forward(PotentialTable *potentialTable, size_t seqLength)
            {
                double tempMeg  = 0.0;
                double temp     = 0.0;
                size_t index    = 0;
                double maxProb  = 0.0;
                Vector Fs(mLabelStateSize, 0.0);

                Matrix *message = new Matrix(seqLength, Vector(mLabelStateSize, 0.0));
                copy(potentialTable->Log0[i], potentialTable->Log0[i] + mLabelStateSize, message[0].begin());
                for(int i = 1; i < seqLength; ++i)
                {
                    for(int j = 0; j < mLabelStateSize; ++i)
                    {
                        tempMeg = 0.0;
                        index   = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 + j;

                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            Fs[k] = potentialTable->Logs[index + k*potentialTable->LogsSize2] + message[i-1][k]
                        }
                        maxProb = max_element(Fs.begin(), Fs.end());

                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            tempMeg += exp(Fs[k] - maxProb)
                        }
                        tempMeg += maxProb
                        message[i][j] = tempMeg;
                    }
                }
                return message;
            }
            double *backward(PotentialTable *potentialTable, int seqLength)
            {
                double tempMeg  = 0.0;
                double temp     = 0.0;
                size_t index    = 0;
                double maxProb  = 0.0;
                Vector Fs(mLabelStateSize, 0.0);

                Matrix *message = new Matrix(seqLength, Vector(mLabelStateSize, 0.0));
                for(int i = seqLength-2; i >= 0; --i)
                {
                    for(int j = 0; j < mLabelStateSize; ++i)
                    {
                        tempMeg = 0.0;
                        index   = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 + 
                                  j     * potentialTable->LogsSize2;

                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            Fs[k] = potentialTable->Logs[index + k] + message[i+1][k]
                        }
                        maxProb = max_element(Fs.begin(), Fs.end());

                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            tempMeg += exp(Fs[k] - maxProb)
                        }
                        tempMeg += maxProb
                        message[i][j] = tempMeg;
                    }
                }
                return message;
            }
            void update(Sample &sequence, double rate)
            {
                size_t seqLength = sequence.Sequence.size();
                const vector<int> * const = sequence.Labels;

                PotentialTable *potentialTable = LogPotentialTable(sequence);
                Matrix *forwardMessages  = self.forward(potentialTable, seqLength);
                Matrix *backwardMessages = self.backward(potentialTable, seqLength);

                double maxProb = max_element(forwardMessages->begin(), forwardMessages->end());
                double tempMargin = 0.0;
                for(int i = 0; i < mLabelStateSize; ++i)
                {
                    tempMargin += exp(messages[seqLength-1][i] - maxProb);
                }
                double logNormalizedTerm = log(tempMargin) + maxProb;

                Vector *WnodeGradient = new Vector(mNodeFeatureSize, 0.0);
                Vector *WedgeGradient = new Vector(mEdgeFeatureSize, 0.0);

                for(int i = 0; i < seqLength; ++i)
                {
                    for(int j = 0; j < mLabelStateSize; ++j)
                    {
                        for(auto &elem in sequence.GetFeature(i, j))
                        {
                            WnodeGradient[elem] += exp(forwardMessages[i][j] + backwardMessages[i][j] - logNormalized);
                        }
                    }
                }                
                for(int i = 0; i < seqLength; ++i)
                {
                    for(int j = 0; j < mLabelStateSize; ++j)
                    {
                        for(int k = 0; k < mLabelStateSize; ++k)
                        {
                            index = (i-1) * potentialTable->LogsSize1 * potentialTable->LogsSize2 +
                                    j     * potentialTable->LogsSize2 + k;
                            for(auto &elem in sequence.GetFeature(i, j ,k))
                            {
                                WedgeGradient[elem] += exp(forwardMessages[i-1][j] + logPotentials[index] + backwardMessages[i][k] - logNormalized);
                            }
                        }
                    }
                }
                for(int i = 0; i < mNodeFeatureSize; ++i)
                {
                    mWnode[i] += WnodeGradient[i] * rate;
                }
                for(int i = 0; i < mEdgeFeatureSize; ++i)
                {
                    mWedge[i] += WedgeGradient[i] * rate;
                }
                for(int i = 0; i < seqLength; ++i)
                {
                    for(auto &elem in sequence.GetFeature(j, labels->operator[](j) ))
                    {
                        mWnode[elem] += rate;
                    }
                }
                for(int i = 1; i < seqLength; ++i)
                {
                    for(auto &elem in sequence.GetFeature(j, labels->operator[](j-1), labels->operator[](j)))
                    {
                        mWedge[elem] += rate;
                    }
                }
            }
            
    };
}
