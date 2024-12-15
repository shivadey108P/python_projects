#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

struct Rectangle{
    int length;
    int breadth;
};


int main(){
    int *p1,a1;
    float *p2, a2;
    double *p3,a3;
    char *p4, a4;
    struct Rectangle *p5, a5;

    cout<<sizeof(p1)<<endl;
    cout<<sizeof(p2)<<endl;
    cout<<sizeof(p3)<<endl;
    cout<<sizeof(p4)<<endl;
    cout<<sizeof(p5)<<endl;

    cout<<sizeof(a1)<<endl;
    cout<<sizeof(a2)<<endl;
    cout<<sizeof(a3)<<endl;
    cout<<sizeof(a4)<<endl;
    cout<<sizeof(a5)<<endl;


    return 0;
}


