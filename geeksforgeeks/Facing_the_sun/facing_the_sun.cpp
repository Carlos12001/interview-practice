#include <iostream>
#include <vector>

class Solution {
 public:
  // Returns count buildings that can see sunlight
  int countBuildings(const std::vector<int>& height) {
    unsigned int last_height = 0;
    unsigned int count = 0;
    for (size_t i = 0; i < height.size(); i++) {
      if (last_height < height[i]) {
        count++;
        last_height = height[i];
      }
    }
    return count;
  }
};

// ---------------- Tests Cases ---------------
void runTest(const std::vector<int>& heights, int expected,
             const std::string& testName) {
  Solution sol;
  int result = sol.countBuildings(heights);
  std::cout << "Test " << testName << ": "
            << (result == expected ? "PASS" : "FAIL");
  std::cout << " (Expected: " << expected << ", Got: " << result << ")"
            << std::endl;
}

int main() {
  runTest({7, 4, 8, 2, 9}, 3, "Test 1");
  runTest({2, 3, 4, 5}, 4, "Test 2");
  return 0;
}