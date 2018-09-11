#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	char a[] = "AMITABH BACHCHAN";
	char b[] = "RAJNIKANTH";
	vector<char> temp;
	int i, size, j;
	for(i=0; i<sizeof(b); i++)
	{
		for(j=0; j<sizeof(a); j++)
		{
			if(b[i] == a[j])
			{
				if(!(std::find(temp.begin(), temp.end(), b[i]) != temp.end()))
					temp.push_back(b[i]);		
			}
		}
	}
	for(i=0; i<temp.size(); i++)
		cout<<temp[i];
	return 0;
}
