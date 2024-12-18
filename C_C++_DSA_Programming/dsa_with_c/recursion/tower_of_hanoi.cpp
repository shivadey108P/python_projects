#include <iostream>
using namespace std;

int count = 0;

void toh(int n, int A, int B, int C){
    if(n>0){
        toh(n-1,A,C,B);
        // cout<<"Disc "<<A<<" is moved to "<<C<<" using "<<B<<endl;
        count++;
        toh(n-1,B,A,C);
    }
}

int main(){
    toh(16,1,2,3);
    cout<<"Total steps: "<<count;
    return 0;
}