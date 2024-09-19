export class Solution {
  // Returns count buildings that can see sunlight
  /**
   * @param {number[]} height
   * @returns {number}
   */
  countBuildings(height) {
    let last_height = 0;
    let count = 0;
    for (let i = 0; i < height.length; i++) {
      if (last_height < height[i]) {
        count++;
        last_height = height[i];
      }
    }
    return count;
  }
}
