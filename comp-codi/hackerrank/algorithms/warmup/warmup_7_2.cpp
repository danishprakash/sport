#include <iostream>
using namespace std;
typedef unsigned long long int ull;


int main()
{
  ull a[5], min = 0, max = 0, sum = 0;
  for(int i=0; i<5; i++)  {cin>>a[i]; sum += a[i];}
  min = a[0]; max = a[0];
  for(int j =  0; j<5; j++)
  {
    if(a[j] >= max)  max = a[j];
    if(a[j] < min)  min = a[j];
  }
  cout<<(sum-max)<<" "<<(sum-min);
}
