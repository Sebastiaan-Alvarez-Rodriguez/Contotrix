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
include CMakeFiles/lexbor-ns.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/lexbor-ns.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/lexbor-ns.dir/flags.make

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o: CMakeFiles/lexbor-ns.dir/flags.make
CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o: source/lexbor/ns/ns.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/radon/Uni/mir/final/wip/lexbor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o   -c /home/radon/Uni/mir/final/wip/lexbor/source/lexbor/ns/ns.c

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/radon/Uni/mir/final/wip/lexbor/source/lexbor/ns/ns.c > CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.i

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/radon/Uni/mir/final/wip/lexbor/source/lexbor/ns/ns.c -o CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.s

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.requires:

.PHONY : CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.requires

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.provides: CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.requires
	$(MAKE) -f CMakeFiles/lexbor-ns.dir/build.make CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.provides.build
.PHONY : CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.provides

CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.provides.build: CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o


# Object files for target lexbor-ns
lexbor__ns_OBJECTS = \
"CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o"

# External object files for target lexbor-ns
lexbor__ns_EXTERNAL_OBJECTS =

liblexbor-ns.so.1.2.0: CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o
liblexbor-ns.so.1.2.0: CMakeFiles/lexbor-ns.dir/build.make
liblexbor-ns.so.1.2.0: liblexbor-core.so.1.3.1
liblexbor-ns.so.1.2.0: CMakeFiles/lexbor-ns.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/radon/Uni/mir/final/wip/lexbor/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library liblexbor-ns.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lexbor-ns.dir/link.txt --verbose=$(VERBOSE)
	$(CMAKE_COMMAND) -E cmake_symlink_library liblexbor-ns.so.1.2.0 liblexbor-ns.so.1 liblexbor-ns.so

liblexbor-ns.so.1: liblexbor-ns.so.1.2.0
	@$(CMAKE_COMMAND) -E touch_nocreate liblexbor-ns.so.1

liblexbor-ns.so: liblexbor-ns.so.1.2.0
	@$(CMAKE_COMMAND) -E touch_nocreate liblexbor-ns.so

# Rule to build all files generated by this target.
CMakeFiles/lexbor-ns.dir/build: liblexbor-ns.so

.PHONY : CMakeFiles/lexbor-ns.dir/build

CMakeFiles/lexbor-ns.dir/requires: CMakeFiles/lexbor-ns.dir/source/lexbor/ns/ns.c.o.requires

.PHONY : CMakeFiles/lexbor-ns.dir/requires

CMakeFiles/lexbor-ns.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/lexbor-ns.dir/cmake_clean.cmake
.PHONY : CMakeFiles/lexbor-ns.dir/clean

CMakeFiles/lexbor-ns.dir/depend:
	cd /home/radon/Uni/mir/final/wip/lexbor && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor /home/radon/Uni/mir/final/wip/lexbor/CMakeFiles/lexbor-ns.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/lexbor-ns.dir/depend

