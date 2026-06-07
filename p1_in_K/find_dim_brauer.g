# ----------------------------------------------------------------------
# Function: FixedPointDimension( tbl, class_idx, character )
# 
# Input:
#   brauer_tbl - brauer table for some prime number p
#   class_idx - index of conjugacy where for some element g of prime order
#   brauer_character – character of current representation
#
# ! Order of g and p should be distinct
#
# Output:
#   dimenstion of C_V(g) (integer)
# ----------------------------------------------------------------------
FixedPointDimension := function( brauer_tbl, class_idx, brauer_chi )
    local ords, g_order, sum, k, power_class, power_tbl, dim;
    
    ords := OrdersClassRepresentatives( brauer_tbl ); # table of order for brauer table
    g_order := ords[class_idx]; # order of element g
    
    sum := 0;
    for k in [1 .. g_order] do
        power_tbl := PowerMap( brauer_tbl, k ); # find power table for k
        if power_tbl = fail then
            Error( "PowerTbl failed for exponent ", k );
        fi;
        power_class := power_tbl[class_idx]; # class of element g^k
        if power_class = fail then
            Error( "PowerMap failed for class ", class_idx );
        fi;
        sum := sum + brauer_chi[power_class]; # add value of brauer character on g^k
    od;
    
    dim := sum / g_order; # divide by |g|
    if not IsInt( dim ) then
        Error("FixedPointDimension: sum is not an integer (got ", sum, ")");
    fi;

    return dim;
end;

