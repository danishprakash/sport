#include <stdio.h>
#include <conio.h>

int calDist(int t[3][3], int g[3][3])
{
	int i=0, j=0, count=0;
	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
		{
			if(t[i][j] != g[i][j])
				count++;
		}
	}
	return count;
}

int getIndex(int x[3][3], int c, int num)
{
	int i=0, j=0, ret=0;
	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
		{
			if(x[i][j] == num)
			{
				//printf("\nnum: %d x[i][j]: %d", num, x[i][j]);
				if(c == 1)
					ret = i;
				else
					ret = j;
			}
		}
	}
	return ret;
}

int calSum(int t[3][3], int g[3][3])
{
	int i=0,j=0, sum=0, i2, j2;
	for(i=0; i<3;i++)
	{
		for(j=0; j<3; j++)
		{
			if(t[i][j] != 0)
			{
				i2 = getIndex(g, 1, t[i][j]);
				j2 = getIndex(g, 2, t[i][j]);
				//printf("\n%d %d %d %d", i, j, i2, j2);
				sum += (abs(i-i2)+abs(j-j2));
				//printf("\nSum: %d", sum);
			}
		}
	}
	return sum;
}


void printMatrix(int x[3][3])
{
	int i=0,j=0;
	for(i=0; i<3; i++)
	{
		for(j=0; j<3; j++)
		{
			printf("%d", x[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int si[3][3]={0,6,3,7,2,4,8,1,5}, sf[3][3]={1,2,3,8,0,4,7,6,5};
	clrscr();
	printf("Enter initial matrix\n");
	//printMatrix(si);
	//printMatrix(sf);
	printf("%d", calSum(si, sf));
	getch();
	return 1;
}