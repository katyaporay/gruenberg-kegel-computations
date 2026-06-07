LoadPackage("ctbllib");

# ----------------------------------------------------------------------
# Function: FrobeniusPQ( p, q )
#
# Input:
#   p – prime number
#   q – prime number
#
# Output:
#   Frobenius group p:q
# ----------------------------------------------------------------------

FrobeniusPQ := function( p, q )
    local desc;
    desc := Concatenation("C", String(p), " : C", String(q));
    return First(AllSmallGroups(p * q), G -> StructureDescription(G) = desc);
end;

