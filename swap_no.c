#include <stdio.h>

int main()
{
    int a = 5, b =10;
    a = a+b;    // a=15
    b = a - b; // b= 15-10 = 5
    a = a - b;  //a = 15-5 = 10
    
    printf(" a = % d , b = %d ",a,b);

    return 0;
}
