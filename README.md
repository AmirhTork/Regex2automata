# Regex2Automata

## Overview
Regex2Automata is a Python project that converts **regular expressions (regex)** into **Non-deterministic Finite Automata (NFA)** and **Deterministic Finite Automata (DFA)**.  
It also supports **DFA minimization** and **visualization** of both NFA and DFA as high-quality graphs.  

This tool is designed for academic purposes and demonstrates practical implementation of automata theory, useful for compiler construction, formal language analysis, and computer science research.

---

## Features
- Convert any valid regex to **NFA**.
- Convert NFA to **DFA** using the subset construction algorithm.
- **Minimize DFA** to reduce states while preserving language.
- **Visualize automata** with Graphviz (`.png` outputs with timestamps for uniqueness).
- Fully **modular** design, suitable for CLI or library usage.
- Timestamped outputs prevent overwriting and keep results organized.

---

## Installation
You can install Regex2Automata via `pip`:

```
pip install regex2automata
```

---

## Usage

### As a CLI
After installation, you can run:

```
regex2automata
```

Follow the prompt to enter your regular expression. The program will:
1. Validate the regex
2. Generate NFA and DFA
3. Minimize the DFA
4. Save all visualizations to a `plots/` folder with timestamped filenames

---

### As a Python library
You can also use it programmatically:

```
from automata.regex_utils import validate_regex, regex_to_postfix
from automata.nfa import postfix_to_nfa
from automata.dfa import nfa_to_dfa, minimize_dfa
from automata.visualizer import AutomatonVisualizer

regex = "a(b|c)*d"
validate_regex(regex)

postfix = regex_to_postfix(regex)
nfa_start = postfix_to_nfa(postfix)

dfa = nfa_to_dfa(nfa_start)
minimized = minimize_dfa(dfa)

# Visualize and save plots
nfa_file = AutomatonVisualizer.visualize_nfa(nfa_start)
dfa_file = AutomatonVisualizer.visualize_dfa(dfa)
min_dfa_file = AutomatonVisualizer.visualize_dfa(minimized)

print("NFA saved to:", nfa_file)
print("DFA saved to:", dfa_file)
print("Minimized DFA saved to:", min_dfa_file)
```

All outputs are automatically timestamped to prevent overwriting.

---

## Project Structure

```
regex2automata/
├─ automata/
│ ├─ regex_utils.py # Regex validation and conversion to postfix
│ ├─ nfa.py # Postfix to NFA conversion
│ ├─ dfa.py # NFA to DFA and DFA minimization
│ └─ visualizer.py # NFA/DFA visualization
│
│
├─ requirements.txt
├─ setup.py
├─ main.py
├─ cli.py # Command-line interface entry point
├─ README.md
└─ LICENSE
```


---

## Dependencies
- Python >= 3.8
- `graphviz` for visualizations
- `setuptools` for package installation

You can install dependencies via:

```
pip install -r requirements.txt
```

---

## License
MIT License — see the LICENSE file for details.


---

## Notes
- All filenames of plots include timestamps for uniqueness.  
- Modular structure allows easy extension or integration into larger projects.  
- This project demonstrates practical understanding of formal languages, automata theory, and Python programming skills, making it suitable for top-tier university internship submissions.

