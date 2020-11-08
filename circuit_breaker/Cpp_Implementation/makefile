CC = g++
CONF = -std=c++17 
LINK = -ltbb
INC = -I./src -I./scripts -I./
CFLAGS = -Wall -O2
CXXFLAGS = $(CONF) $(INC)  
EXPORTED_FUNCTIONS = ""

all: main

# Main
main: main.o scripts/szenarios.o src/model.o src/solver.o src/timeDependentParameter.o src/utils.o
	$(CC) $(CXXFLAGS) -o main.exec main.o scripts/szenarios.o src/model.o src/solver.o src/timeDependentParameter.o src/utils.o $(LINK)
main.o: main.cpp
	$(CC) $(CXXFLAGS) -c main.cpp $(LINK)

# Scripts
szenarios.o: scripts/szenarios.cpp scripts/scripts.h
	$(CC) $(CXXFLAGS) -c scripts/szenarios.cpp $(LINK)


# Src
model.o: model.cpp model.h
	$(CC) $(CXXFLAGS) -c model.cpp $(LINK)

solver.o: solver.cpp solver.h
	$(CC) $(CXXFLAGS) -c solver.cpp $(LINK)

timeDependentParameter.o: timeDependentParameter.cpp timeDependentParameter.h
	$(CC) $(CXXFLAGS) -c timeDependentParameter.cpp $(LINK)

utils.o: utils.cpp utils.h
	$(CC) $(CXXFLAGS) -c utils.cpp $(LINK)


# Other
clean:
	find . -name "*.o" -type f -delete
	find . -name "*.exec" -type f -delete
	
new: clean all
	