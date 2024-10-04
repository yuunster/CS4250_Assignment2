Console output:
    
    ######### Menu ##############
    #a - Create a document
    #b - Update a document
    #c - Delete a document.
    #d - Output the inverted index ordered by term.
    #q - Quit
    
    Enter a menu choice: a
    Enter the ID of the document: 1
    Enter the text of the document: Baseball is played during summer months.
    Enter the title of the document: Exercise
    Enter the date of the document: 2024-09-03
    Enter the category of the document: Sports
    
    Enter a menu choice: d
    {'is': ['Exercise:1'], 'during': ['Exercise:1'], 'months': ['Exercise:1'], 'played': ['Exercise:1'], 'baseball': ['Exercise:1'], 'summer': ['Exercise:1']}
    
    Enter a menu choice: a
    Enter the ID of the document: 2
    Enter the text of the document: Summer is the time for picnics here. Picnics time!
    Enter the title of the document: California
    Enter the date of the document: 2024-09-04
    Enter the category of the document: Sports
    
    Enter a menu choice: d
    {'months': ['Exercise:1'], 'during': ['Exercise:1'], 'played': ['Exercise:1'], 'time': ['California:2'], 'summer': ['Exercise:1', 'California:1'], 'baseball': ['Exercise:1'], 'here': ['California:1'], 'the': ['California:1'], 'for': ['California:1'], 'picnics': ['California:2'], 'is': ['Exercise:1', 'California:1']}
    
    Enter a menu choice: a
    Enter the ID of the document: 3
    Enter the text of the document: Months, months, months later we found out why.
    Enter the title of the document: Discovery
    Enter the date of the document: 2024-09-05
    Enter the category of the document: Seasons
    
    Enter a menu choice: d
    {'during': ['Exercise:1'], 'baseball': ['Exercise:1'], 'why': ['Discovery:1'], 'picnics': ['California:2'], 'we': ['Discovery:1'], 'later': ['Discovery:1'], 'the': ['California:1'], 'is': ['Exercise:1', 'California:1'], 'played': ['Exercise:1'], 'time': ['California:2'], 'found': ['Discovery:1'], 'months': ['Discovery:3', 'Exercise:1'], 'here': ['California:1'], 'out': ['Discovery:1'], 'summer': ['Exercise:1', 'California:1'], 'for': ['California:1']}
    
    Enter a menu choice: a
    Enter the ID of the document: 4
    Enter the text of the document: Why is summer so hot here? So hot!
    Enter the title of the document: Arizona
    Enter the date of the document: 2024-09-06
    Enter the category of the document: Seasons
    
    Enter a menu choice: d
    {'so': ['Arizona:2'], 'for': ['California:1'], 'hot': ['Arizona:2'], 'months': ['Discovery:3', 'Exercise:1'], 'found': ['Discovery:1'], 'played': ['Exercise:1'], 'summer': ['Exercise:1', 'California:1', 'Arizona:1'], 'time': ['California:2'], 'here': ['California:1', 'Arizona:1'], 'out': ['Discovery:1'], 'later': ['Discovery:1'], 'picnics': ['California:2'], 'why': ['Arizona:1', 'Discovery:1'], 'we': ['Discovery:1'], 'the': ['California:1'], 'is': ['Exercise:1', 'California:1', 'Arizona:1'], 'during': ['Exercise:1'], 'baseball': ['Exercise:1']}
    
    Enter a menu choice: c
    Enter the document ID to be deleted: 3
    
    Enter a menu choice: d
    {'months': ['Exercise:1'], 'is': ['Exercise:1', 'California:1', 'Arizona:1'], 'hot': ['Arizona:2'], 'why': ['Arizona:1'], 'picnics': ['California:2'], 'for': ['California:1'], 'the': ['California:1'], 'so': ['Arizona:2'], 'here': ['California:1', 'Arizona:1'], 'baseball': ['Exercise:1'], 'summer': ['Exercise:1', 'California:1', 'Arizona:1'], 'played': ['Exercise:1'], 'time': ['California:2'], 'during': ['Exercise:1']}
    
    Enter a menu choice: b
    Enter the ID of the document: 4
    Enter the text of the document: Why is summer so hot here? This is a bad time!
    Enter the title of the document: Arizona
    Enter the date of the document: 2024-09-07
    Enter the category of the document: Seasons
    
    Enter a menu choice: d
    {'during': ['Exercise:1'], 'so': ['Arizona:1'], 'baseball': ['Exercise:1'], 'why': ['Arizona:1'], 'picnics': ['California:2'], 'the': ['California:1'], 'bad': ['Arizona:1'], 'is': ['Exercise:1', 'California:1', 'Arizona:2'], 'time': ['Arizona:1', 'California:2'], 'played': ['Exercise:1'], 'months': ['Exercise:1'], 'here': ['California:1', 'Arizona:1'], 'summer': ['Exercise:1', 'California:1', 'Arizona:1'], 'for': ['California:1'], 'a': ['Arizona:1'], 'this': ['Arizona:1'], 'hot': ['Arizona:1']}
    
    Enter a menu choice:
