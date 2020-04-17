CXX ?= g++
SRC  = src
OBJ  = obj

EXEC       = extractor
WARNINGS   = -Wall -Wextra -pedantic
NOWARNINGS = -w
DEBUG      = -g

IDIRS = -I$(SRC)
LIBS  =  -lrt -lpthread
LDIRS =

CXXFLAGS     = $(IDIRS) -std=c++11 $(WARNINGS) $(DEBUG)
CXXFASTFLAGS = $(IDIRS) -std=c++11 \
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

find = $(shell find $1 -type f -name $2 -print 2>/dev/null)

CXXSRCS := $(call find, $(SRC)/, "*.cpp")
CXXOBJS := $(CXXSRCS:%.cpp=$(OBJ)/%.o)

CLEAR  = [0m
CYAN   = [1;36m
GREEN  = [1;32m
YELLOW = [1;33m
WHITE  = [1;37m

MAKEFLAGS = -j

FAST := $(filter fast,$(MAKECMDGOALS))

xoutofy = $(or $(eval PROCESSED := $(PROCESSED) .),$(info $(WHITE)[$(YELLOW)$(words $(PROCESSED))$(WHITE)] $1$(CLEAR)))

.PHONY: debug fast

# Requests object creation, links, builds debug executable
debug: $(CXXOBJS)
	@$(call xoutofy,$(GREEN)Linking debug $(EXEC))
	$(CXX) $(CXXFLAGS) $(CXXOBJS) -o $(EXEC) $(LIBS) $(LDIRS)

# Requests object creation, links, builds fast executable
fast: $(CXXOBJS)
	@$(call xoutofy,$(GREEN)Linking fast $(EXEC))
	$(CXX) $(CXXFASTFLAGS) $(CXXOBJS) -o $(EXEC) $(LIBS) $(LDIRS)

# Compiles regular cpp files
$(OBJ)/%.o: %.cpp
	@$(call xoutofy,$(CYAN)Compiling $<)
	@mkdir -p $(dir $@)
	$(CXX) $(if $(FAST),$(CXXFASTFLAGS),$(CXXFLAGS)) -o $@ -c $<

$(OBJ):
	mkdir -p $(OBJ)

clean:
	@echo Cleaning...
	@rm -rf $(OBJ) $(EXEC)
	@echo Done!

git: clean
	git add .
	git commit
	git push

c: clean