#include <stdio.h>

int main()
{
	int t, n, i, j, temp, count, k, temp2;
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		count = 0;
		scanf("%d", &n);
		int a[n];
		for(j=0; j<n; j++)
		{
			scanf("%d", &a[j]);
		}
		while(n-1 != 0)
		{
			printf("%d %d %d\n", a[0], a[n-1], n-1);
			temp2 = a[n-1];
			while(k>0)
			{
				temp = a[k-1];
				a[k] = temp;
				k--;
			}
			a[0] = temp2;
			if(count >= n-1)
				k = 0;
			else
				k = n-1-count;
			printf("\n--%d %d %d %d--\n", a[k], k, n, count);
			while(k<n)
			{
				a[k] = a[k+1];
				k++;
			}
			n--;
			count++;
		}
		printf("\n%d\n", a[n-1]);
	}
	return 1;
}
