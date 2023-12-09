// Advent of code 2023
// day 2
// Eric Moss

using System;
using System.IO;

void Main()
{
    // string filename = "inputs/sample.txt";
    // string filename = "inputs/sample2.txt";
    string filename = "inputs/input.txt";


    if(!File.Exists(filename))
    {
        Console.Error.WriteLine("Error: provided file \"" + filename + "\" does not exist. Exiting.");
        System.Environment.Exit(1);
    }
    string[] lines = File.ReadAllLines(filename);
    List<Game> all_games = parse_input(lines);

    Console.WriteLine(Part1(all_games));
    Console.WriteLine(Part2(all_games));


}
Main();

List<Game> parse_input(string[] lines) 
{
    List<Game> all_games = new List<Game>();
    int[] calibration_values = new int[lines.Length];
    for(int i=0; i<lines.Length; i++)
    {
        string[] substrings = lines[i].Split(':');

        // First, extract game ID and create game object
        int id = Int32.Parse(substrings[0].Split()[1]);
        Game currentGame = new Game(id);

        // Next, iterate through each round of the game and add to the game object
        string[] gameRounds = substrings[1].Split(';');
        foreach(string round in gameRounds)
        {
            string[] roundSplit = round.Split(',');
            Set currentSet = new Set();
            foreach(string colorData in roundSplit)
            {
                string[] splitColorData = colorData.Split();
                int quantity = Int32.Parse(splitColorData[1]);
                switch(splitColorData[2]) {
                    case "red":
                        currentSet.red = quantity;
                        break;
                    case "green":
                        currentSet.green = quantity;
                        break;
                    case "blue":
                        currentSet.blue = quantity;
                        break;
                }
            }
            currentGame.sets.Add(currentSet);
        }
        all_games.Add(currentGame);
    }
    return all_games;
}

int Part1(List<Game> all_games) {
    int id_sum = 0;
    foreach(Game g in all_games) {
        if(g.valid_config(12, 13, 14))
        {
            id_sum += g.id;
        }
    }
    return id_sum;
}

int Part2(List<Game> all_games) {
    int power_sum = 0;
    foreach(Game g in all_games) {
        power_sum += g.power();
    }
    return power_sum;
}


public struct Set {
    public int red { get; set; }
    public int green { get; set; }
    public int blue { get; set; }
   public override string ToString()
   {
      return String.Format("red: {0}, green: {1}, blue: {2}", red, green, blue);
   }
}

public class Game 
{

    public Game(int _id) 
    {
        id = _id;
        sets = new List<Set>();
    }

    public int id { get; init; }
    public List<Set> sets { get; set; }

    // determines if this game could have happened with the given marble quantities
    // (used for part 1)
    public bool valid_config(int total_red, int total_green, int total_blue)
    {
        foreach(Set set in sets)
        {
            if(set.red > total_red ||
               set.green > total_green||
               set.blue > total_blue) {
                    return false;
                }

        }
        return true;
    }

    // determines the "power" of a given game 
    // (used for part 2)
    public int power() {
        int max_red = 0;
        int max_green = 0;
        int max_blue = 0;
        foreach(Set set in sets)
        {
            if(set.red > max_red)
            {
                max_red = set.red;
            }
            if(set.green > max_green)
            {
                max_green = set.green;
            }
            if(set.blue > max_blue)
            {
                max_blue = set.blue;
            }
        }
        return max_red * max_green * max_blue;
    }
}
