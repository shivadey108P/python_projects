#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(){
    int const val = 5;
    int *p;
    // p=(int *)malloc(val*sizeof(int));
    p = new int[val];
    
    for(int i = 0 ; i<val ; i++){
        p[i] = i*2;
    }

    int length = val;
    for (int i = 0 ; i<length ; i++){
        cout<<p[i]<<endl;
    }

    delete [] p;
    // free(p);
    return 0;
}   