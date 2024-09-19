import { expect } from "chai";
import { Solution } from "./facing_the_sun.js"; // Asegúrate de que la ruta es correcta.

describe("Solution", () => {
  it("Test 1 - Mixed Heights with Visible and Hidden", () => {
    let solution = new Solution();
    expect(solution.countBuildings([7, 4, 8, 2, 9])).to.equal(3);
  });

  it("Test 2 - Increasing Heights", () => {
    let solution = new Solution();
    expect(solution.countBuildings([2, 3, 4, 5])).to.equal(4);
  });
});
