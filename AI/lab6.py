def processRule(rule):
    rule = rule.replace('~', 'not ')
    rule = rule.replace('^', ' and ')
    rule = rule.replace('v', ' or ')
    return rule

def formatRule(rule, P, Q, R):
    P, Q, R = str(P), str(Q), str(R)
    rule = rule.replace('P', P)
    rule = rule.replace('Q', Q)
    rule = rule.replace('R', R)
    return rule

def checkEntailment(rule, query):
    models = [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True)
    ]
    rule = processRule(rule)
    entails = True

    for P, Q, R in models:
        formattedRule = formatRule(rule, P, Q, R) 
        print(f'Evaluating: {formattedRule}')
        KB = eval(formattedRule)
        _query = R if query == 'R' else P if query == 'P' else Q
        print(f'Knowledge Base: {KB}      Query: {_query}')
        if KB:
            entails &= KB and _query
            print(f'entails {entails}')

    if entails:
        print('Knowledge Base entails the query')
    else:
        print("Knowledge Base doesn't entail the query")
        
# Doesn't entail        
rule, query = '(Rv~P)v(Rv~Q)^(~RvP)^(~RvQ)', 'R'
checkEntailment(rule, query)

# Entails
rule, query = '(~Qv~PvR)^(~Q^P)^Q', 'R'
checkEntailment(rule, query)
