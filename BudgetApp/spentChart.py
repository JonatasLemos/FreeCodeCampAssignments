def create_spent_chart(categories):
    category_values, len_names, names = [], [], []
    for object in categories:
        category_values.append(object.lost_money)
        len_names.append(len(object.name))
        names.append(object.name)

    percentages = [int((category_values[j]/sum(category_values)*100)) if category_values[j] > 0
                   else 0 for j in range(len(categories))]
    stars = ""
    text = "Percentage spent by category\n"
    for i in range(10, -1, -1):
        percents = (str(10 * i) + "|").rjust(4)+" "
        for j in range(len(percentages)):
            if 10*i <= percentages[j]:
                stars += "o  "
            else:
                stars += "   "
        text += percents + stars + "\n"
        if i == 0:
            n_of_dashes = 3*len(percentages) + 1
            text += (n_of_dashes * "-").rjust(n_of_dashes+4)
        stars = ""

    equal_names = []
    for i in names:
        i += " "*(max(len_names)-len(i))
        equal_names.append(i)
    spacing = [2]*(len(names)-1)
    spacing.insert(0, 6)
    text_word = ""

    for i in range(max(len_names)):
        for j in range(len(percentages)):
            text_word += equal_names[j][i].rjust(spacing[j]) + " "
        text_word += "\n"

    return text+"\n"+text_word