# Standard Mode is release
MODE ?= release

# Base compiler and universal flags
CC = gcc
BASE_CFLAGS = -Wall -Wextra -pedantic -I./src

ifeq ($(MODE), debug)
    # -g: Adds debugging symbols
    # -O0: Disables all optimization so code matches source line-by-line
    # -DDEBUG: Defines a 'DEBUG' macro you can use
    CFLAGS = $(BASE_CFLAGS) -g -O0 -DDEBUG
    BUILD_DIR = build/debug

else ifeq ($(MODE), benchmark)
    # -O3: Aggressive optimization
    # -march=native: Optimizes instructions specifically for current CPU architecture
    # -flto: Link-time optimization
    # -DNDEBUG: Disables standard C asserts
	CFLAGS = $(BASE_CFLAGS) -O3 -march=native -flto -DNDEBUG
    BUILD_DIR = build/benchmark

else ifeq ($(MODE), release)
    # -O2: Standard optimization
    # -DNDEBUG: Disables standard C asserts
    CFLAGS = $(BASE_CFLAGS) -O2 -DNDEBUG
    BUILD_DIR = build/release

else
    $(error Unknown MODE: '$(MODE)'. Valid modes are: debug, release, benchmark)
endif

SRC_DIR   = src
TEST_DIR  = tests
OBJ_DIR   = $(BUILD_DIR)/obj
LIB_DIR   = $(BUILD_DIR)/lib
BIN_DIR   = $(BUILD_DIR)/bin

LIB = dsa
TARGET_LIB = $(LIB_DIR)/lib$(LIB).a

SRC_FILES = $(shell find $(SRC_DIR) -name '*.c')

OBJ_FILES = $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRC_FILES))

TEST_FILES = $(shell find $(TEST_DIR) -name '*.c')

TEST_BINS = $(patsubst $(TEST_DIR)/%.c, $(BIN_DIR)/%, $(TEST_FILES))

.PHONY: all
all: $(TARGET_LIB) $(TEST_BINS)

# Rule to build the static library
$(TARGET_LIB): $(OBJ_FILES)
	@mkdir -p $(dir $@)
	@echo "Compiling $@ into library"
	@ar rcs $@ $^

# Rule to compile source files into object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	@echo "Compiling $<"
	@$(CC) $(CFLAGS) -c $< -o $@

# Rule to compile test executables
$(BIN_DIR)/%: $(TEST_DIR)/%.c $(TARGET_LIB)
	@mkdir -p $(dir $@)
	@echo "Building test $@"
	@$(CC) $(CFLAGS) $< -L$(LIB_DIR) -l$(LIB) -o $@

# Target to run all tests
.PHONY: test
test: all
	@echo "Running all tests"
	@for test_bin in $(TEST_BINS); do \
		echo "Executing $$test_bin"; \
		./$$test_bin || exit 1; \
	done

.PHONY: clean
clean:
	echo "Cleaning build directory"
	rm -rf $(BUILD_DIR)
