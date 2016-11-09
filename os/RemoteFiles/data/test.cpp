#include <iostream>
#include <thread>
#include <sstream>
using namespace std;

void threadPro(int a, string b, double c)
{
    cout << a << " " << b << " " << c << endl;
}

int main(void)
{
    string str = "123";
    stringstream ss(str);
	int result;
	ss >> result;

    cout << result - 1 << endl;
}