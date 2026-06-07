Read("find_dim_brauer.g");
Read("check_table.g");

# ----------------------------------------------------------------------
# Function: CheckGroup( G, name, primes, output_file, debug_file )
# 
# Input:
#   G - value which will be passed to ChatacterTable(...)
#   name - name of current group
#   primes - list of primes which will be checked
#   output_file - file for output
#   debug_file - file for debug
#
# Output:
#   Some debug information in debug_file and for output_file lines in format `{group name} {index of current representation} {p1} {p2} {index of class} {group order}` where p1 is prime number from primes, representation is modular for p1, p2 is order of element g from some conjugacy class of current group. 
# ----------------------------------------------------------------------

CheckGroup := function( G, name, primes, output_file, debug_file )
    local tbl, prime, brauer_tbl; 
    # Load character table
    tbl := CharacterTable(G);
    if tbl = fail then
        AppendTo(debug_file, "ERROR: Character table for ", name, " not found.\n\n");
        return;
    fi;
    
    AppendTo(debug_file, "Group: ", name, "\n");
    AppendTo(debug_file, "----------------------------------------\n");
   
    for prime in primes do # prime = p1

        AppendTo(debug_file, "Prime: ", prime, "\n");
        AppendTo(debug_file, "----------------------------------------\n");

        # Get all irreducible brauer characters (absolutely irreducible representations)
        brauer_tbl := tbl mod prime;
        if brauer_tbl = fail then
            AppendTo(debug_file, "ERROR: Brauer table not found\n");
            continue;
        fi;

        CheckTable(brauer_tbl, name, prime, output_file, debug_file);

    od;
    AppendTo(debug_file, "\n\n");
end;

