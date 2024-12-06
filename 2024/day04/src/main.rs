// Advent of code 2024
// day 3
// Eric Moss

use std::env;
use std::fs;
use itertools::Itertools;

fn main() {
    // Parse command line args
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("From file: {}", filename);

    // Parse input file
    let input = fs::read_to_string(filename).unwrap();

    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in input.split_whitespace() {
        grid.push(line.chars().collect());
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

fn find_string(grid: &Vec<Vec<char>>, start_row:usize, start_col:usize, delta_row:isize, delta_col:isize, target: &Vec<char>) -> bool{
    // make start row and col signed so that types match during math
    let start_row: isize = isize::try_from(start_row).unwrap();
    let start_col: isize = isize::try_from(start_col).unwrap();
    let num_rows: usize = grid.len();
    let num_cols: usize = grid[0].len();
    for (idx, target_char) in target.iter().enumerate() {
        let idx: isize = isize::try_from(idx).unwrap();
        // calculate where we're gonna look
        let search_row = match usize::try_from(start_row + (delta_row * idx)) {
            Ok(val) => val,
            Err(_) => return false,
        };
        let search_col = match usize::try_from(start_col + (delta_col * idx)) {
            Ok(val) => val,
            Err(_) => return false,
        };
        // ensure we're still looking within bounds of the grid
        if search_col >= num_cols ||
           search_row >= num_rows {
            return false;
        }
        // see what we actually have in the grid at that location
        let actual_char = grid[search_row][search_col];
        if actual_char != *target_char {
            return false;
        }
    }
    return true;
}

fn part1(grid: &Vec<Vec<char>>) -> Option<usize> {
    let target: Vec<char> = ['X', 'M', 'A', 'S'].to_vec();
    let tegrat: Vec<char> = ['S', 'A', 'M', 'X'].to_vec(); // reversed target (since words can be backwards in a word search)
    let mut num_xmas = 0;
    let num_rows: usize = grid.len();
    let num_cols: usize = grid[0].len();
    // iterate through every starting square in the grid
    for (row, col) in (0..num_rows).cartesian_product(0..num_cols) {
        // Search from this point right for xmas/samx
        if find_string(grid, row, col, 0, 1, &target) ||
           find_string(grid, row, col, 0, 1, &tegrat) {
            num_xmas += 1;
        }

        // Search from this point down for xmas/samx
        if find_string(grid, row, col, 1, 0, &target) ||
           find_string(grid, row, col, 1, 0, &tegrat) {
            num_xmas += 1;
        }

        // Search from this point down right for xmas/samx
        if find_string(grid, row, col, 1, 1, &target) ||
           find_string(grid, row, col, 1, 1, &tegrat) {
            num_xmas += 1;
        }

        // Search from this point down left for xmas/samx
        if find_string(grid, row, col, 1, -1, &target) ||
           find_string(grid, row, col, 1, -1, &tegrat) {
            num_xmas += 1;
        }
    }
    Some(num_xmas)
}

// Part 2 code

fn find_x_mas(grid: &Vec<Vec<char>>, start_row:usize, start_col:usize) -> bool{
    // if center of X isn't an 'A', we can't possibly have an x-mas!
    if grid[start_row][start_col] != 'A' {
        return false;
    }
    // make start row and col signed so that types match during math
    let start_row: isize = isize::try_from(start_row).unwrap();
    let start_col: isize = isize::try_from(start_col).unwrap();
    let num_rows: usize = grid.len();
    let num_cols: usize = grid[0].len();
    // calculate where we're gonna look
    let left_col = match usize::try_from(start_col - 1) {
        Ok(val) => val,
        Err(_) => return false,
    };
    let right_col = match usize::try_from(start_col + 1) {
        Ok(val) => val,
        Err(_) => return false,
    };
    let top_row = match usize::try_from(start_row - 1) {
        Ok(val) => val,
        Err(_) => return false,
    };
    let bot_row = match usize::try_from(start_row + 1) {
        Ok(val) => val,
        Err(_) => return false,
    };
    // ensure we're still looking within bounds of the grid
    if right_col >= num_cols ||
       bot_row >= num_rows {
        return false;
    }
    // get our corner chars
    let tl: char = grid[top_row][left_col];
    let bl: char = grid[top_row][right_col];
    let tr: char = grid[bot_row][left_col];
    let br: char = grid[bot_row][right_col];

    // Check for vertically polarized x-mas
    if tl == bl &&
       tr == br &&
       ((tl == 'M' && tr == 'S') ||
        (tl == 'S' && tr == 'M')) {
        return true;
    }

    // Check for horizontally polarized x-mas
    if tl == tr &&
       bl == br &&
       ((tl == 'M' && bl == 'S') ||
        (tl == 'S' && bl == 'M')) {
        return true;
    }
    return false;
}

fn part2(grid: &Vec<Vec<char>>) -> Option<usize>{
    let mut num_xmas = 0;
    let num_rows: usize = grid.len();
    let num_cols: usize = grid[0].len();
    // iterate through every starting square in the grid
    for (row, col) in (0..num_rows).cartesian_product(0..num_cols) {
        if find_x_mas(grid, row, col) {
            num_xmas += 1;
        }
    }
    Some(num_xmas)
}