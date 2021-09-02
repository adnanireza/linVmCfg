import re
from platform import system

def bashrc_processing(name_and_ips, lines):
    for (name, ip) in name_and_ips:
        found = False
        for idx in range(len(lines)):
            if re.match(r'{}="\d+\.\d+\.\d+\.\d+'.format(name), lines[idx]):
                lines[idx] = re.sub(r'\d+\.\d+\.\d+\.\d+', ip, lines[idx])
                found = True
                break
        if not found:
            lines.append('{}{}="{}"'.format('\r\n' if system().lower() == "windows" else '\n', name, ip))
    return lines

def add_line(orig_lines, new_lines):
    print(new_lines)
    for new_line in new_lines:
        found = False
        for idx in range(len(orig_lines)):
            if new_line.strip('\r\n ') == orig_lines[idx].strip('\r\n '):
                found = True
                break
        if not found:
            orig_lines.append('\r\n' + new_line if system().lower() == "windows" else '\n' + new_line.rstrip("\r"))
    if not system().lower() == "windows":
        orig_lines.append("\n")

# def bashrc_processing(name_and_ips, lines):
#     for (name, ip) in name_and_ips:
#         found = False
#         for idx in range(len(lines)):
#             if re.match(r'{}="\d+\.\d+\.\d+\.\d+'.format(name), lines[idx]):
#                 lines[idx] = re.sub(r'\d+\.\d+\.\d+\.\d+', ip, lines[idx])
#                 found = True
#                 break
#         if not found:
#             lines.append('{}{}="{}"'.format('\r\n' if system().lower() == "windows" else '\n', name, ip))
#     return lines

# def add_line(orig_lines, new_lines):
#     print(new_lines)
#     for new_line in new_lines:
#         found = False
#         for idx in range(len(orig_lines)):
#             if new_line == orig_lines[idx]:
#                 found = True
#                 break
#         if not found:
#             orig_lines.append(new_line if system().lower() == "windows" else new_line.rstrip("\r"))
#     if not system().lower() == "windows":
#         orig_lines.append("\n")