#include <iostream>
using namespace std;

int main()
{

    int A[10] = {5, 8, 3, 9, 6, 2, 10, -2, 7, 4};
    int n = 10;
    int min, max;
    min=max = A[0];
    for(int i=0; i<n; i++){
        if(A[i]<min){
            min = A[i];
        }else if(A[i]>max){
            max = A[i];
        }
    }
    cout<<"Min: "<<min<<endl;
    cout<<"Max: "<<max<<endl;

    return 0;
}