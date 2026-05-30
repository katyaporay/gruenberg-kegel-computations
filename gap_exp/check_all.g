LoadPackage("ctbllib");

Read("frobenius.g");
Read("check_group.g");

# List of character table names for the desired groups and their automorphism groups
group_names := [
    "M22", "M22.2",
    "J3", "J3.2",
    "Fi24'", "Fi24'.2",
    "ON", "ON.2",
];

additional_groups := [
    "Fi23",
];

# Open output file
output_file := "fixedpoint_results.txt";
PrintTo(output_file, "Fixed point dimensions for groups J2, HS, McL, Ru and their automorphism groups\n");
PrintTo(output_file, "================================================================================\n\n");

info_file := "fixedpoint_main.txt";
PrintTo(info_file, "Group Chi p1 p2 Class Size\n");

for name in group_names do
    group_order := Size(CharacterTable(name));
    prime_divisors := Set( FactorsInt( group_order ) );
    CheckGroup(name, name, prime_divisors, output_file, info_file);
od;

for name in additional_groups do
    CheckGroup(name, name, [2, 3], output_file, info_file);
od;

Print("Done. Results written to ", output_file, "\n");

