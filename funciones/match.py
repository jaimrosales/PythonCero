"""match => es el equivalente a switch en otros lenguajes"""


status = "solido"

match status:
    case "solido" | "liquido" | "gaseoso":
        print("solido o liquido o gaseoso")
    # case "solido" 
    #     print("solido")
    # case "Liquido": print("liquido")
    # case "gaseoso":
    #     print ("Gaseoso")
    case _:
        print("caso por defecto")
