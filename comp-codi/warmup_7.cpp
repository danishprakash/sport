#include <iostream>
#include <stdint.h>
using namespace std;

int main()
{
  int64_t a[5], max = 0, min = 0, sum=0;

  for(int i=0; i<5; i++)  cin>>a[i];

  for(int i=0; i<5; i++)
  {
    sum = 0;
    for(int j=0; j<5; j++)  sum += a[j];
    sum = sum - a[i];
    if(sum >= max) max = sum;
    else if(sum < min)  min = sum;
  }
  cout<<min<<" "<<max<<endl;
}
