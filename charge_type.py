
def cit_charge(df, x):
    '''
    Function that perfomrs additional cleaning for citizen charge type
    
    Args:
       df (dataframe)
       x is column from dataframe
       
   Returns:
      Reorganized and cleaned dataset where similar charges are categorized into one generic category
    '''
    df.loc[x.str.contains('resist'), 'citcharge_type'] = 'resisting arrest'
    df.loc[x.str.contains('battery|assault|strangulation'), 'citcharge_type'] = 'assault and battery'
    df.loc[x.str.contains('lifting|stolen|rob|fraud|forgery|conversion|burglary'), 'citcharge_type'] = 'theft'
    df.loc[x.str.contains('substance|marijuana|para|cocaine|meth|dealing'), 'citcharge_type'] = 'drug possesion and use'
    df.loc[x.str.contains('handgun|firearm'), 'citcharge_type'] = 'weapon possesion'
    df.loc[x.str.contains('public'), 'citcharge_type'] = 'disorderly conduct'
    df.loc[x.str.contains('escape|leaving'), 'citcharge_type'] = 'leaving crime scene'
    df.loc[x.str.contains('murder|homicide'), 'citcharge_type'] = 'murder'
    df.loc[x.str.contains('car|vehicle|joyriding|driving|traffic'), 'citcharge_type'] = 'vehicular crime'
    df.loc[x.str.contains('rape|prostitution|child|minor'), 'citcharge_type'] = 'sex crime'
    df.loc[x.str.contains('animal'), 'citcharge_type'] = 'animal cruelty'
    df.loc[x.str.contains('protective'), 'citcharge_type'] = 'violation of protective order'
    df.loc[x.str.contains('mischief'), 'citcharge_type'] = 'criminal mischief'
    df.loc[x.str.contains('trespass|entry'), 'citcharge_type'] = 'trespass'
    df.loc[x.str.contains('obstruction|reporting'), 'citcharge_type'] = 'obstruction of justice'
    df.loc[x.str.contains('nuisance'), 'citcharge_type'] = 'common nuisance'
    df.loc[x.str.contains('writ'), 'citcharge_type'] = 'immediate detention'
    df.loc[x.str.contains('kidnap'), 'citcharge_type'] = 'criminal confinement'
    
    return x
        
