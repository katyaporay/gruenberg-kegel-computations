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
    local ords, g_order, sum, k, power_class, power_tbl, dim;
    
    ords := OrdersClassRepresentatives( brauer_tbl );
    g_order := ords[class_idx];
    
    sum := 0;
    for k in [1 .. g_order] do
        power_tbl := PowerMap( brauer_tbl, k );
        if power_tbl = fail then
            Error( "PowerTbl failed for exponent ", k );
        fi;
        power_class := power_tbl[class_idx];
        if power_class = fail then
            Error( "PowerMap failed for class ", class_idx );
        fi;
        sum := sum + brauer_chi[power_class];
    od;
    
    dim := sum / g_order;
    if not IsInt( dim ) then
        Error("FixedPointDimension: sum is not an integer (got ", sum, ")");
    fi;

    return dim;
end;

