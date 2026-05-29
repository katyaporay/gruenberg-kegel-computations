# ----------------------------------------------------------------------
# Функция: FixedPointDimension( tbl, class_idx, character )
# 
# Вход:
#   brauer_tbl       – объект таблицы характеров Бруэра
#   class_idx        – номер класса сопряжённости, в котором содержится g
#   brauer_character – характер модуля V (список значений по классам)
#
# ! Порядок элемента g и p должны быть взаимно просты ! Иначе UB
#
# Выход:
#   размерность dim C_V(g) (целое число)
# ----------------------------------------------------------------------
FixedPointDimension := function( brauer_tbl, class_idx, brauer_chi )
    local ords, g_order, sum, k, power_class, ord_tbl, fusion, ord_class, power_ord_class;
    
    ords := OrdersClassRepresentatives( brauer_tbl );
    g_order := ords[class_idx];
    
    # Get ordinary table and fusion
    ord_tbl := OrdinaryCharacterTable( brauer_tbl );
    if ord_tbl = fail then
        Error( "No underlying ordinary table found" );
    fi;
    fusion := FusionConjugacyClasses( brauer_tbl, ord_tbl );
    if fusion = fail then
        Error( "Fusion map not available" );
    fi;
    
    # Get ordinary class
    ord_class := fusion[class_idx];
    
    sum := 0;
    for k in [1 .. g_order] do
        power_ord_class := PowerMap( ord_tbl, k, ord_class );
        if power_ord_class = fail then
            Error( "PowerMap failed for exponent ", k );
        fi;
        # Searching for this class in brauer table
        power_class := Position( fusion, power_ord_class );
        if power_class = fail then
            Error( "Class ", power_ord_class, " is not p-regular" );
        fi;
        sum := sum + brauer_chi[power_class];
    od;
    

    if not (IsRat(sum) and DenominatorRat(sum) = 1) then
        Error("FixedPointDimension: sum is not an integer (got ", sum, ")");
    fi;

    return QuoInt( Int(sum), g_order );
end;

