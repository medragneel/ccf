import re

def lines(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")


def match_lines(lines,pattern):
    for line in lines:
        if pattern in line:
            yield line


def get_class(matches):
    pattern = r'"(.*?)"'
    for _,v in enumerate(matches):
        split_result = re.split(pattern,v)
        try:
            cls = split_result[1].split(" ")
            for classname in cls:
                yield classname
        except IndexError:
            print("Error: Failed to split string: {}".format(v))

def extract_class_rules(css_file, specific_classes):
    with open(css_file, 'r') as file:
        css_content = file.read()

    for class_name in specific_classes:
        regex = r'(\.' + class_name + r'\s*\{[\w\W]*?\})'
        class_rules = re.findall(regex, css_content)
        for class_rule in class_rules:
            yield class_rule


html = lines("./merged.html")


html_matches = match_lines(html,"class")




mm = set(get_class(html_matches))


for class_rule in extract_class_rules("./style.css", mm):
    print(class_rule)
