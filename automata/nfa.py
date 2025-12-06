from collections import defaultdict
from collections import deque

class State:
    def __init__(self):
        self.edges = defaultdict(list)
        self.is_final = False


class Fragment:
    def __init__(self, start_state, end_state):
        self.start_state = start_state
        self.end_state = end_state


def postfix_to_nfa(postfix: str) -> State:
    stack = []

    for token in postfix:
        if token.isalnum():
            start = State()
            end = State()
            start.edges[token].append(end)
            stack.append(Fragment(start, end))

        elif token == '.':
            b = stack.pop()
            a = stack.pop()
            for sym, targets in b.start_state.edges.items():
                a.end_state.edges[sym].extend(targets)
            stack.append(Fragment(a.start_state, b.end_state))

        elif token == '|':
            b = stack.pop()
            a = stack.pop()
            start = State()
            end = State()
            start.edges[''].extend([a.start_state, b.start_state])
            a.end_state.edges[''].append(end)
            b.end_state.edges[''].append(end)
            stack.append(Fragment(start, end))

        elif token == '*':
            frag = stack.pop()
            start = State()
            end = State()
            start.edges[''].extend([frag.start_state, end])
            frag.end_state.edges[''].extend([frag.start_state, end])
            stack.append(Fragment(start, end))

        elif token == '+':
            frag = stack.pop()
            start = State()
            end = State()
            start.edges[''].append(frag.start_state)
            frag.end_state.edges[''].extend([frag.start_state, end])
            stack.append(Fragment(start, end))

    final = stack.pop()
    final.end_state.is_final = True
    return final.start_state


def epsilon_closure(states: set) -> set:
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()
        if '' in state.edges:
            for nxt in state.edges['']:
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
    return closure
