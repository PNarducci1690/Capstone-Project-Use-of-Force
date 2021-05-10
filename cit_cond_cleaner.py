def cit_cond(df, x):
    df.loc[x.str.contains('none|no injury'), 'cit_cond_type'] = 'no injuries noted or visible'
    df.loc[x.str.contains('broken|fractured|dislocated|tooth'), 'cit_cond_type'] = 'broken, fractured, and dislocated bones'
    df.loc[x.str.contains('scrape|marks|loss|abrasion|scratch|burn'), 'cit_cond_type'] = 'abrasions'
    df.loc[x.str.contains('laceration|lip|cut'), 'cit_cond_type'] = 'lacerations'
    df.loc[x.str.contains('taser|tazer|probe|puncture|prong'), 'cit_cond_type'] = 'taser wounds'
    df.loc[x.str.contains('breathing'), 'cit_cond_type'] = 'breathing issues'
    df.loc[x.str.contains('swelling|bruising'), 'cit_cond_type'] = 'swelling and bruising'
    df.loc[x.str.contains('pain|numb'), 'cit_cond_type'] = 'complaint of pain and discomfort'
    df.loc[x.str.contains('gun|knife'), 'cit_cond_type'] = 'weapon wound'
    df.loc[x.str.contains('oc/cs|chemical|spray|gas|csoc|red'), 'cit_cond_type'] = 'chemical weapon exposure'
    df.loc[x.str.contains('take|grab|push|kick|pull'), 'cit_cond_type'] = 'physical force wound'
    df.loc[x.str.contains('major|minor'), 'cit_cond_type'] = 'major and minor bleeding'
    df.loc[x.str.contains('unknown|unknwon'), 'cit_cond_type'] = 'other'
    
    return x