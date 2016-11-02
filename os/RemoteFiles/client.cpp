#include <cerrno>
#include <cstring>

#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <fstream>
#include <exception>
using namespace std;

#include <netinet/in.h>/* for the sockaddr_in ,AF_INET ,SOCK_STREAM*/
#include <arpa/inet.h>
#include <unistd.h>

#define MAXLINE 2 * 1024 * 1024
#define PORT 9877

vector<string> split(string line, char delim)
{
    istringstream toLine(line);
    vector<string> tokens;
    string item;
    while(getline(toLine, item, delim))
    {
		if (item == "" or item[0] == ' ')
		{
			continue;
		}
        tokens.push_back(item);
    }
    return tokens;
}

/* close the socket */
void Close(int connfd)
{
	if(close(connfd) < 0){
		cerr << "close" << endl;
		terminate();
	}
}
/* write str */
void Write(int connfd, const char *buff, int size_buff)
{
	if(write(connfd, buff, size_buff) < 0){
		cerr << "write" << endl;
		terminate();
	}
}

/* read str */
void Read(int connfd, char *buff, int size_buff)
{
	if(read(connfd, buff, size_buff) < 0){
		cerr << "write" << endl;
		terminate();
	}
}
void GetFile(int sockfd, string filename)
{
	char recvline[MAXLINE + 1];
	ofstream file;
	file.open(filename.c_str());
	while(true)
	{
		int n = recv(sockfd, recvline, MAXLINE, 0);
		file.write(recvline, n);
		file.flush();
		if (n == 0)
		{
			break;
		}
	}
	file.close();
}
void PutFile(int sockfd, string filename)
{	
	char recvline[MAXLINE + 1];
	ifstream file;
	file.open(filename.c_str());
	while(!file.eof())
	{
		file.read(recvline, MAXLINE);
		if (file.gcount() == 0)
		{
			break;
		}
		send(sockfd, recvline, file.gcount(), 0);
	}
	file.close();
}
int main(int argc, char *argv[])
{
	int sockfd, n;
	char recvline[MAXLINE + 1];
	struct sockaddr_in servaddr;

	if(argc != 2){
		cout << "Usage: a.out <IPaddress>" << endl;
		return 1;
	}

	/* create a socket */
	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
		cerr << "socket" << endl;
		return 1;
	}

	/* clear the socket address struct */
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;/* set the family */
	servaddr.sin_port = htons(PORT);/* set the port number */

	/* set the command line arg to the suitable like */
	if(inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0){
		cerr << "inet_pton error" << endl;
		return 1;
	}

	/* connect the server, the server address is in the struct that named servaddr */
	if(connect(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) < 0){
		cout << errno << endl;
		cerr << "connect" << endl;
		return 1;
	}
	
	string command;
	//command format:
	// put localFileName  remoteFileName
	// get remoteFileName localFileName
	getline(cin, command);
	vector<string> elems = split(command, ' ');
	if      (elems[0] == "get")
	{
		Write(sockfd, "1", 2);//send operation code.
		Write(sockfd, elems[1].c_str(), elems[1].size() + 1);//send filename which client want to get.
		GetFile(sockfd, elems[2]);
	}
	else if (elems[0] == "put")
	{
		Write(sockfd, "2", 2);//send operation code.
		Write(sockfd, elems[2].c_str(), elems[2].size() + 1);//send filename which server should create.
		PutFile(sockfd, elems[1]);
	}
	else
	{
		cout << "Invalid operations." << endl;
	}
	Close(sockfd);

	return 0;
}
