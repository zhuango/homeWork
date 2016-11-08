test:test.cpp
	g++ test.cpp -o test -std=c++11 -lpthread
client:client.cpp
	g++ client.cpp -o put -std=c++11 -lpthread
	cp put get
server:server.cpp
	g++ server.cpp -o server -std=c++11 -lpthread
clean:
	rm test client server
