from collections import deque

def nfa_to_dfa(nfa_start_state):
    dfa_map = {}
    queue = deque()
    names = {}
    alphabet = set()
    final_states = set()
    transitions = {}

    from .nfa import epsilon_closure

    start_closure = frozenset(epsilon_closure({nfa_start_state}))
    dfa_map[start_closure] = 0
    names[0] = "State_0"

    queue.append(start_closure)

    while queue:
        closure = queue.popleft()
        state_id = dfa_map[closure]
        transitions[state_id] = {}

        # discover alphabet
        for s in closure:
            for sym in s.edges:
                if sym:
                    alphabet.add(sym)

        for sym in alphabet:
            next_states = set()
            for s in closure:
                if sym in s.edges:
                    from .nfa import epsilon_closure
                    next_states.update(epsilon_closure(s.edges[sym]))

            if next_states:
                frozen_next = frozenset(next_states)
                if frozen_next not in dfa_map:
                    new_id = len(dfa_map)
                    dfa_map[frozen_next] = new_id
                    names[new_id] = f"State_{new_id}"
                    queue.append(frozen_next)

                transitions[state_id][sym] = dfa_map[frozen_next]

        if any(s.is_final for s in closure):
            final_states.add(state_id)

    return {
        "states": list(range(len(dfa_map))),
        "state_names": names,
        "alphabet": list(alphabet),
        "start": 0,
        "finals": list(final_states),
        "transitions": transitions
    }


def minimize_dfa(dfa: dict) -> dict:
    final = set(dfa['finals'])
    nonfinal = set(dfa['states']) - final
    partitions = [final, nonfinal]

    state_class = {s: i for i, part in enumerate(partitions) for s in part}

    stable = False
    while not stable:
        stable = True
        new_parts = []

        for part in partitions:
            groups = {}
            for s in part:
                signature = tuple(
                    state_class.get(dfa['transitions'].get(s, {}).get(sym))
                    for sym in dfa['alphabet']
                )
                groups.setdefault(signature, []).append(s)

            if len(groups) > 1:
                stable = False
                new_parts.extend(groups.values())
            else:
                new_parts.append(part)

        partitions = new_parts
        state_class = {s: i for i, part in enumerate(partitions) for s in part}

    minimized = {
        "states": list(range(len(partitions))),
        "alphabet": dfa['alphabet'],
        "start": state_class[dfa['start']],
        "finals": [],
        "state_names": {},
        "transitions": {}
    }

    for idx, part in enumerate(partitions):
        minimized["state_names"][idx] = f"State_{idx}"
        if any(s in final for s in part):
            minimized["finals"].append(idx)

    for old, new in state_class.items():
        for sym, tgt in dfa["transitions"].get(old, {}).items():
            minimized["transitions"].setdefault(new, {})[sym] = state_class[tgt]

    return minimized
