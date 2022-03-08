import importlib as importlib
keys= ["__name__","__doc__","__package__","__loader__","__spec__","__file__","__cached__","__builtins__"]
html_core = ['<!DOCTYPE html>','<html lang="en">','<head>','<meta charset="UTF-8">',
    '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>Document</title>','</head>','</head>','<body>','</body>','</html>']

def parse_type(txt:str) -> str:
    """ side method, parses the text of the type into a single word."""
    return str(txt)[str(txt).find("'")+1:str(txt).rfind("'")]

def doc_for_module(modulepy:str, htmlfile:str):
    pac = modulepy[0:modulepy.rfind(".")]
    module= importlib.import_module(pac)
    head = [ module.__name__, module.__doc__]
    func_names = [str(arg) for arg in module.__dict__ if str(arg) not in keys]
    doc = {str(f):getattr(module, str(f)).__doc__ for f in func_names}
    annons = {str(f):getattr(module, str(f)).__annotations__ for f in func_names}


    with open(f"./{htmlfile}","w+") as file:
        for line in html_core:
            if line == '<body>':
                file.write("<h1>Module {}: </h1>\n".format(str(head[0])))
                file.write(str(head[1])+"\n")
                for name in func_names:
                    file.write("<h2>Function {}: </h2>\n".format(name))
                    file.write("{}\n".format(doc[name]))
                    file.write("<h3>Annotations</h3>\n")
                    for annon in annons:
                        for d in dict(annons[annon]):
                            if "class" in str(dict(annons[annon])[d]):
                                file.write("<p>{} : {}\n</p>".format(d,parse_type(dict(annons[annon])[d]) ))
                            else:
                                file.write("<p>{} : {}\n</p>".format(d,dict(annons[annon])[d]))
            file.write(line+"\n")
    

    