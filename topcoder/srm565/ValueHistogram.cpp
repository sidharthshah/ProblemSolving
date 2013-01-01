#include <cstdio>
#include <iostream>
#include <cstring> 
#include <vector> 
#include <algorithm>

using namespace std;

class ValueHistogram{
	public:
	 vector <string> build(vector <int> values){
	 	int height = 0;
	 	int counts[11];

	 	memset(counts,0,sizeof(counts));
	 	vector <string> results;

	 	for(int i=0;i<values.size();i++){
	 		counts[values[i]]++;
	 	}

	 	for(int i=0;i<values.size();i++){
	 		cout << counts[i] << endl;
 	 	}

	 	for(int i=0;sizeof(counts);i++){
	 		int current_count = counts[i];
	 		height = max(height,current_count);
	 	}

	 	height += 1;
	 	cout << "Height" << endl;
	 	cout << height << endl;
	 	for(int i=0;i<height;i++){
	 		string current = "";
	 		for(int j=0;sizeof(counts);j++){
	 			if(counts[j] > 0){
	 				current += "X";
	 				counts[j] -= 1;
	 			}else{
	 				current += ".";
	 			}
	 		}
	 		results.push_back(current);
	 	}
	 	reverse(results.begin(),results.end());
	 	return results;
	}
};

int main(){
 ValueHistogram v;
 cout << "This is cool" << endl; 

 vector <int> test_1;
 test_1.push_back(2);
 test_1.push_back(3);
 test_1.push_back(5);
 test_1.push_back(5);	
 test_1.push_back(2);
 test_1.push_back(0);
 test_1.push_back(8);
 v.build(test_1);
}