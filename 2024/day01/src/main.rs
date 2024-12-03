// Advent of code 2024
// day 1
// Eric Moss

use std::env;
use std::fs;

fn main() {
    // Parse command line args
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("From file: {}", filename);

    // Parse input file
    let mut left: Vec<usize> = Vec::new();
    let mut right: Vec<usize> = Vec::new();
    for line in fs::read_to_string(filename).unwrap().lines() {
        let mut split_line = line.split_whitespace();
        left.push(split_line.next()
                            .expect("Unable to get left element from line")
                            .parse::<usize>()
                            .expect("Left element not a number"));
        right.push(split_line.next()
                             .expect("Unable to get right element from line")
                             .parse::<usize>()
                             .expect("Right element not a number"));
    }

    // Execute main logic
    match part1(&left, &right) {
        Some(result) => println!("Part 1: {}", result),
        None => println!("Error in part 1"),
    }
    match part2(&left, &right) {
        Some(result) => println!("Part 2: {}", result),
        None => println!("Error in part 2"),
    }
}

fn part1(left: &Vec<usize>, right: &Vec<usize>) -> Option<usize> {
    let mut sorted_left: Vec<usize> = left.clone();
    sorted_left.sort();
    let mut sorted_right: Vec<usize> = right.clone();
    sorted_right.sort();

    let mut total_diff: usize = 0;
    for (l, r) in sorted_left.iter().zip(sorted_right.iter()) {
        total_diff += l.abs_diff(*r);
    }
    Some(total_diff)
}

fn part2(left: &Vec<usize>, right: &Vec<usize>) -> Option<usize> {
    let mut sorted_right: Vec<usize> = right.clone();
    sorted_right.sort();

    let mut total_similarity_score = 0;
    for l in left.iter() {
        let lower_bound = match sorted_right.iter().position(|&x| x == *l) {
            Some(val) => val,
            None => continue, // No matches in second list? Skip this entry
        };
        let upper_bound = match sorted_right.iter().position(|&x| x > *l) {
            Some(val) => val,
            None => sorted_right.len(),
        };
        let num_matches: usize = upper_bound - lower_bound;
        let similarity_score = l * num_matches;
        total_similarity_score += similarity_score;
    }
    Some(total_similarity_score)
}