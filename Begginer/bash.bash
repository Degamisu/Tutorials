# Bash is widely used for scripting in Unix-like operating systems.
# When I use Bash, I usually make installers out of it.
# For this program, we will learn about Variables and Syntax Commands.
# Lets start!

echo "What's your name?"
read name  # This reads a line from standard input (the keyboard) and stores it into the variable 'name'.
           # The prompt "What's your name" is printed to the terminal before reading the input.

echo "Nice to meet you $name!"   # This prints text with variables substituted by their values. '$name' gets replaced by whatever was typed at the keyboard.
input()