from automata.regex_utils import validate_regex, regex_to_postfix
from automata.nfa import postfix_to_nfa
from automata.dfa import nfa_to_dfa, minimize_dfa
from automata.visualizer import AutomatonVisualizer


def main():
    regex = input("Enter regular expression: ")
    validate_regex(regex)

    postfix = regex_to_postfix(regex)
    nfa_start = postfix_to_nfa(postfix)

    dfa = nfa_to_dfa(nfa_start)
    minimized = minimize_dfa(dfa)

    print("Minimized DFA:")
    print("States:", minimized["states"])
    print("Start:", minimized["start"])
    print("Final States:", minimized["finals"])
    print("Transitions:", minimized["transitions"])

    AutomatonVisualizer.visualize_nfa(nfa_start)
    AutomatonVisualizer.visualize_dfa(dfa, "dfa")
    AutomatonVisualizer.visualize_dfa(minimized, "minimized_dfa")



if __name__ == "__main__":
    main()
