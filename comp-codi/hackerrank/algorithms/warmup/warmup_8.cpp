#include <iostream>
#include <string>
using namespace std;

int main()
{
  string stamp, flag;
  getline(cin, stamp);
  flag = stamp.substr(stamp.length()-2:stamp.length());
  cout<<flag;

}
