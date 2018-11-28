with open(r"C:\Users\Shwaita\Downloads\HoLOCRtxtTrunc_copy.txt") as file:
    text = file.read() # text is a string of full text

print("Loaded text of length " + str(len(text))) # print number of characters

# split on '.' and '\n'
sentence_split = [".","\n","!","?"]
replaced_text = text
for punctuation in sentence_split:
    replaced_text = replaced_text.replace(punctuation,"<END>")
lines = replaced_text.split("<END>")
# lines is now a list of each 'line' in the text

lines = [line.strip() for line in lines if len(line.strip()) > 0] # remove all empty strings

target = input("Name? ") # get a name as input and save it in 'target'
case_sensitive = input("Case Sensitive? [Y/n] ")
case_sensitive = len(case_sensitive) == 0 or case_sensitive[0].lower() == "y"
adj_lines = int(input("Number of lines of context? "))

relevant_lines = []
for i in range(len(lines)):
    if case_sensitive:
        if target in lines[i]:
            if adj_lines == 0:
                relevant_lines.append(lines[i])
            else:
                relevant_lines.extend(lines[i-adj_lines:i+adj_lines+1])
    else:
        if target.lower() in lines[i].lower():
            if adj_lines == 0:
                relevant_lines.append(lines[i])
            else:
                relevant_lines.extend(lines[i-adj_lines:i+adj_lines+1])

with open("TextDump_" + target + "_" + str(adj_lines) + ".txt","w") as file:
    for rline in relevant_lines:
        file.write(rline + "\n")
