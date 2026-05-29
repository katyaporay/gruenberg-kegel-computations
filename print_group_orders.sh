
Print("Size: ", Size(G), "\n");
classes := ConjugacyClasses(G);

Print("Orders: ");
for class in classes do
    element := Representative(class);
    Print(Order(element), " ");
od;
Print("\n\n");
