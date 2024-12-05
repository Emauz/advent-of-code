// Advent of code 2024
// day 3
// Eric Moss

use std::env;
use std::fs;
use regex::Regex;

fn main() {
    // Parse command line args
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("From file: {}", filename);

    // Parse input file
    let input = fs::read_to_string(filename).unwrap();

    // Execute logic for each day
    match part1(&input) {
        Some(result) => println!("Part 1: {}", result),
        None => println!("Error in part 1"),
    }
    match part2(&input) {
        Some(result) => println!("Part 2: {}", result),
        None => println!("Error in part 2"),
    }
}

fn part1(input: &String) -> Option<usize> {
    let re = Regex::new(r"mul\((\d*),(\d*)\)").unwrap();
    let mut total: usize = 0;
    for capture in re.captures_iter(input) {
        let first: usize = usize::from_str_radix(&capture[1], 10).unwrap();
        let second: usize = usize::from_str_radix(&capture[2], 10).unwrap();
        total += first * second;
    }
    Some(total)
}

fn part2(input: &String) -> Option<usize> {
    let re = Regex::new(r"mul\((\d*),(\d*)\)|do\(\)|don't\(\)").unwrap();
    let mut total: usize = 0;
    let mut enable: bool = true;
    for capture in re.captures_iter(input) {
        match &capture[0] {
            "do()" => enable = true,
            "don't()" => enable = false,
            _ => {
                if enable {
                    let first: usize = usize::from_str_radix(&capture[1], 10).unwrap();
                    let second: usize = usize::from_str_radix(&capture[2], 10).unwrap();
                    total += first * second;
                }
            }
        }
    }
    Some(total)
}