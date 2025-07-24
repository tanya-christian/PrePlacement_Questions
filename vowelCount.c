#include <stdio.h>
#include <string.h>

int main()
{
    
    char str[20],vowels[5]={'a','e','i','o','u'};
    int count=0,len;
    printf("Enter String:");
    scanf("%s",str);
    len = strlen(str);
    for(int i=0;i<len;i++)
    {
        if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u')
        {
            count ++;
        }
    }
    printf("Number of Vowels are:%d",count);
    return 0;
}
