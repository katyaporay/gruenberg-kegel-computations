LoadPackage("ctbllib");

Read("find_dim_brauer.g");

# List of character table names for the desired groups and their automorphism groups
group_names := [
    "M22", "M22.2",
    "J3", "J3.2",
    "Fi24'", "Fi24'.2",
    "ON", "ON.2"
];

# Open output file
output_file := "fixedpoint_results.txt";
PrintTo(output_file, "Fixed point dimensions for groups J2, HS, McL, Ru and their automorphism groups\n");
PrintTo(output_file, "================================================================================\n\n");

info_file := "fixedpoint_main.txt";
PrintTo(info_file, "Group Chi p1 p2 Class Size\n");

for name in group_names do
    # Load character table
    tbl := CharacterTable(name);
    if tbl = fail then
        AppendTo(output_file, "ERROR: Character table for ", name, " not found.\n\n");
        continue;
    fi;
    
    AppendTo(output_file, "Group: ", name, "\n");
    AppendTo(output_file, "----------------------------------------\n");
    
    group_order := Size(tbl);
    prime_divisors := Set( FactorsInt( group_order ) );
    for prime in prime_divisors do # prime = p1

        AppendTo(output_file, "Prime: ", prime, "\n");
        AppendTo(output_file, "----------------------------------------\n");

        # Get all irreducible brauer characters (absolutely irreducible representations)
        brauer_tbl := tbl mod prime;
        if brauer_tbl = fail then
            AppendTo(output_file, "ERROR: Brauer table not found\n");
            continue;
        fi;
        brauer_irreps := Irr(brauer_tbl);

        AppendTo(output_file, "Number of characters: ", Length( brauer_irreps ), "\n\n");

        # For each irreducible character
        for chi_idx in [1 .. Length(brauer_irreps)] do # chi_idx - irreducible representation
            chi := brauer_irreps[chi_idx];
            chi_deg := chi[1];

            if chi_deg = 1 then
                continue;
            fi;

            AppendTo(output_file, "Character ", chi_idx, " (degree ", chi_deg, "):\n");
            AppendTo(info_file, name, " ", chi_idx, " ", prime, " ", -1, " ", -1, " ", group_order, "\n");
            
            # For each conjugacy class
            nclasses := NrConjugacyClasses(brauer_tbl);
            orders := OrdersClassRepresentatives(brauer_tbl);
            
            for class_idx in [1 .. nclasses] do # class of element g
                order := orders[class_idx]; # order should be p2
                if not IsPrime(order) or order = prime then
                    continue;
                fi;
                dim_fixed := FixedPointDimension(brauer_tbl, class_idx, chi);
                AppendTo(output_file, "  Class ", class_idx,
                         " (order ", order, "): dim C_V(g) = ", dim_fixed, "\n");
                if dim_fixed <> 0 then # C_K(g) != 1
                    # name of group A, number of representation, p1, p2, number of class of g, order of A 
                    AppendTo(info_file, name, " ", chi_idx, " ", prime, " ", order, " ", class_idx, " ", group_order, "\n");
                fi;
            od;
            AppendTo(output_file, "\n");
        od;
      od;
    AppendTo(output_file, "\n\n");
od;

Print("Done. Results written to ", output_file, "\n");

