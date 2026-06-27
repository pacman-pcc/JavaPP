import sys
# LIBS
VARIABLES = {} # Variables
CONSTANTS = set() # constants
STRUCT_DEFS = {} # Structs
ARRAYS = {} # ARRAYS
LOOP_STACK = []

def get_parsed_value(x): # function parsed value
    x = x.strip().replace("{", "").strip()

    if x.endswith(';'):
        x = x[:-1].strip()

    if x.startswith('"') and x.endswith('"!'):
        return x[1:-2]
    if x.startswith('"') and x.endswith('"'):
        return x[1:-1]
    if x.replace('.', '', 1).isdigit():
        return float(x) if '.' in x else int(x)
    if x == "true": return True
    if x == "false": return False

    if x in VARIABLES:
        return VARIABLES[x]

    if '[' in x and x.endswith(']'):
        arr_name = x.split('[')[0].strip()
        idx = int(x.split('[')[1].replace(']', '').strip())

        if arr_name in ARRAYS:
            return ARRAYS[arr_name][idx]
    return x

def run_instructions(lines): # based function
    line_idx = 0
    while line_idx < len(lines):
        line = lines[line_idx].strip()
        # print(f"DEBUG: Index {line_idx}, command {line}")

        if line.endswith(';'):
            line = line[:-1].strip()

        if line.startswith("@USING") or not line:
            line_idx += 1
            continue

        if line.startswith("new.variables.create.stack"):
            clean = line.replace("new.variables.create.stack", "").replace(';', "").strip()
            parts = clean.split("=")
            left_side = parts[0].strip().split()

            var_name = left_side[0]
            if var_name in CONSTANTS:
                print(f"Error: Re-Wrote constant {var_name}!")
                sys.exit(1)

            VARIABLES[var_name] = get_parsed_value(parts[1])
            line_idx += 1

        elif line.startswith("new.constant.create.stack"):
            clean = line.replace("new.constant.create.stack", "").replace(";", "").strip()
            parts = clean.split("=")
            left_side = parts[0].strip().split()

            const_name = left_side[0]
            VARIABLES[const_name] = get_parsed_value(parts[1])
            CONSTANTS.add(const_name)
            line_idx += 1

        elif line.startswith("print.consolewrite.puts"):
            start = line.find('(') + 1
            end = line.rfind(')')
            content = line[start:end].strip()
            print(get_parsed_value(content))
            line_idx += 1

        elif line.startswith("new.if.typedefender"):
            # print("DEGUB IF:", VARIABLES)
            start = line.find('(') + 1
            end = line.rfind(')')
            condition = line[start:end].strip()

            parts = condition.split()
            var_val = VARIABLES.get(parts[0], get_parsed_value(parts[0]))
            op = parts[1]
            target_val = get_parsed_value(parts[2])

            is_true = False
            if op == "==": is_true = (var_val == target_val)
            elif op == ">": is_true = (var_val > target_val)
            elif op == "<": is_true = (var_val < target_val)

            if is_true:
                line_idx += 1
                continue
            else:
                while line_idx < len(lines) and "}" not in lines[line_idx]:
                    line_idx += 1

        elif "quit.program.uwu" in line:
            start = line.find('(') + 1
            end = line.rfind(')')
            code = line[start:end].strip()
            sys.exit(int(code))
            line_idx += 1

        elif line.startswith("__class__"):
            clean = line.replace("__clase__", "").replace("{", "").replace("in", "").strip()
            struct_name = clean

            STRUCT_DEFS[struct_name] = {}
            line_idx += 1

            while line_idx < len(lines) and "};" not in lines[line_idx]:
                struct_line = lines[line_idx].strip()
                if struct_line and ":" in struct_line:
                    if struct_line.endswith(":"):
                        struct_line = struct_line[:-1]

                    field_parts = struct_line.split(":")
                    field_name = field_parts[0].strip()
                    field_type = field_parts[1].strip()

                    STRUCT_DEFS[struct_name][field_name] = field_type
                line_idx += 1

        elif line.startswith("new.array"):
            clean = line.replace("new.array", "").replace(";", "").strip()
            parts = clean.split("=")

            left_side = parts[0].strip().split()
            arr_name = left_side[0]
            arr_len_raws = left_side[1]

            right_side = parts[1].strip()
            start_bracket = right_side.find('{') + 1
            end_bracket = right_side.rfind('}')
            elements_raw = right_side[start_bracket:end_bracket].split(',')

            elements = [get_parsed_value(el) for el in elements_raw if el.strip()]

            if arr_len_raws != "_":
                target_len = int(arr_len_raws)
                while len(elements) < target_len:
                    elements.append(0)

            ARRAYS[arr_name] = elements
            line_idx += 1

        elif ".append" in line:
            arr_name = line.split(".append")[0].strip()

            start = line.find('(') + 1
            end = line.rfind(')')
            val_to_append = line[start:end].strip()

            if arr_name in ARRAYS:
                ARRAYS[arr_name].append(get_parsed_value(val_to_append))
            else:
                print(f"Error: Array {arr_name} not found!")
                sys.exit(1)
            line_idx += 1
        elif line.startswith("new.looping"):
            start = line.find('(') + 1
            end = line.rfind(')')
            condition = line[start:end].strip()

            is_true = get_parsed_value(condition)

            if is_true == True or is_true == "true":
                LOOP_STACK.append(("while", line_idx, condition))
                line_idx += 1
            else:
                while line_idx < len(lines) and "}" not in lines[line_idx]:
                    line_idx += 1

        elif line.startswith("new.for.looping"):
            start = line.find('(') + 1
            end = line.rfind(')')
            inside_for = line[start:end].split(';')

            init_part = inside_for[0].strip().replace("type.integer", "").strip()
            var_name, var_val_raw = init_part.split('=')
            var_name = var_name.strip()
            VARIABLES[var_name] = get_parsed_value(var_val_raw)

            cond_part = inside_for[1].strip().split() # ['i', '<', '2']
            op = cond_part[1]
            target_val = get_parsed_value(cond_part[2])

            if (op == "<" and VARIABLES[var_name] < target_val) or (op == "==" and VARIABLES[var_name] == target_val):
                step_part = inside_for[2].strip()
                LOOP_STACK.append(("for", line_idx, var_name, op, target_val, step_part))
                line_idx += 1
            else:
                while line_idx < len(lines) and "}" not in lines[line_idx]:
                    line_idx += 1
                line_idx += 1

        elif line == "}":
            if LOOP_STACK:
                current_loop = LOOP_STACK[-1]

                if current_loop[0] == "while":
                    _, start_idx, condition = current_loop
                    if get_parsed_value(condition) in [True, "true"]:
                        line_idx = start_idx + 1
                        continue
                    else:
                        LOOP_STACK.pop()

                elif current_loop[0] == "for":
                    _, start_idx, var_name, op, target_val, step_part = current_loop

                    if "plusplus" in step_part:
                        VARIABLES[var_name] += 1
                    elif "minmin" in step_part:
                        VARIABLES[var_name] -= 1

                    if op == "<" and VARIABLES[var_name] < target_val:
                        line_idx = start_idx + 1
                        continue
                    else:
                        LOOP_STACK.pop()

            line_idx += 1

        elif line.startswith("input.new.users.putss"):
            start = line.find('(') + 1
            end = line.rfind(')')
            args = line[start:end].split(',')

            prompt = get_parsed_value(args[0])
            target_var = args[1].strip()

            user_input = input(f"{prompt}: ").strip()
            user_input = user_input.replace("\r", "").replace("\n", "").strip()

            if user_input.replace('.', '', 1).isdigit():
                VARIABLES[target_var] = float(user_input) if '.' in user_input else int(user_input)
            elif user_input.lower() == "true":
                VARIABLES[target_var] = True
            elif user_input.lower() == "false":
                VARIABLES[target_var] = False
            else:
                VARIABLES[target_var] = user_input

            line_idx += 1


        elif "plusplus" in line:
            var_name = line.replace("plusplus", "").replace(";", "").strip()
            if var_name in VARIABLES:
                VARIABLES[var_name] += 1
            else:
                print(f"Error: Variable {var_name} for fplusplus not found")
                sys.exit(1)

            line_idx += 1

        elif "=" in line and not line.startswith("new."):
            parts = line.split("=")
            var_name = parts[0].strip()
            expression = parts[1].strip()

            if "+" in expression:
                expr_parts = expression.split("+")
                left_val = get_parsed_value(expr_parts[0])
                right_val = get_parsed_value(expr_parts[1])
                VARIABLES[var_name] = left_val + right_val

            elif "-" in expression:
                expr_parts = expression.split("-")
                left_val = get_parsed_value(expr_parts[0])
                right_val = get_parsed_value(expr_parts[1])
                VARIABLES[var_name] = left_val - right_val

            else:
                VARIABLES[var_name] = get_parsed_value(expression)

            line_idx += 1

        elif "minmin" in line:
            var_name = line.replace("minmin", "").replace(";", "").strip()
            if var_name in VARIABLES:
                VARIABLES[var_name] -= 1
            else:
                print(f"Error: Variable {var_name} for fminmin not found")
                sys.exit(1)

            line_idx += 1

        else:
            line_idx += 1
