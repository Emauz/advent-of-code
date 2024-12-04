// Advent of code 2024
// day 2
// Eric Moss

use std::env;
use std::fs;

fn main() {
    // Parse command line args
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("From file: {}", filename);

    // Parse input file
    let mut grid: Vec<Vec<usize>> = Vec::new();
    let input = fs::read_to_string(filename).unwrap();
    for line in input.trim().split('\n'){
        let line_vec: Vec<usize> = line.split_whitespace()
                                       .map(|x| usize::from_str_radix(x, 10).unwrap())
                                       .collect();
        grid.push(line_vec);
    }

    // Execute logic for each day
    match part1(&grid) {
        Some(result) => println!("Part 1: {}", result),
        None => println!("Error in part 1"),
    }
    match part2(&grid) {
        Some(result) => println!("Part 2: {}", result),
        None => println!("Error in part 2"),
    }
}

fn part1(grid: &Vec<Vec<usize>>) -> Option<usize> {
    let mut safe_lines: usize = 0;
    for line in grid {
        let mut safe: bool = true;
        let mut prev: usize = line[0];
        let increasing: bool = line[0] < line[1];
        for entry in &line[1..] {
            if usize::abs_diff(*entry, prev) > 3 ||
               usize::abs_diff(*entry, prev) == 0 ||
               prev > *entry && increasing ||
               prev < *entry && !increasing  {
                safe = false;
            }
            prev = *entry;
        }
        if safe {
            safe_lines += 1;
        }
    }
    Some(safe_lines)
}

// part 2 implementation

/// Finds the index of the first unsafe value in this reactor row
/// If row is safe, funciton returns None
/*/
fn find_unsafe_idx(line: &Vec<usize>) -> Option<usize> {
    let increasing: bool = line[0] < line[1];
    for (pos, entry) in line.iter().enumerate() {
        if pos == line.len() - 1  {
            return None;
        }
        let next = line[pos + 1];
        if usize::abs_diff(*entry, next) > 3 ||
           usize::abs_diff(*entry, next) == 0 {
            return Some(pos)
        }
        if next < *entry && increasing ||
           next > *entry && !increasing  {
            return Some(pos + 1)
        }
    }
    None
}
*/

fn is_safe(line: &Vec<usize>) -> bool {
    let mut prev: usize = line[0];
    let increasing: bool = line[0] < line[1];
    for entry in &line[1..] {
        if usize::abs_diff(*entry, prev) > 3 ||
            usize::abs_diff(*entry, prev) == 0 ||
            prev > *entry && increasing ||
            prev < *entry && !increasing  {
            return false
        }
        prev = *entry;
    }
    return true
}

fn part2(grid: &Vec<Vec<usize>>) -> Option<usize> {
    let mut safe_lines: usize = 0;
    for line in grid {
        // See if it's safe by default
        match is_safe(line) {
            true => { safe_lines += 1; }
            false => {
                // try removing each element from the list and see if any of those lists end up safe
                for i in 0 .. line.len() {
                    let mut removed_line = line.clone();
                    removed_line.remove(i);
                    if is_safe(&removed_line) {
                        safe_lines += 1;
                        break;
                    }
                }
            }
        }
        //println!("safe line:\t{:?}", line);
    }
    Some(safe_lines)
}

/*
fn part2(grid: &Vec<Vec<usize>>) -> Option<usize> {
    let mut safe_lines: usize = 0;
    for line in grid {
        // See if it's safe by default
        match find_unsafe_idx(line) {
            Some(idx) => {
                // See if it's safe with that index removed
                let mut modified_line = line.clone();
                println!("unsafe line:\t{:?}", modified_line);
                modified_line.remove(idx);
                println!("safe ? line:\t{:?}", modified_line);
                match find_unsafe_idx(&modified_line) {
                    Some(_) => { 
                        continue; 
                    }
                    None => { safe_lines += 1; }
                }

            }
            None => { safe_lines += 1; }
        }
        //println!("safe line:\t{:?}", line);
    }
    Some(safe_lines)
}
*/