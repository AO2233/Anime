//
// Created by ao on 2022/3/13.
//

#include <bits/stdc++.h>
#include <argparse/argparse.hpp>

int main(int argc, char *argv[]) {
    argparse::ArgumentParser program("secret");

    program.add_argument("mode")
            .help("choose the mode: 0 encrypt 1 decrypt")
            .scan<'i', int>().required();

    program.add_argument("-i")
            .help("choose the input file path");

    program.add_argument("-o")
            .help("choose the output file path");

    try {
        program.parse_args(argc, argv);
    }
    catch (const std::runtime_error &err) {
        std::cerr << err.what() << std::endl;
        std::cerr << program;
        std::exit(1);
    }

    auto mode = program.get<int>("mode");
    auto i_file_path = program.present("-i");
    auto o_file_path = program.present("-o");

    if(i_file_path)
        freopen(i_file_path->data(),"rb",stdin);
    else
        std::cout << "input the code" << std::endl;

    if(o_file_path)
        freopen(o_file_path->data(),"wb",stdout);

    if (mode == 1) {
        std::bitset<8> bit8;
        while (std::cin >> bit8) {
            std::cout << static_cast<char>(bit8.to_ulong());
        }
    } else {
        int t;
        while ((t = std::fgetc(stdin)) != EOF) {
            std::string m;
            std::cout<<std::bitset<8>(t);
        }
    std::fclose(stdout);
    std::fclose(stdin);
    return 0;}
}
