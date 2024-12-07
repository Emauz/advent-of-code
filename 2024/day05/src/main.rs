// Advent of code 2024
// day 5
// Eric Moss

use std::env;
use std::fs;
use std::collections::{HashMap,HashSet};

fn main() {
    // Parse command line args
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("From file: {}", filename);

    // Parse input file
    let input = fs::read_to_string(filename).unwrap();
    let input = input.trim();
    let (rule_text, update_text) = input.split_once("\n\n").unwrap();

    // "rules" maps from a page number to ALL page numbers it must precede
    let mut rules: HashMap<usize, HashSet<usize>> = HashMap::new();
    for rule in rule_text.split("\n") {
        let (earlier, later) = rule.split_once("|").unwrap();
        let earlier: usize = earlier.parse().unwrap();
        let later: usize = later.parse().unwrap();

        let later_list: &mut HashSet<usize> = rules.entry(earlier).or_default();
        later_list.insert(later);
    }

    // "updates" is a 2d vector of page orderings
    let mut updates: Vec<Vec<usize>> = Vec::new();
    for line in update_text.split("\n") {
        let update_order: Vec<usize> = line.split(",").map(|x| x.parse::<usize>().unwrap()).collect();
        updates.push(update_order);
    }

    // Execute logic for each day
    match part1(&rules, &updates) {
        Some(result) => println!("Part 1: {}", result),
        None => println!("Error in part 1"),
    }
    match part2(&rules, &updates) {
        Some(result) => println!("Part 2: {}", result),
        None => println!("Error in part 2"),
    }
}

// Checks if single update adheres to the given set of ordering rules
fn is_inorder(rules: &HashMap<usize, HashSet<usize>>, update: &Vec<usize>) -> bool {
    let mut already_seen: HashSet<usize> = HashSet::new();
    for page in update {
        let should_precede: &HashSet<usize> = match rules.get(page) {
            Some(val) => val,
            None => continue,
        };
        // ensure nothing we're supposed to precede came before us
        if already_seen.intersection(should_precede).count() > 0 {
            //println!("{:?}: NOT inorder", update);
            //println!("Because: {} is preceded by: {:?}", page, already_seen.intersection(should_precede));
            return false;
        }
        already_seen.insert(*page);
    }
    //println!("{:?}: inorder", update);
    true
}

fn part1(rules: &HashMap<usize, HashSet<usize>>, updates: &Vec<Vec<usize>>) -> Option<usize> {
    let mut center_sum: usize = 0;
    for u in updates {
        if is_inorder(rules, u) {
            let center_val: &usize = u.get(u.len() / 2)?;
            center_sum += center_val;
        }
    }
    Some(center_sum)
}

// Part 2 code

// very similar to above, but returns the two indices that should be swapped to fix whatever rule is wrong.
// Note: may not necessarily fix the whole thing, so this should be ran iteratively until no "fix" is returned
fn find_rulebreakers(rules: &HashMap<usize, HashSet<usize>>, update: &Vec<usize>) -> Option<(usize, usize)> {
    let mut already_seen: HashSet<usize> = HashSet::new();
    for (idx2, page) in update.iter().enumerate() {
        let should_precede: &HashSet<usize> = match rules.get(page) {
            Some(val) => val,
            None => continue,
        };
        // ensure nothing we're supposed to precede came before us
        if already_seen.intersection(should_precede).count() > 0 {
            //println!("{:?}: NOT inorder", update);
            let offending_val = already_seen.intersection(should_precede).next()?;
            //println!("Swapping ({},{})", page, offending_val);
            let idx1 = update.iter().position(|&x| x == *offending_val)?;
            return Some((idx1, idx2));
        }
        already_seen.insert(*page);
    }
    //println!("{:?}: inorder", update);
    None
}
fn part2(rules: &HashMap<usize, HashSet<usize>>, updates: &Vec<Vec<usize>>) -> Option<usize> {
    let mut center_sum: usize = 0;
    for u in updates {
        let mut u: Vec<usize> = u.clone();
        let mut incorrect= false;
        loop {
            let (idx1, idx2) = match find_rulebreakers(rules, &u) {
                Some(r) => r,
                None => {
                    //println!("{:?}: inorder!\n", u);
                    break
                },
            };
            //println!("{:?}: pre swap", u);
            u.swap(idx1, idx2);
            //println!("{:?}: post swap\n", u);
            incorrect = true;
        }
        if incorrect {
            //println!("{:?}: inorder!", u);
            let center_val: &usize = u.get(u.len() / 2)?;
            center_sum += center_val;
        }
    }
    Some(center_sum)
}