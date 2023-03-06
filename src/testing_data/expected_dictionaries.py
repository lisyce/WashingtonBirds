'''
Output dictionaries
'''
def for_diet_summarized():
    dictionary = {'cascades': ['Clupeiformes [herrings]', 'Euphausiacea [krill]',
       'Myctophiformes [lanternfishes]'], 'eastern': ['Euphausiacea [krill]', 'Myctophiformes [lanternfishes]',
       'Amphipoda [amphipods]'], 'pacific': ['Teuthida', 'Euphausiacea [krill]', 'Clupeiformes [herrings]']
       }
    return dictionary

def for_ecoregion_diversity():
    dictionary = {'ecoregion': {0: 'cascades', 1: 'eastern', 2: 'pacific'}, 'name': {0: 2, 1: 3, 2: 7}}
    return dictionary


def for_replaced_float():
    dictionary =  {'name': {0: 'Albatross', 1: 'Loon', 2: 'Crow', 3: 'Crow', 4: 'Crow', 5: 'Eagle', 6: 'Eagle', 7: 'Sparrow', 8: 'Hawk', 9: 'Owl', 10: 'Hummingbird', 11: 'Blue Jay'}, 'birdweb_society_link': {0: 'URL_Here', 1: 'URL_Here', 2: 'URL_Here', 3: 'URL_Here', 4: 'URL_Here', 5: 'URL_Here', 6: 'URL_Here', 7: 'URL_Here', 8: 'URL_Here', 9: 'URL_Here', 10: 'URL_Here', 11: 'URL_Here'}, 'ecoregion': {0: 'pacific', 1: 'pacific', 2: 'pacific', 3: 'cascades', 4: 'eastern', 5: 'cascades', 6: 'pacific', 7: 'pacific', 8: 'eastern', 9: 'eastern', 10: 'pacific', 11: 'pacific'}, 'jan_abundance': {0: 0, 1: 1, 2: 4, 3: 4, 4: 4, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 'feb_abundance': {0: 0, 1: 1, 2: 4, 3: 4, 4: 4, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 'mar_abundance': {0: 0, 1: 1, 2: 4, 3: 4, 4: 4, 5: 0, 6: 0, 7: 2, 8: 0, 9: 1, 10: 1, 11: 1}, 'apr_abundance': {0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 2, 6: 2, 7: 4, 8: 2, 9: 4, 10: 4, 11: 4}, 'may_abundance': {0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 2, 6: 2, 7: 1, 8: 2, 9: 4, 10: 4, 11: 4}, 'jun_abundance': {0: 2, 1: 4, 2: 3, 3: 4, 4: 4, 5: 1, 6: 1, 7: 4, 8: 1, 9: 4, 10: 4, 11: 4}, 'jul_abundance': {0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 2, 6: 2, 7: 2, 8: 2, 9: 4, 10: 4, 11: 4}, 'aug_abundance': {0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 2, 6: 1, 7: 2, 8: 2, 9: 4, 10: 4, 11: 4}, 'sep_abundance': {0: 0, 1: 4, 2: 4, 3: 4, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 4, 10: 4, 11: 4}, 'oct_abundance': {0: 2, 1: 4, 2: 4, 3: 4, 4: 4, 5: 2, 6: 2, 7: 0, 8: 2, 9: 4, 10: 4, 11: 4}, 'nov_abundance': {0: 2, 1: 2, 2: 4, 3: 4, 4: 4, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1}, 'dec_abundance': {0: 0, 1: 1, 2: 4, 3: 4, 4: 4, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1}, 'score': {0: 6, 1: 34, 2: 47, 3: 48, 4: 47, 5: 15, 6: 14, 7: 17, 8: 15, 9: 31, 10: 31, 11: 31}}
    return dictionary


def for_replaced():
    dictionary = {'name': {0: 'Albatross', 1: 'Loon', 2: 'Crow', 3: 'Crow', 4: 'Crow', 5: 'Eagle', 6: 'Eagle', 7: 'Sparrow', 8: 'Hawk', 9: 'Owl', 10: 'Hummingbird', 11: 'Blue Jay'}, 'birdweb_society_link': {0: 'URL_Here', 1: 'URL_Here', 2: 'URL_Here', 3: 'URL_Here', 4: 'URL_Here', 5: 'URL_Here', 6: 'URL_Here', 7: 'URL_Here', 8: 'URL_Here', 9: 'URL_Here', 10: 'URL_Here', 11: 'URL_Here'}, 'ecoregion': {0: 'pacific', 1: 'pacific', 2: 'pacific', 3: 'cascades', 4: 'eastern', 5: 'cascades', 6: 'pacific', 7: 'pacific', 8: 'eastern', 9: 'eastern', 10: 'pacific', 11: 'pacific'}, 'jan_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 'feb_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}, 'mar_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 1, 8: 0, 9: 1, 10: 1, 11: 1}, 'apr_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'may_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'jun_abundance': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'jul_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'aug_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'sep_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}, 'oct_abundance': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1}, 'nov_abundance': {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1}, 'dec_abundance': {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1}}
    return dictionary


def for_scores():
    dictionary = {'name': {0: 'Albatross', 1: 'Loon', 2: 'Crow', 3: 'Crow', 4: 'Crow', 5: 'Eagle', 6: 'Eagle', 7: 'Sparrow', 8: 'Hawk', 9: 'Owl', 10: 'Hummingbird', 11: 'Blue Jay'}, 'Spring': {0: 0.0, 1: 3.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 2.0, 6: 2.0, 7: 3.0, 8: 2.0, 9: 3.0, 10: 3.0, 11: 3.0}, 'Summer': {0: 1.0, 1: 3.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 3.0, 6: 3.0, 7: 3.0, 8: 3.0, 9: 3.0, 10: 3.0, 11: 3.0}, 'Fall': {0: 2.0, 1: 3.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 3.0, 6: 3.0, 7: 1.0, 8: 3.0, 9: 3.0, 10: 3.0, 11: 3.0}, 'Winter': {0: 0.0, 1: 3.0, 2: 3.0, 3: 3.0, 4: 3.0, 5: 1.0, 6: 1.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 1.0, 11: 1.0}, 'ecoregion': {0: 'pacific', 1: 'pacific', 2: 'pacific', 3: 'cascades', 4: 'eastern', 5: 'cascades', 6: 'pacific', 7: 'pacific', 8: 'eastern', 9: 'eastern', 10: 'pacific', 11: 'pacific'}}
    return dictionary
    
