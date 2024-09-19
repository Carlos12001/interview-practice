struct Solution;

impl Solution {
    fn count_buildings(&self, heights: Vec<i32>) -> i32 {
        let mut last_height = 0;
        let mut count = 0;
        for &height in heights.iter() {
            if last_height < height {
                count += 1;
                last_height = height;
            }
        }
        count
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_mixed_heights() {
        let solution = Solution;
        assert_eq!(solution.count_buildings(vec![7, 4, 8, 2, 9]), 3);
    }

    #[test]
    fn test_increasing_heights() {
        let solution = Solution;
        assert_eq!(solution.count_buildings(vec![2, 3, 4, 5]), 4);
    }
}

fn main() {
    let solution = Solution;
    let heights = vec![7, 4, 8, 2, 9];
    let result = solution.count_buildings(heights);
    println!("Number of buildings that can see the sun: {}", result);
}
