#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdlib>

struct Instruction {
    char dir; // 'L' or 'R'
    int steps;
};

int wrap(int x) {
    x %= 100;
    if (x < 0) x += 100;
    return x;
}

Instruction parse(const std::string& s) {
    Instruction ins;
    ins.dir = s[0];
    ins.steps = std::atoi(s.c_str() + 1);
    return ins;
}

std::vector<std::string> read_input(const char* filename) {
    std::ifstream f(filename);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(f, line)) {
        if (!line.empty())
            lines.push_back(line);
    }
    return lines;
}

// Counts zero crossings if count_all is true, else counts landing on zero
long solve(const std::vector<std::string>& lines, bool count_all) {
    std::vector<Instruction> instrs;
    for (size_t i = 0; i < lines.size(); ++i)
        instrs.push_back(parse(lines[i]));

    int pos = 50;
    long pw = 0;

    for (size_t i = 0; i < instrs.size(); ++i) {
        Instruction ins = instrs[i];
        int delta = (ins.dir == 'L') ? 1 : -1;

        if (count_all) {
            for (int step = 1; step <= ins.steps; ++step) {
                int p = wrap(pos + delta * step);
                if (p == 0) ++pw;
            }
        }

        pos = wrap(pos + (ins.dir == 'L' ? ins.steps : -ins.steps));

        if (!count_all && pos == 0)
            ++pw;
    }

    return pw;
}

int main() {
    std::vector<std::string> lines = read_input("input.txt");

    long part1 = solve(lines, false);
    long part2 = solve(lines, true);

    std::cout << "Part 1: " << part1 << ", Part 2: " << part2 << "\n";
}
