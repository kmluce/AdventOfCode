#!/bin/bash

TEMPLATE_DIR=template


# USAGE string
USAGE="$0    [ -y year ]  [ -d day ]
        -y: year you want to set up (in 4-digit format)
        -d: day of month you want to set up
    Sets up today's (or some other day's) Advent of Code directory
"
COMMAND_LINE="$0 $*"  # save command line for error messages
MY_YEAR=0
MY_DAY=0


## Functions
# Exit nicely on command line error, showing command line and passed-in
# error string
cl_exit_error () {
    echo "ERROR: $*"
    echo "your command line: $COMMAND_LINE"
    echo "USAGE: $USAGE"
    exit 2
}

## Main
# get options
while getopts "y:d:" OPTION_NAME; do
    case "$OPTION_NAME" in
        y)     MY_YEAR="$OPTARG";;
        d)     MY_DAY="$OPTARG";;
        [?])   echo "$USAGE"
               exit 2;;
    esac
done

if [ "$MY_YEAR" -eq 0 ]; then
   MY_YEAR=$(gdate -d"now + 2 hours" "+%Y")
fi
if [ "$MY_DAY" -eq 0 ]; then
   MY_DAY=$(gdate -d"now + 2 hours" "+%d")
fi

if [ "$MY_YEAR" -lt 2015 ] || [ "$MY_YEAR" -gt "$(gdate "+%Y")" ]; then
    cl_exit_error "Invalid year: $MY_YEAR"
fi
if [ "$MY_DAY" -lt 0 ] || [ "$MY_DAY" -gt 25 ]; then
    cl_exit_error "Invalid day: $MY_DAY"
fi

echo "Setting up directory for Advent of Code year $MY_YEAR, day $MY_DAY."
MY_DIR=$(printf "%d/day_%02d" "$MY_YEAR" "$MY_DAY")
echo "Making directory"
mkdir -p "$MY_DIR"
echo "Copying template directory"
cp $TEMPLATE_DIR/* "$MY_DIR"
echo "Getting data"
./venv/bin/aocd "$MY_DAY" "$MY_YEAR" > "$MY_DIR"/test_data.txt
echo "Getting example data"
EXAMPLE_FILE="$MY_DIR/example.txt"
./venv/bin/aocd "$MY_DAY" "$MY_YEAR" --example > "$EXAMPLE_FILE"
NO_EXAMPLES=$(grep -- '-- Example data 1/' "$EXAMPLE_FILE" | cut -f2 -d"/" | cut -f1 -d" ")

echo "there are $NO_EXAMPLES examples in $EXAMPLE_FILE"
for i in $(seq "$NO_EXAMPLES"); do
	echo "finding example $i"
	sed "1,/^--* Example data $i/d;/^--/,\$d" "$EXAMPLE_FILE" > "$MY_DIR/demo_data${i}.txt"
	echo "finding answers for example $i"
	sed "1,/^--* Example data $i/d" "$EXAMPLE_FILE" | sed '1,/^---*/d;/^---*/,$d' > "$MY_DIR/demo_answers${i}.txt"
done

