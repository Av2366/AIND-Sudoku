from itertools import chain
from collections import defaultdict


assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'
puggle=[]
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers


    #General plan is to take the blocks that have two elements and put them in a list 
   



# Take a single box in the intersect - see if it's equal to original value
#  it is leave it alone. 
#if it's not blank out the digits. 







    print("Game Board", values)
    twin_values = [values[box] for box in values.keys() 
    if len(values[box]) == 2
        for peer in peers[box]
            if values[peer]==values[box]




    ]

  


    #get all the boxes with length 2

    twin_boxes = [box for box in values.keys() 
    if len(values[box]) == 2
        for peer in peers[box]
            if values[peer]==values[box]




    ]
    two_boxes = [box for box in values.keys()
        if len(values[box]) == 2 ]

    gemini = [box for box in two_boxes
        for peer in peers[box]
            if values[peer]==values[box] ]
    gemini = remove_duplicate_boxes(gemini)           


   
    print('skfalfkldfdjljlsdf',two_boxes)
    print('KDFJLKJFLKJDFLJLFJ',gemini)

# start of newer solution
# Take all blocks that have naked twins
# Take each one and blank out everything except the block it's equal to
# do this for everything
# return the board.



# part 1 





    #get all the boxes that are naked twins

    naked_twins_boxes = [box for box in twin_boxes
        for peer in peers[box]
            if values[box]==values[peer]
            ]

            #get rid of dupes

    naked_twins_boxes_reduced = remove_duplicate_boxes(naked_twins_boxes)



  #  print("twin values and singles", twin_values)
    #reduce list to only twins
    newlist= remove_singles(twin_values)
    singles=remove_duplicates(twin_values)
    nonunique = non_unique(twin_values)

   # nonunique=nonunique.sort()
    #twin_values=remove_singles(twin_values)
    print("twin values", twin_values)
    print('singles',singles)
   
    unique_twin_values=remove_duplicates(nonunique)
    print('unique twin values ',unique_twin_values)
  #  testlist=check_for_npair(unique_twin_values)
    print ('the NAKED TRUTH IS',naked_twins_boxes )
    print ('reduced set is',naked_twins_boxes_reduced)
    print ('should be equal to ',gemini)

#take the reduced list and check it's peers and run replace on boxes not equal to the box you're looking at. 





    print("Game Board before", values)
    for box in gemini:
        if len(values[box]) ==2:
            equal_box1= equals_search(values,box)
            intersect= intersection_of_peers(box,equal_box1)
            results = blank_out(values,intersect,equal_box1)

        else:
            continue









  #      for peer in peers[box]:
   #         if values[box]==values[peer]:
    #                both_values= values[box]
     #               print('BVS',both_values)
      #              digit1=both_values[0]
       #             digit2=both_values[1]
        #            if both_values!=values[peer]:
         #               if digit1 in values[peer]:
          #                  print('peer',values[peer])
           #                 values[peer] = values[peer].replace(digit1, '')
                        
            #            if digit2 in values[peer]:
             #               values[peer] = values[peer].replace(digit2, '')





   # for box in gemini:
    #    equals_search(box)
     #   print ('FUCKING',box)






        
        



        
         #   import ipdb;ipdb.set_trace()
           

            
           #BUG

                    
                        
                   
                    
                     #   print(peer,values[peer])
                        
                         
                 #   else:
                  #      continue
           # else:
            #    continue
        
#BUG
    print("Game Board after", values)
    return values       







    #print ('IQOIEUIOEIOWOEOUWOWOEIWIOIWUEOIWUEIOWIOEUOIU',naked_twin_values)       






#print ('akdjslsjdlsjdlsadlsadjsldlasdssdlsda',intersection_of_peers(A1,A2))







# from that list figure out which one are naked twins

# then take the first twin, run replacements rinse lather repeat 

   # return values




def intersection_of_peers(box,equal_box):

    a= set(peers[box])
    b= set(peers[equal_box])
    pug = (a & b)
    

    return list(pug)

def blank_out(values,intersect,equal_box):

    for box in intersect:
        
        boxx_value=values[equal_box]
        digit1=boxx_value[0]
        digit2=boxx_value[1]
        print ('skdjsakdj',boxx_value)    

        if  box != equal_box and len(boxx_value)==2:

            values[box] = values[box].replace(digit1, '')
            values[box] = values[box].replace(digit2, '')
        else:
            continue    
    return  values

def add_diagonals(peers):

    for box in peers:
        if box in diagonal1:
            diagon1= diagonal1.remove[box]
            peers[box].append(diagon1)

    for box in peers:
        if box in diagonal2:
            diagon2= diagonal2.remove[box]
            peers[box].append(diagon2)

    return peers

    


    


def equals_search(values,box):

    for peer in peers[box]:
        if values[box]==values[peer] and len(values[peer])==2:
            equal_box = peer
    return equal_box


    


#defining a remove dulicates function by converting to a set and then back. 

def remove_duplicates(twin_values):
    return list(set(twin_values))

def remove_duplicate_boxes(naked_twins_boxes):
    return list(set(naked_twins_boxes))

def non_unique(twin_values):
    for index in range(len(twin_values) - 1, -1, -1):
        if twin_values.count(twin_values[index]) == 1:
            del twin_values[index]
    return twin_values

def remove_singles(twin_values):
    list(filter((2).__ne__, twin_values))
    return twin_values

def cross(A, B):
    return [s+t for s in A for t in B]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
diagonal1 = ['A1','B2','C3','D4','E5','F6','G7','H8','I9']
diagonal2 = ['I1','H2','G3','F4','E5','D6','C7','B8','A9']
#peers = add_diagonals(peers)






def grid_values(grid):
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    

def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        # Your code here: Use the Eliminate Strategy
        vaules= only_choice(values)
        # Your code here: Use the Only Choice Strategy
         
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')