import os
from datetime import datetime
from graphviz import Digraph

class AutomatonVisualizer:

    @staticmethod
    def get_timestamp():
        """Return a timestamp string suitable for filenames."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def visualize_dfa(dfa, name, directory="plots"):
        name = name
        os.makedirs(directory, exist_ok=True)
        filename = f"{name}_{AutomatonVisualizer.get_timestamp()}"
        filepath = os.path.join(directory, filename)

        dot = Digraph(comment="DFA")
        dot.attr(rankdir='LR')

        for s in dfa["states"]:
            dot.node(str(s),
                     shape="doublecircle" if s in dfa["finals"] else "circle")

        dot.node("start", shape="none", label="")
        dot.edge("start", str(dfa["start"]))

        for src, trans in dfa["transitions"].items():
            for sym, dst in trans.items():
                dot.edge(str(src), str(dst), label=sym)

        dot.render(filepath, view=True, format="png", cleanup=True)

    @staticmethod
    def visualize_nfa(start_state, directory="plots"):
        os.makedirs(directory, exist_ok=True)
        filename = f"nfa_{AutomatonVisualizer.get_timestamp()}"
        filepath = os.path.join(directory, filename)

        dot = Digraph(format="png")
        dot.attr(rankdir="LR")

        ids = {}
        counter = [0]

        def get_id(st):
            if st not in ids:
                ids[st] = f"State_{counter[0]}"
                counter[0] += 1
            return ids[st]

        visited = set()

        def dfs(state):
            sid = get_id(state)
            if sid in visited:
                return
            visited.add(sid)

            shape = "doublecircle" if state.is_final else "circle"
            dot.node(sid, shape=shape)

            for sym, targets in state.edges.items():
                for t in targets:
                    dot.edge(sid, get_id(t), label=sym if sym else "ε")
                    dfs(t)

        dot.node("start", shape="none", label="")
        dot.edge("start", get_id(start_state))

        dfs(start_state)
        dot.render(filepath, view=True, format="png", cleanup=True)