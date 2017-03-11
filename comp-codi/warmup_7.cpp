#include <iostream>
using namespace std;

int main()
{
  int a[5], max = 0, min = 0, sum=0;

  for(int i=0; i<5; i++)  cin>>a[i];

  for(int i=0; i<5; i++)
  {
    for(int j=0; j<5; j++)  sum += a[j];
    sum = sum - a[i];
    if(sum >= max) max = sum;
    else min = sum;
    sum = 0;
  }
  cout<<min<<" "<<max<<endl;
}
