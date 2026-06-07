Read("find_dim_brauer.g");
Read("check_table.g");

CheckGroup := function( G, name, primes, output_file, info_file )
    local tbl, group_order, prime_divisors, prime, brauer_tbl, brauer_irreps,
        order, chi_idx, chi, chi_deg, nclasses, orders, class_idx, dim_fixed;
    # Load character table
    tbl := CharacterTable(G);
    if tbl = fail then
        AppendTo(output_file, "ERROR: Character table for ", name, " not found.\n\n");
        return;
    fi;
    
    AppendTo(output_file, "Group: ", name, "\n");
    AppendTo(output_file, "----------------------------------------\n");
    
    group_order := Size(tbl);
    for prime in primes do # prime = p1

        AppendTo(output_file, "Prime: ", prime, "\n");
        AppendTo(output_file, "----------------------------------------\n");

        # Get all irreducible brauer characters (absolutely irreducible representations)
        brauer_tbl := tbl mod prime;
        if brauer_tbl = fail then
            AppendTo(output_file, "ERROR: Brauer table not found\n");
            continue;
        fi;

        CheckTable(brauer_tbl, name, prime, output_file, info_file);

    od;
    AppendTo(output_file, "\n\n");
end;

