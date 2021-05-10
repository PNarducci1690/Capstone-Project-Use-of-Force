def off_cond(df, x):
    df.loc[x.str.contains('none|no inj|pulled away|nothing'), 'off_cond_type'] = 'no injuries noted or visible'
    df.loc[x.str.contains('broken|fractured|dislocated|tooth'), 'off_cond_type'] = 'broken, fractured, and dislocated bones'
    df.loc[x.str.contains('scrape|marks|abrasion|scratch'), 'off_cond_type'] = 'abrasions'
    df.loc[x.str.contains('laceration|cut'), 'off_cond_type'] = 'lacerations'
    df.loc[x.str.contains('sprain|strain|torn|tear|pull'), 'off_cond_type'] = 'muscular injury'
    df.loc[x.str.contains('pain|discomfort|right knee'), 'off_cond_type'] = 'complaint of pain'
    df.loc[x.str.contains('swell|bruis|head bump|red'), 'off_cond_type'] = 'swelling and bruising'
    df.loc[x.str.contains('taser|gun|knife|needle'), 'off_cond_type'] = 'weapon wound'
    df.loc[x.str.contains('bite|kick|push|strike|hit|slap|contact'), 'off_cond_type'] = 'physical assault'
    df.loc[x.str.contains('take|grab|push|kick|pull'), 'off_cond_type'] = 'physical force wound'
    df.loc[x.str.contains('major|minor'), 'off_cond_type'] = 'major and minor bleeding'
    df.loc[x.str.contains('spit|exposure|spat|waste|fluid|fuid|saliva'), 'off_cond_type'] = 'exposure to bodily fluids'
    
    return x