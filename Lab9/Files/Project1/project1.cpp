#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    string temp = "This is a known message!";
    auto hex2 = 0xa469b1c502c1cab966965e50425438e1bb1b5f9037a4c159;
    auto hex3 = 0xbf73bcd3509299d566c35b5d450337e1bb175f903fafc159;
    stringstream ss;
    int a = 5, b = 6;
    for(auto i : temp){
        ss << hex << (int)i;
    }
    
    cout << (hex2 ^ hex3);
    }
