//#include "testCRF.cpp"
#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <tuple>
#include <vector>
#include <algorithm>

using namespace std;

class Test
{
    public:
    int a = 10;
    static int b;
    double *const c;
    Test()
    :c(new double)
    {
    }
    int getB()
    {
        return b;
    }
};
int Test::b = 100;

const int s = 11;

int getInt(int a, int b = s)
{
    return b;
}
auto makeTuple()
{
    return make_tuple("zliag", 12, 12.3, "sdfff");
}
int main(void)
{
    cout << pow(12, 2) << endl;

    Test t;
    cout << t.a << endl;
    cout << t.getB() << endl;
    cout << getInt(1) << endl;
    map<string, int> m;
    m.insert(pair<string, int>("liuzhuang", 129));
    cout << m.size() << endl;

    int *const b = new int;
    delete b;

    auto tup = makeTuple();
    cout << std::get<1>(tup) << endl;
    cout << std::get<2>(tup) << endl;
    vector<vector<vector<int> > > tensor;

    cout << log(1) << endl;

    vector<int> *r = new vector<int>(2, 21);
    cout << r->operator[](1) << endl;
}