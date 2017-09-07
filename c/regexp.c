/* program to check validity of a string  for (a+b)^*b */
#include <stdio.h>
#include <string.h>

char str[100];
int flag = 0;

void regcheck()
{
	int i=0;
	if(str[0] == 'a')
	{
		while(str[i] == 'a')
		{
			i++;
		}

		if(str[i] == 'b' && str[i+1] == '\0')
		{
			flag=1;
		}
		else
			flag=0;
	}
	else if(str[0] = 'b')
	{
		while(str[i] == 'b')
		{
			i++;
		}

		if(str[i] == '\0') //str[i+1] == '\0')
			flag = 1;
		else
			flag = 0;
	}

}


		
int main()
{
	printf("Enter the string to be verified for the grammar (a+b)*b\n");
	gets(str);
	regcheck();
	if(flag == 1)
		printf("Entered string is a valid string\n");
	else
		printf("Entered string is not a valid string\n");
	return 0;
}
