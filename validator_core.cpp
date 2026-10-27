#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<string>

int main(int c,char* v[]){
    if(c<2)return 1;
    std::ifstream f(v[1]);
    if(!f.is_open())return 1;
    std::string l;
    int errs=0,passed=0;
    while(std::getline(f,l)){
        if(l.find("FAIL")!=std::string::npos)errs++;
        else if(l.find("PASS")!=std::string::npos)passed++;
    }
    std::cout<<"PASSED:"<<passed<<"|FAILED:"<<errs<<"\n";
    return errs>0?2:0;
}