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
    typedef std::auto_ptr<VectorInt > SmartIntVectorPointer;
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
                for(size_t i = 0; i < seqLength; ++i)
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
                size_t seqLength = sequence.Length;
                const vector<int> * const seqStates = sequence.Labels;

                PotentialTable * potentialTable = LogPotentialTable(sequence);
                Vector *messages = forward(potentialTable, seqLength)
                
                maxProb = max_element(messages->begin(), messages->end());
                

            }

            VectorInt *Sample(Sample &sequence)
            {

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
            update(Sample *sequence)
            {

            }
            
    };
}