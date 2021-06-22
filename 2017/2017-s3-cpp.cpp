#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using namespace std;

#define map std::unordered_map // Define std::unordered_map as just map
#define set std::unordered_set // Defined std::unordered_set as just set

void printVec(vector<int> vec) {
    cout << "[";

    if (vec.size() > 0) {
        for (auto& elem : vector<int>(vec.begin(), vec.end() - 1)) { // For elem in vec[:-1]
            cout << elem << ", ";                                    // Print the element
        }

        cout << vec.back(); // Print the last element of the vector without a comma
    }

    cout << "]" << endl;
}


int baseNums(vector<int> numListIn, int length) {
    int count = 0;
    vector<int> numList = numListIn;
    for(auto& elem : numListIn) {
        //printVec(numList);
        int inverse = length - elem;
        if(std::find(numList.begin(), numList.end(), inverse) != numList.end()) {
            numList.erase(std::remove(numList.begin(), numList.end(), elem), numList.end());
            numList.erase(std::remove(numList.begin(), numList.end(), inverse), numList.end());
            //printVec(numList);
        }
        else if(!(std::find(numList.begin(), numList.end(), inverse) != numList.end())) {
            ;
        }
        else {
            numList.erase(std::remove(numList.begin(), numList.end(), elem), numList.end());
            count++;
        }
    }
    return count;
}


int main() {
    int n;
    cin >> n;
    vector<int> nums;
    //cout << "\n" << endl;
    int input;
    for(int i=0; i < n; i++) {
        cin >> input;
        nums.push_back(input);
    }
    sort(nums.begin(), nums.end());
    int minLen = nums[0] + nums[1];
    int maxLen = nums[nums.size() - 1] + nums[nums.size()-2];
    
    map<int, vector<int>> out;

    if(minLen == maxLen) {
        cout << (int)((n - baseNums(nums, minLen))/2) << " " << 1 << endl;
        return 0;
    }
    else {
        int maxVal = 0;
        for(int length = maxLen-1; length > minLen; length--) {
            cout << "starting" << endl;
            //printVec(nums);
            int res = (int)((n - baseNums(nums, minLen))/2);
            cout << "ranfunc" << endl;
            maxVal = max(res, maxVal);
            cout << maxVal << length << endl;
        }
    }
}