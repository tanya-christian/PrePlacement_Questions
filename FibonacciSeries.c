#include <stdio.h>

int main()
{
    
    int num,first=0,second=1,next,i;
    printf("Enter Number:");
    scanf("%d",&num);
    printf("Fibonacci Series:\n");
    for(i=0;i<num;i++)
    {
        printf("%d ",first);
        next = first +second;
        first = second;
        second = next;
    }

    return 0;
}
