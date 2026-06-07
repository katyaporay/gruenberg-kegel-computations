Read("find_dim_brauer.g");

CheckTable := function(tbl, name, prime, output_file, info_file)
    local irreps, chi_idx, chi, chi_deg, nclasses, orders, order, class_idx, 
        dim_fixed, group_order;
    irreps := Irr(tbl);
    group_order := Size(tbl);
    # For each irreducible character
    for chi_idx in [1 .. Length(irreps)] do # chi_idx - irreducible representation
        chi := irreps[chi_idx];
        chi_deg := chi[1];

        if chi_deg = 1 then
            continue;
        fi;

        AppendTo(output_file, "Character ", chi_idx, " (degree ", chi_deg, "):\n");
        AppendTo(info_file, name, " ", chi_idx, " ", prime, " ", -1, " ", -1, " ", group_order, "\n");
        
        # For each conjugacy class
        nclasses := NrConjugacyClasses(tbl);
        orders := OrdersClassRepresentatives(tbl);
        
        for class_idx in [1 .. nclasses] do # class of element g
            order := orders[class_idx]; # order should be p2
            if not IsPrime(order) or order = prime then
                continue;
            fi;
            dim_fixed := FixedPointDimension(tbl, class_idx, chi);
            AppendTo(output_file, "  Class ", class_idx,
                     " (order ", order, "): dim C_V(g) = ", dim_fixed, "\n");
            if dim_fixed <> 0 then # C_K(g) != 1
                # name of group A, number of representation, p1, p2, number of class of g, order of A 
                AppendTo(info_file, name, " ", chi_idx, " ", prime, " ", order, " ", class_idx, " ", group_order, "\n");
            fi;
        od;
        AppendTo(output_file, "\n");
    od;
end;

