CC  ?= gcc
SRC  = src
OBJ  = obj
LIB  = libs

EXEC	   = Haut
WARNINGS   = -Wall -Wextra -pedantic
NOWARNINGS = -w
DEBUG      = -g

IDIRS	 = -I$(SRC) -I$(SRC)/haut-html/include
LIBS	 =  -lrt -lpthread -lhaut -lcurl
LDIRS    = -L$(LIB)

CFLAGS     = $(IDIRS) -std=c11 $(WARNINGS) $(DEBUG)
CFASTFLAGS = $(IDIRS) -std=c11 $(NOWARNINGS) \
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

find	 = $(shell find $1 -type f -name $2 -print 2>/dev/null)

CSRCS   := $(call find, $(SRC)/, "*.c")
COBJS   := $(CSRCS:%.c=$(OBJ)/%.o)

CLEAR  = [0m
CYAN   = [1;36m
GREEN  = [1;32m
YELLOW = [1;33m
WHITE  = [1;37m

MAKEFLAGS = -j

FAST := $(filter fast,$(MAKECMDGOALS))

xoutofy = $(or $(eval PROCESSED := $(PROCESSED) .),$(info $(WHITE)[$(YELLOW)$(words $(PROCESSED))$(WHITE)] $1$(CLEAR)))

.PHONY: debug fast

fast: lib $(COBJS) $(CXXOBJS)
	@$(call xoutofy,$(GREEN)Linking fast $(EXEC))
	$(CC) $(CFASTFLAGS) $(COBJS) -o $(EXEC) $(LIBS) $(LDIRS)

debug: lib $(COBJS) $(CXXOBJS)
	@$(call xoutofy,$(GREEN)Linking debug $(EXEC))
	$(CC) $(CFLAGS) $(COBJS) -o $(EXEC) $(LIBS) $(LDIRS)


lib: $(COBJS)
	@$(call xoutofy,$(YELLOW)Linking haut library)
	mkdir -p $(LIB)
	ar rcs $(LIB)/libhaut.a $(OBJ)/$(SRC)/haut-html/src/haut.o $(OBJ)/$(SRC)/haut-html/src/string_util.o $(OBJ)/$(SRC)/haut-html/src/state_machine.o

$(OBJ)/%.o: %.c
	@$(call xoutofy,$(CYAN)Compiling $<)
	@mkdir -p $(dir $@)
	$(CC) $(if $(FAST),$(CFASTFLAGS),$(CFLAGS)) -o $@ -c $<

$(OBJ):
	mkdir -p $(OBJ)

clean:
	@echo Cleaning...
	@rm -rf $(OBJ) $(LIB) $(EXEC)
	@echo Done!

git: clean
	git add .
	git commit
	git push

c: clean