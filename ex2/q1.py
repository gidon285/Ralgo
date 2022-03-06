html_core = ['<!DOCTYPE html>','<html lang="en">','<head>','<meta charset="UTF-8">',
    '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>Document</title>','</head>','</head> <h1>this is for ex2</h1>','<body>','</body>','</html>']

def doc_for_module(pyfile:str, modulepy:str, htmlfile:str):
    with open(pyfile, "r"):
        print("PL")
    with open(htmlfile,"w") as file:
        for line in html_core:
            file.write(line+"\n")
        
doc_for_module("python_doc_to_html.py","mymodule.py","mydoc.html")
# if __name__ == "__main":
    