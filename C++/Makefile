ksum: helpers.h
	g++ -std=c++11 -o $@.exe $@.cpp 

int_to_roman:
	g++ -std=c++11 -o $@.exe $@.cpp 

trap_water: helpers.o
	g++ -std=c++11 -o $@.exe $@.cpp helpers.o

longest_par: helpers.o
	g++ -std=c++11 -o $@.exe $@.cpp helpers.o

helpers.o: helpers.cpp
	g++ -std=c++11 -c helpers.cpp

autocomplete:
	g++ -std=c++11 -o autocomplete.exe autocomplete.cpp