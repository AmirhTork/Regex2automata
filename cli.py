import argparse
from regex2automata.lexer import Lexer
from regex2automata.parser import Parser
from regex2automata.nfa import NFA
from regex2automata.dfa import DFA
from regex2automata.minimize import MinimizedDFA
from regex2automata.visualize import visualize_automaton


def convert_regex(regex, visualize=False, out=None):
    # Tokenize
    lexer = Lexer(regex)
    tokens = lexer.tokenize()

    # Parse
    parser = Parser(tokens)
    syntax_tree = parser.parse()

    # Build NFA
    nfa = NFA.from_regex_tree(syntax_tree)

    # Build DFA
    dfa = DFA.from_nfa(nfa)

    # Minimize DFA
    min_dfa = MinimizedDFA.from_dfa(dfa)

    if visualize:
        if out is None:
            out = "automata"
        visualize_automaton(nfa, f"{out}_nfa")
        visualize_automaton(dfa, f"{out}_dfa")
        visualize_automaton(min_dfa, f"{out}_min_dfa")

    return nfa, dfa, min_dfa


def print_automaton(title, automaton):
    print("=" * 40)
    print(title)
    print("=" * 40)
    print(automaton)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Convert a Regular Expression into NFA, DFA, and Minimized DFA."
    )

    parser.add_argument(
        "regex",
        type=str,
        help="The regular expression to convert. Example: '(a|b)*abb'"
    )

    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Generate GraphViz visualizations (saved as .png files)."
    )

    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output filename prefix for visualization (default: 'automata')."
    )

    args = parser.parse_args()

    try:
        nfa, dfa, min_dfa = convert_regex(
            regex=args.regex,
            visualize=args.visualize,
            out=args.out,
        )
    except Exception as e:
        print("❌ Error:", str(e))
        exit(1)

    # Print readable automata
    print_automaton("NFA", nfa)
    print_automaton("DFA", dfa)
    print_automaton("Minimized DFA", min_dfa)
