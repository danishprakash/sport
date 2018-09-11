/* Given two sequences, a subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For
 * example, 
 * “abc”, “abg”, “bdf”, “aeg”, „”acefg”, .. etc are subsequences of “a
 * bcdefg”. So a string of length n has 2^n different possible subsequences.  It is a 
 * classic computer science problem, the basis of file comparison programs and has applications in bioinformatics. Develop a pro
 * gram to 
 * implement the solution of Longest Common
 * Sub
 * -
 *  sequence problem.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int lcs(char *str, char*sub, int m, int n)
{
	if(m == 0 || n == 0)
		return 0;
	else if(str[m-1] == str[n-1])
		return lcs(str, sub, m-1, n-1)+1;
	else
		return MAX(lcs(str, sub, m-1, n), lcs(str, sub, m, n-1));
}

int main()
{
	int t=0, i=0;
	scanf("%d", &t);
	for(i=0; i<t; i++)
	{
		char *str=malloc(256);
		char *sub=malloc(256);
		scanf("%s", str);
		scanf("%s", sub);	
		printf("%d", lcs(str, sub, strlen(str), strlen(sub)));
	}
	return 1;
}
