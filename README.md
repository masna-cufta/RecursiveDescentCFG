## Recursive Descent Parser (LL(1))

This Python script implements a simple **recursive descent parser** for a custom context-free grammar.  
It reads an input string from standard input and determines whether it can be derived from the grammar using nonterminal functions (`S`, `A`, `B`, `C`).

### ✨ Features

- Implements LL(1) parsing using recursive functions
- Handles ε-productions (empty transitions)
- Tracks and prints the sequence of nonterminal symbols used
- Outputs `"YES"` if the input string is accepted, `"NO"` otherwise

### 📥 Input

The input should be a single line string (no whitespace or newlines) over the alphabet `{a, b, c}`.

Example:
abccabccbc

### 🚀 Usage

Run the script and provide input through standard input:

```bash
python parser.py
```

Then type or pipe the input string:
echo abccabccbc | python parser.py

### Output
The sequence of nonterminals visited (e.g., SABCBACAA)

YES if the input is accepted, NO if not
