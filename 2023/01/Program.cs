// Advent of code 2023
// day 1
// Eric Moss

using System;
using System.IO;

string[] spelled_out_digits = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
};

int Part1(string[] lines) {
    int[] calibration_values = new int[lines.Length];
    for(int i=0; i<lines.Length; i++)
    {
        string current_line = lines[i];
        int first_number = -1;
        int second_number = -1;
        bool first_number_set = false;
        for(int j=0; j<current_line.Length; j++)
        {
            if(Char.IsDigit(current_line[j])) {
                int digit = (int)Char.GetNumericValue(current_line[j]);
                if(!first_number_set)
                {
                    first_number = digit;
                    first_number_set = true;
                }
                second_number = digit;
            }
        }
        int calibration_value = (first_number * 10) + second_number;
        calibration_values[i] = calibration_value;
    }

    int answer = 0;
    foreach(int value in calibration_values)
    {
        answer += value;
    }
    return answer;
}

int Part2(string[] lines) {
    int[] calibration_values = new int[lines.Length];
    // calculate calibration values for each string provided
    for(int i=0; i<lines.Length; i++)
    {
        string current_line = lines[i];
        int first_number = -1;
        int second_number = -1;
        bool first_number_set = false;
        for(int j=0; j<current_line.Length; j++)
        {
            // calculate calibration value for single string
            int digit = -1;
            // Is the current character a numeral?
            if(Char.IsDigit(current_line[j])) 
            {
                digit = (int)Char.GetNumericValue(current_line[j]);
            }
            else
            {
                // Are we currently at the beginning of a spelled out digit?
                for(int k=0; k<9; k++)
                {
                    string spelled_digit = spelled_out_digits[k];
                    string to_compare = new String(current_line.Skip(j)
                                                            .Take(spelled_digit.Length)
                                                            .ToArray());
                    if(spelled_digit == to_compare)
                    {
                        digit = k+1;
                        break;
                    }
                }

            }

            if(digit != -1)
            {
                // we're currently at a digit
                if(!first_number_set)
                {
                    first_number = digit;
                    first_number_set = true;
                }
                second_number = digit;
            }
        }
        int calibration_value = (first_number * 10) + second_number;
        calibration_values[i] = calibration_value;
    }

    int answer = 0;
    foreach(int value in calibration_values)
    {
        answer += value;
    }
    return answer;
}


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

    Console.WriteLine(Part1((string[])lines.Clone()));
    Console.WriteLine(Part2((string[])lines.Clone()));


}

Main();