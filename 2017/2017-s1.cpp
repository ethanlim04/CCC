#include <iostream>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::vector;


int main() {
  
  int n;
  cin >> n;

  vector<vector<int>> games = {};

  for(unsigned int i = 0; i < 2; i++) {
    vector<int> tempList = {};
    for(unsigned int j = 0; j < n; j++) {
      int tempVar = 0;
      cin >> tempVar;
      tempList.push_back(tempVar);
    }
    games.push_back(tempList);
  }
  
  int sum1 = 0;
  int sum2 = 0;
  vector<int> total = {};
  for(unsigned int t = 0; t < n; t++) {
    sum1 += games[0][t];
    sum2 += games[1][t];
    if(sum1 == sum2) {
      total.push_back(t+1);
    }
  }
  if(total.size() != 0) {
    cout << total[total.size() - 1] << endl;
  }
  else {
    cout << 0 << endl;
  }
  

  return 0;
}