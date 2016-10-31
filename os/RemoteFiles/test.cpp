#include <iostream>
#include <thread>
using namespace std;

void threadPro(int a, string b, double c)
{
    cout << a << " " << b << " " << c << endl;
}

int main(void)
{
    thread t1(threadPro, 1, "sfd", 12.3);
    t1.join();
    return 0;
}