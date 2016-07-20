all: process_input

process_input: process_input.cc
	g++ -std=c++11 -Wall -Wextra -g \
		`root-config --libs` -lMinuit `root-config --cflags` \
		process_input.cc -o process_input
