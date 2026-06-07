LoadPackage("ctbllib");

Read("frobenius.g");
Read("check_group.g");

# List of groups which all brauer tables and all absolute irreducible characters will be checked
group_names := [
    "J3",
    "ON",
];

# List of:
# 1) Value which will be passed to CharacterTable(...)
# 2) Group name
# 3) List of primes p1 which will be checked
additional_groups := [
    ["M22", "M22", [3, 5, 7]],
    ["M22.2", "M22.2", [2]],
    ["Fi23", "Fi23", [3]],
];

# Print first lines for debug
debug_file := "fixedpoint_debug.txt";
PrintTo(debug_file, "Fixed point dimensions for groups J2, HS, McL, Ru and their automorphism groups\n");
PrintTo(debug_file, "================================================================================\n\n");

# Print first lines to output
output_file := "fixedpoint_main.txt";
PrintTo(output_file, "Group Chi p1 p2 Class Size\n");

for name in group_names do
    group_order := Size(CharacterTable(name)); # Count group order
    prime_divisors := Set( FactorsInt( group_order ) ); # Create set of all prime divisors
    CheckGroup(name, name, prime_divisors, output_file, debug_file);
od;

for pair in additional_groups do
    G := pair[1]; # Value which will be passed to ChatacterTable(...)
    name := pair[2]; # Group name
    primes := pair[3]; # List of primes p1 which will be checked
    CheckGroup(G, name, primes, output_file, debug_file);
od;

# Print last line for debug
Print("Done. Results written to ", debug_file, "\n");

