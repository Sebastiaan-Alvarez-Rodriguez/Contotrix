CXX  ?= g++

EXEC       = Lexbor
WARNINGS   = -Wall -Wextra -pedantic
NOWARNINGS = -w
DEBUG      = -g

IDIRS    = -Ilibrary/source
LIBS     = -llexbor-core -llexbor-dom -llexbor-html -llexbor-ns -llexbor-tag
LDIRS    = -Llibrary
RPATH    = -Wl,-rpath library

CXXFLAGS     = $(IDIRS) -std=c++11 $(WARNINGS) $(DEBUG)
CXXFASTFLAGS = $(IDIRS) -std=c++11 $(NOWARNINGS) \
	-Ofast \
	-march=native \
	-ffast-math \
	-funsafe-math-optimizations \
	-fassociative-math \
	-freciprocal-math \
	-ffinite-math-only \
	-fno-signed-zeros \
	-fno-trapping-math \
	-funroll-loops


CLEAR  = [0m
CYAN   = [1;36m
GREEN  = [1;32m
YELLOW = [1;33m
WHITE  = [1;37m

MAKEFLAGS = -j

FAST := $(filter fast,$(MAKECMDGOALS))

xoutofy = $(or $(eval PROCESSED := $(PROCESSED) .),$(info $(WHITE)[$(YELLOW)$(words $(PROCESSED))$(WHITE)] $1$(CLEAR)))

.PHONY: debug fast

fast: main.o
	@$(call xoutofy,$(GREEN)Linking fast $(EXEC))
	$(CXX) $(CXXFASTFLAGS) main.o -o $(EXEC) $(LIBS) $(LDIRS) $(RPATH)

debug: main.o
	@$(call xoutofy,$(GREEN)Linking debug $(EXEC))
	$(CXX) $(CXXFLAGS) main.o -o $(EXEC) $(LIBS) $(LDIRS) $(RPATH)

main.o: main.cpp
	@$(call xoutofy,$(CYAN)Compiling $<)
	$(CXX) $(if $(FAST),$(CXXFASTFLAGS),$(CXXFLAGS)) -o $@ -c $< $(LIBS) $(LDIRS)


clean:
	@echo Cleaning...
	@rm -rf main.o $(EXEC)
	@echo Done!

c: clean