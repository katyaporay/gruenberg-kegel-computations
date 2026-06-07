LoadPackage("ctbllib");

FrobeniusPQ := function( p, q )
    local desc;
    desc := Concatenation("C", String(p), " : C", String(q));
    return First(AllSmallGroups(p * q), G -> StructureDescription(G) = desc);
end;

