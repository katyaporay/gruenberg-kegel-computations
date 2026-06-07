Read("find_dim_brauer.g");

# ----------------------------------------------------------------------
# Function: CheckTable( tbl, name, prime, output_file, debug_file )
# 
# Input:
#   tbl - brauer table for prime (or just character table)
#   name - name of current group
#   prime - prime number for current table was created
#   output_file - file for output
#   debug_file - file for debug
#
# Output:
#   Some debug information in debug_file and for output_file lines in format `{group name} {index of current representation} {p1} {p2} {index of class} {group order}` where p1 is prime, p2 is order of element g from some conjugacy class of current group. 
# ----------------------------------------------------------------------

CheckTable := function(tbl, name, prime, output_file, debug_file)
    local irreps, chi_idx, chi, chi_deg, nclasses, orders, order, class_idx, 
        dim_fixed, group_order;
    irreps := Irr(tbl); # all absolute irreducible characters
    group_order := Size(tbl);
    # For each irreducible character
    for chi_idx in [1 .. Length(irreps)] do # chi_idx - irreducible representation
        chi := irreps[chi_idx]; # current character 
        chi_deg := chi[1]; # its degree

        if chi_deg = 1 then # in case its trivial
            continue;
        fi;

        # Some debug info
        AppendTo(debug_file, "Character ", chi_idx, " (degree ", chi_deg, "):\n");
        # Print that currently character with chi_idx and primes is checked
        AppendTo(output_file, name, " ", chi_idx, " ", prime, " ", -1, " ", -1, " ", group_order, "\n");
        
        nclasses := NrConjugacyClasses(tbl); # Number of conjugacy classes
        orders := OrdersClassRepresentatives(tbl); # List of orders
        
        # For each conjugacy class
        for class_idx in [1 .. nclasses] do # class of element g
            order := orders[class_idx]; # order of some g from this class should be prime p2 != p1
            if not IsPrime(order) or order = prime then
                continue;
            fi;
            # Find dimension of C_K(g)
            dim_fixed := FixedPointDimension(tbl, class_idx, chi);
            AppendTo(debug_file, "  Class ", class_idx,
                     " (order ", order, "): dim C_V(g) = ", dim_fixed, "\n");
            if dim_fixed <> 0 then # C_K(g) != 1
                # name of group, index of representation, p1, p2, number of class of g, order of current group 
                AppendTo(output_file, name, " ", chi_idx, " ", prime, " ", order, " ", class_idx, " ", group_order, "\n");
            fi;
        od;
        AppendTo(debug_file, "\n");
    od;
end;

