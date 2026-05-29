# ----------------------------------------------------------------------
# Функция: FixedPointDimension( tbl, class_idx, character, p )
# 
# Вход:
#   tbl      – объект таблицы характеров (обычной или Брауэра)
#   class_idx – номер класса сопряжённости, в котором содержится g
#   character– характер модуля V (список значений по классам)
#
# ! Порядок элемента g и p должны быть взаимно просты ! Иначе UB
#
# Выход:
#   размерность dim C_V(g) (целое число)
# ----------------------------------------------------------------------
FixedPointDimension := function( tbl, class_idx, chi )
    local ords, g_order, sum, k, power_class;
    
    ords := OrdersClassRepresentatives( tbl );
    g_order := ords[class_idx];
    
    sum := 0;
    for k in [1 .. g_order] do
        power_class := PowerMap( tbl, class_idx, k );
        sum := sum + chi[power_class];
    od;
    
    if not (IsRat(sum) and DenominatorRat(sum) = 1) then
        Error("FixedPointDimension: sum is not an integer (got ", sum, ")");
    fi;

    return QuoInt( Int(sum), g_order );
end;

