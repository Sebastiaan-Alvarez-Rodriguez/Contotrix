# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/radon/Uni/mir/final/wip/lexbor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/radon/Uni/mir/final/wip/lexbor

# Include any dependencies generated for this target.
include examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/depend.make

# Include the progress variables for this target.
include examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/progress.make

# Include the compile flags for this target's objects.
include examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/flags.make

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/flags.make
examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o: examples/lexbor/html/tokenizer/callback.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/radon/Uni/mir/final/wip/lexbor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o"
	cd /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o   -c /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html/tokenizer/callback.c

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.i"
	cd /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html/tokenizer/callback.c > CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.i

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.s"
	cd /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html/tokenizer/callback.c -o CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.s

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.requires:

.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.requires

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.provides: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.requires
	$(MAKE) -f examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/build.make examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.provides.build
.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.provides

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.provides.build: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o


# Object files for target examples_lexbor_html_tokenizer_callback
examples_lexbor_html_tokenizer_callback_OBJECTS = \
"CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o"

# External object files for target examples_lexbor_html_tokenizer_callback
examples_lexbor_html_tokenizer_callback_EXTERNAL_OBJECTS =

examples/lexbor/html/tokenizer/callback: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o
examples/lexbor/html/tokenizer/callback: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/build.make
examples/lexbor/html/tokenizer/callback: liblexbor.so.1.0.0
examples/lexbor/html/tokenizer/callback: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/radon/Uni/mir/final/wip/lexbor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable tokenizer/callback"
	cd /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/build: examples/lexbor/html/tokenizer/callback

.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/build

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/requires: examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/tokenizer/callback.c.o.requires

.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/requires

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/clean:
	cd /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html && $(CMAKE_COMMAND) -P CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/cmake_clean.cmake
.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/clean

examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/depend:
	cd /home/radon/Uni/mir/final/wip/lexbor && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html /home/radon/Uni/mir/final/wip/lexbor/examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/lexbor/html/CMakeFiles/examples_lexbor_html_tokenizer_callback.dir/depend
