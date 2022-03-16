#include <iostream>
#include<sys/socket.h>
#include <vector>
#include <string>

using namespace std;

const int SOCK_DOMAIN = 2;
const int SOCK_TYPE = 0;

int main() {
    int sockfd = socket(SOCK_DOMAIN, SOCK_TYPE, 0);

}