# 开发时间：2023/12/4 17:44
import pandas as pd
from collections import deque


def get_nfa(input_data):
    # 初始化字典
    nfa = {
        'start': None,
        'final': set(),
        'symbols': set(),
        'transitions': {}
    }

    # 解析数据
    for i, line in enumerate(input_data):
        parts = line.split()

        if i == 1:
            nfa['final'].update(parts)
        else:
            if i == 0:
                nfa['start'] = parts[0]
            state = parts[0]
            for part in parts[1:]:
                if "->" in part:
                    symbol, next_state = part.split("->")
                    symbol = symbol.split("-")[-1]
                    nfa['symbols'].add(symbol)

                    if state not in nfa['transitions']:
                        nfa['transitions'][state] = {}
                    if symbol not in nfa['transitions'][state]:
                        nfa['transitions'][state][symbol] = []

                    nfa['transitions'][state][symbol].append(next_state)

    nfa['symbols'].discard('~')

    # 转换状态键为整数或保持为字符串（对于 'X' 和 'Y'）
    for state in list(nfa['transitions'].keys()):
        new_state = int(state) if state.isdigit() else state
        nfa['transitions'][new_state] = nfa['transitions'].pop(state)
        for symbol in nfa['transitions'][new_state]:
            nfa['transitions'][new_state][symbol] = \
                [int(ns) if ns.isdigit() else ns for ns in nfa['transitions'][new_state][symbol]]
    return nfa


def epsilon_closure(nfa, states):
    epsilon_closure_set = set(states)
    stack = list(states)

    while stack:
        current_state = stack.pop()
        epsilon_transitions = nfa.get(current_state, {}).get('~', [])
        for state in epsilon_transitions:
            if state not in epsilon_closure_set:
                epsilon_closure_set.add(state)
                stack.append(state)

    return frozenset(epsilon_closure_set)


def nfa_to_dfa(nfa):
    dfa = {}
    # 求x空闭包
    nfa_states = set([nfa['start']])
    dfa_start_state = epsilon_closure(nfa['transitions'], nfa_states)
    dfa_states = {dfa_start_state}
    queue = deque([dfa_start_state])

    epsilon_closure_order = [dfa_start_state]

    while queue:
        current_state = queue.popleft()

        for symbol in sorted(list(nfa['symbols'])):
            # 求出经过symbol的子集
            next_states = set()
            for nfa_state in current_state:
                transitions = nfa['transitions'].get(nfa_state, {}).get(symbol, [])
                next_states.update(transitions)
            # 求出经过symbol的子集的空闭包
            epsilon_closure_set = epsilon_closure(nfa['transitions'], next_states)
            if epsilon_closure_set:
                if epsilon_closure_set not in dfa_states:
                    dfa_states.add(epsilon_closure_set)
                    queue.append(epsilon_closure_set)
                    epsilon_closure_order.append(epsilon_closure_set)

                dfa[current_state, symbol] = epsilon_closure_set

    dfa_final_states = {state for state in dfa_states if state.intersection(nfa['final'])}

    return {
        'start': dfa_start_state,
        'states': dfa_states,
        'symbols': nfa['symbols'],
        'transitions': dfa,
        'final': dfa_final_states,
        'epsilon_closure_order': epsilon_closure_order
    }


if __name__ == '__main__':

    input_data = []
    while True:
        try:
            line = input()
            if not line:
                break
            input_data.append(line)
        except Exception:
            break

    nfa = get_nfa(input_data)
    dfa = nfa_to_dfa(nfa)

    order = dfa['epsilon_closure_order']
    # 将每个 frozenset 状态映射到其在 order 中的位置
    state_mapping = {order[0]: 'X', order[-1]: 'Y'}

    for i, state in enumerate(order):
        if state not in state_mapping:
            state_mapping[state] = i - 1

    # 创建二维列表来保存化简后的 DFA
    simplified_dfa = []

    # 遍历 DFA 的转换
    for (current_state, symbol), next_state in dfa['transitions'].items():
        current_label = state_mapping[current_state]
        next_label = state_mapping[next_state]
        simplified_dfa.append([current_label, symbol, next_label])

    state_expressions = {}

    for transition in simplified_dfa:
        state = transition[0]
        symbol = transition[1]
        next_state = transition[2]

        # 构建表达式
        expression = f"{state}-{symbol}->{next_state}"

        # 如果状态已存在于字典中，则追加表达式，否则创建新的表达式列表
        if state in state_expressions:
            state_expressions[state].append(expression)
        else:
            state_expressions[state] = [expression]

    for state, expressions in state_expressions.items():
        if state == 'X':
            print(f"{state} {' '.join(expressions)}")
            if 'Y' in state_expressions:
                print(f"Y {' '.join(state_expressions['Y'])}")
            else:
                print('Y')
        elif state == 'Y':
            continue
        else:
            print(f"{state} {' '.join(expressions)}")
