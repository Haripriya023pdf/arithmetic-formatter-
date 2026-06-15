def arithmetic_arranger(problems, show_answers=False):
    # 1. Quantity check (Up to 5 problems allowed)
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []
    
    for problem in problems:
        pieces = problem.split()
        top_num = pieces[0]
        operator = pieces[1]
        bottom_num = pieces[2]
        
        # 2. Error Checks (Max 4 digits)
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if not top_num.isdigit() or not bottom_num.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(top_num) > 4 or len(bottom_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
        width = max(len(top_num), len(bottom_num)) + 2
        
        if operator == '+':
            math_result = int(top_num) + int(bottom_num)
        else:
            math_result = int(top_num) - int(bottom_num)
            
        # --- Manual Spacing Calculations (All aligned under the loop) ---
        top_spaces = width - len(top_num)
        top_row.append((" " * top_spaces) + top_num)
        
        bottom_spaces = width - len(bottom_num) - 1
        bottom_row.append(operator + (" " * bottom_spaces) + bottom_num)
        
        dash_row.append("-" * width)
        
        result_str = str(math_result)
        answer_spaces = width - len(result_str)
        answer_row.append((" " * answer_spaces) + result_str)

    # --- BLOCK 4: OUTSIDE THE LOOP (Aligned with the 'for' statement) ---
    joined_top = "    ".join(top_row)
    joined_bottom = "    ".join(bottom_row)
    joined_dash = "    ".join(dash_row)

    if show_answers:    
        joined_answer = "    ".join(answer_row)
        return joined_top + "\n" + joined_bottom + "\n" + joined_dash + "\n" + joined_answer
    else:
        return joined_top + "\n" + joined_bottom + "\n" + joined_dash
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
