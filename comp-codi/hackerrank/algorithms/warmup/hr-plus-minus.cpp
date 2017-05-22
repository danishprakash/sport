#include <iostream>
#include <memory>
#include <iomanip>
using namespace std;

int main()
{
  int *a;
  int n;
  float negativeCounter=0, positiveCounter=0, zeroCounter=0;
  float nC=0, pC=0, zC=0;
  //cout<<"Enter the size of the array";
  cin>>n;
  int b[n];
  //a = (int *)malloc(sizeof(int)*n);
  for(int i=0; i<n; i++)
  {
    cin>>b[i];
    if(b[i] < 0) negativeCounter++;
      else if(b[i] == 0) zeroCounter++;
        else positiveCounter++;
  }
  //cout<<negativeCounter<<" "<<positiveCounter<<" "<<zeroCounter;
  nC = negativeCounter/n;
  pC = positiveCounter/n;
  zC = zeroCounter/n;
  cout << std::fixed;
  cout << std::setprecision(6);
  cout<<pC<<endl<<nC<<endl<<zC;
}
