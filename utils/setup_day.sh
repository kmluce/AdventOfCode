#!/bin/bash

BASE_PATH=$(find "$HOME/PycharmProjects" -type d -name AdventOfCode)
AOCD_PATH="venv/bin/"
TEMPLATE_DIR="$BASE_PATH/template"
AOCD_BIN="$BASE_PATH/$AOCD_PATH/aocd"
TMP_DIR="/tmp/aocd.$$"


# USAGE string
USAGE="$0    [ -y year ]  [ -d day ]  [-n]  [-x]  [-q]
       -y: year you want to set up (in 4-digit format)
       -d: day of month you want to set up
       -n: no copy templates, just fetch example data
       -x: don't execute, just show what would be done
       -q: quiet mode
Sets up today's (or some other day's) Advent of Code directory
"
COMMAND_LINE="$0 $*"  # save command line for error messages
MY_YEAR=0
MY_DAY=0
COPY_TEMPLATES=1
NO_EXECUTE=0
QUIET=0


## Functions
# Exit nicely on command line error, showing command line and passed-in
# error string
cl_exit_error () {
    echo "ERROR: $*"
    echo "your command line: $COMMAND_LINE"
    echo
    echo "USAGE: $USAGE"
    cleanup_exit
    exit 2
}

cleanup_exit() {
    rm -rf "$TMP_DIR"
}

## Main
# get options
while getopts "y:d:nxq" OPTION_NAME; do
    case "$OPTION_NAME" in
        y)     MY_YEAR="$OPTARG";;
        d)     MY_DAY="$OPTARG";;
        n)     COPY_TEMPLATES=0;;
        x)     NO_EXECUTE=1;;
        q)     QUIET=1;;
        [?])   echo "$USAGE"
               exit 2;;
    esac
done

if [ "$MY_YEAR" -eq 0 ]; then
    TZ="America/New_York" MY_YEAR=$(gdate "+%Y")
fi
if [ "$MY_DAY" -eq 0 ]; then
    TZ="America/New_York" MY_DAY=$(gdate "+%d")
fi

if [ "$MY_YEAR" -lt 2015 ] && [ "$MY_YEAR" -gt "$(gdate "+%Y")" ]; then
    cl_exit_error "Invalid year: $MY_YEAR"
fi
if [ "$MY_DAY" -lt 0 ] && [ "$MY_DAY" -gt 25 ]; then
    cl_exit_error "Invalid day: $MY_DAY.  No AOC today, so please specify a day via -d"
fi

if ! mkdir $TMP_DIR; then
    cl_exit_error "Could not create temporary directory $TMP_DIR"
fi

[ $QUIET -eq 0 ] && echo "Setting up directory for Advent of Code year $MY_YEAR, day $MY_DAY."
DATE_DIR=$(printf "%d/day_%02d" "$MY_YEAR" "$MY_DAY")
MY_DIR="$BASE_PATH/$DATE_DIR"

if [ -e "$MY_DIR" ] && [ $COPY_TEMPLATES -eq 1 ]; then
    [ $QUIET -eq 0 ] && echo "Directory $MY_DIR already exists.  Will not create"
elif [ $NO_EXECUTE -eq 1 ]; then
    echo "Would make directory $MY_DIR , except that -x was specified"
else
    echo "Making directory $MY_DIR"
    mkdir -p "$MY_DIR"
fi

if [ $NO_EXECUTE -eq 1 ]; then
    [ $QUIET -eq 0 ] && echo "Would copy -n template files, except that -x was specified"
else [ $COPY_TEMPLATES -eq 1 ]
	  [ $QUIET -eq 0 ] && echo "Copying template files from $TEMPLATE_DIR, unless files already exist"
	  cp -n "$TEMPLATE_DIR"/* "$MY_DIR"
fi

[ $QUIET -eq 0 ] && echo "Getting test data"
"$AOCD_BIN" "$MY_DAY" "$MY_YEAR" > "$TMP_DIR"/test_data.txt
[ $QUIET -eq 0 ] && echo "Getting example data"
EXAMPLE_FILE="$TMP_DIR/example.txt"
"$AOCD_BIN" "$MY_DAY" "$MY_YEAR" --example > "$EXAMPLE_FILE"
NO_EXAMPLES=$(grep -- '-- Example data 1/' "$EXAMPLE_FILE" | cut -f2 -d"/" | cut -f1 -d" ")

[ $QUIET -eq 0 ] && echo "there are $NO_EXAMPLES examples in $EXAMPLE_FILE"
for i in $(seq "$NO_EXAMPLES"); do
	  [ $QUIET -eq 0 ] && echo "finding example $i"
	  sed "1,/^--* Example data $i/d;/^--/,\$d" "$EXAMPLE_FILE" > "$TMP_DIR/demo_data${i}.txt"
	  [ $QUIET -eq 0 ] && echo "finding answers for example $i"
	  sed "1,/^--* Example data $i/d" "$EXAMPLE_FILE" | sed '1,/^---*/d;/^---*/,$d' > "$TMP_DIR/demo_answers${i}.txt"
done

for file in "$TMP_DIR"/*; do
    if [ $NO_EXECUTE -eq 1 ]; then
        [ $QUIET -eq 0 ] && echo "Would copy $file to $MY_DIR, except that -x was specified"
    else
        [ $QUIET -eq 0 ] && echo "Copying $file to $MY_DIR, unless file already exists"
        cp -n "$file" "$MY_DIR"
    fi
done

cleanup_exit
