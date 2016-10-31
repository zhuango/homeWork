#include <cstring>
#include <errno.h>

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <exception>
#include <thread>
using namespace std;

#include <netinet/in.h>
#include <sys/types.h>
#include <unistd.h>

#define MAXLINE 2 * 1024 * 1024
#define LISTENQ 4096
#define PORT 9877
/* create socket */
int Socket(int family, int type, int portocol)
{
	int n;
	if((n = socket(family, type, portocol)) < 0){
		cerr << "socket" << endl;
		terminate();;
	}

	return (n);
}
/* bind to the address */
void Bind(int listenfd, struct sockaddr *servaddr, int size_servaddr)
{
	if(bind(listenfd, servaddr, size_servaddr) < 0){
		cerr << "listen" << endl;
		terminate();;
	}
}
/* listen number */
void Listen(int listenfd, int listenq)
{
	if(listen(listenfd, listenq) < 0){
		cerr << "listen" << endl;
		terminate();;
	}
}
/* accept the client */
int Accept(int listenfd, struct sockaddr *servaddr, socklen_t *len)
{
	int connfd;
	if((connfd = accept(listenfd, servaddr, len)) < 0){
		cerr << "sccept" << endl;
		terminate();;
	}

	return (connfd);
}

/* write str */
void Write(int connfd, char *buff, int size_buff)
{
	if(write(connfd, buff, size_buff) < 0){
		cerr << "write" << endl;
		terminate();;
	}
}

/* read str */
void Read(int connfd, char *buff, int size_buff)
{
	if(read(connfd, buff, size_buff) < 0){
		cerr << "write" << endl;
		terminate();;
	}
}

/* close the socket */
void Close(int connfd)
{
	if(close(connfd) < 0){
		cerr << "close" << endl;
		terminate();;
	}
}

void SendFile(int connfd, string filename)
{
	char recvline[MAXLINE + 1];
	ifstream file;
	file.open(filename.c_str());
	while(!file.eof())
	{
		file.read(recvline, MAXLINE);
		if(file.gcount() == 0)
		{
			break;
		}
		send(connfd, recvline, file.gcount(), 0);
	}
	file.close();
}
void RecvFile(int connfd, string filename)
{
	char recvline[MAXLINE + 1];
	ofstream file;
	file.open(filename.c_str());
	while(true)
	{
		int n = recv(connfd, recvline, MAXLINE, 0);
		file.write(recvline, n);
		file.flush();
		if (n == 0)
		{
			break;
		}
	}
	file.close();
}

void process(int connfd)
{			
	char buff[MAXLINE + 1];
	Read(connfd, buff, 2);//get operation info.
	//cout << "aaaaaaaaaaaaa" << string(buff) << endl;///////
	if      (string(buff) == "1")
	{
		Read(connfd, buff, MAXLINE);//read filename.
		SendFile(connfd, string(buff));
	}
	else if (string(buff) == "2")
	{
		Read(connfd, buff, MAXLINE);//read filename
		RecvFile(connfd, string(buff));
	}
	Close(connfd);
	//cout << "aaaaaaaaaaaaa" << string(buff) << endl;///////
}

int main(void)
{
	int listenfd, connfd;
	struct sockaddr_in servaddr;
	time_t ticks;
	vector<thread> threads;
	int maxThreadSize = 2;

	/* create the socket */
	listenfd = Socket(AF_INET, SOCK_STREAM, 0);
	/* clear the address struct */
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;/* set the family */
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);/* receive all address client */
	servaddr.sin_port = htons(PORT);	/* set the portnumber */

	/* bind the sockfd snd the address */
	Bind(listenfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
	/* listening the client */
	Listen(listenfd, LISTENQ);
	/* accept the client */
	for(;;){
		/* if there is a client?Yes, then accept the client */
		connfd = Accept(listenfd, (struct sockaddr *)NULL, NULL);
		threads.push_back(thread(process, connfd));
		if (threads.size() > maxThreadSize)
		{
			for (auto &t: threads)
			{
				t.join();
			}
		}
	}
	
}
