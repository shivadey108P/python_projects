#include <iostream>
#include <stdio.h>
using namespace std;

void fun1(int a){
    if (a>0){
        // fun1(a-1);
        cout<<a<<endl;
        fun1(a-1);
    }
}


int main(){
    int x = 3;
    fun1(x);
    return 0;
}