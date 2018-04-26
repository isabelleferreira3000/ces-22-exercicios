def o_que_essa_funcao_faz(*arguments, **keywords):
    for arg in arguments:
        print (arg)
    print ("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print (kw, ":", keywords[kw])
