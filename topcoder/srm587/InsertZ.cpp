#include <iostream>
#include <string>

using namespace std;

class InsertZ {
    public:
    string canTransform( string init, string goal ){
        string s = "";

        // build s, a copy of goal with the z characters removed:
        for (int i = 0; i < goal.size(); i++) {
            if(goal[i] != 'z') {
                s += goal[i];
            }
        }

        //compare the result with init:
        if (s == init) {
            return "Yes";
        } else {
            return "No";
        }
    }
};


int main(){
    InsertZ i;
    cout << i.canTransform("fox","fx") << endl;
    return 0;
}
