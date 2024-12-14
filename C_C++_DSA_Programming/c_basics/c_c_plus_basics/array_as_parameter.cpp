#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int * func(int size){
    int *p;
    
    // p = (int *) malloc(size * sizeof(int));
    p = new int[size];
    
    for(int i=0; i<size; i++)
    p[i] = (i)+1;
    
    return p;
}

int main()
{
    int n = 5,*ptr;
    
    ptr = func(n);
    
    for(int i=0 ; i< n ; i++){
        cout<<ptr[i]<<endl;
    }
    
    // free(ptr);
    delete [] ptr;
    
    return 0;
}