#include <stdio.h>
#include <string.h>

char prod[10][30];
char alpha[10][10];
char beta[10][10];
int num;
int flag = 0;
int  k=0, l=0, m=0, n=0;
char start;
int counter = 0;
//char eps = 'ϵ'; 


int prosize()
{
	int i = 0;
	while(prod[0][i] != '\0')
	{
		counter++;
		i++;
	}
	return counter;	
}	


void display()
{

	printf("\n\n%c->", start);
	for(int j=0; j<m; j++)
	{
		printf("%s%c'", beta[j], start);
		if(j+1 < m)
			printf("|");
	}
	printf("\n%c'->", start);
	for(int i=0; i<k;i++)
	{
		printf("%s%c'", alpha[i], start);
		if(i <= k)
			printf("|");
	}
	printf("eps");
}


void remrec()
{
	for(int i=0 ;i<num; i++)
	{
		start = prod[i][0];

		for(int j = 3; j<=strlen(prod[i]); j++)
		{
						
				if(start == prod[i][j])
				{
					flag = 1;
					j++;
					while(prod[i][j] != '|')
					{
						alpha[k][l] = prod[i][j];
						j++;
						l++;
					}
					k++; l=0;
					//printf("//INSIDE FIRST IF//");
				}
				else if(start != prod[i][j])
				{
					//printf("//INSIDE SECOND IF//");
					while(prod[i][j] != '|' && prod[i][j] != 0)
					{
						
						beta[m][n] = prod[i][j];
						n++;
						j++;
					}
					m++; n=0;
				}
				else if(prod[i][j] == '\0')
					break;
						
		}
	}
	//	printf("---%s---", beta[1]);
}

int main()
{
	printf("Enter the number of productions");
	scanf("%d", &num);
	printf("Enter the grammar\n");
	for(int i=0; i<num; i++)
	{
		scanf("%s", prod[i]);
	}
	printf("\nEntered Grammar:\n");

	for(int i = 0; i<num; i++)
	{
		printf("%s\n", prod[i]);
	}
	//printf("SIZE IS %d", strlen(prod[0]));
	remrec();
	printf("\n-----------------------\n");
	if(flag == 1)
	{
		printf("\nLeft Recursion is present in the grammar\nCorrect Grammar is: ");
		display();
		printf("\n");
	}
	else
		printf("Left recrusion is not present in the grammar");
	
	return 0;
}
