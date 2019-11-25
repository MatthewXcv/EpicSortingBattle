
#Her laver vi selve sorteringen af hver linje som et "item".
def insertionSort(list):
    #Her looper den processen igennem alle itemsne i listen.
    for i in range(1, len(list)):
        """
        Itemsne i listen som er random placeret, er på pladser.
        De pladser starter på 0 og hent til hvor mange der er f.eks:
        [0,1,2,3,4,5,6] alle disse er antallet af items (i) i listen.
        Så j bliver diffineret som den plads vi er ved og vi starter ved plads 1
        ,hvor så at i bliver defineret til plads 0, hvor den starter nemlig i-1. Så
        i er en plads til venstre fra j.
        """
        j = list[i]
        i = i - 1
        #"i" kan ikke bliver på en plads der er mindre end 0.
        #fordi at den starter fra plads 0 og går op.
        while i >= 0:
            """
            Hvis "j" er mindre end "i", så bliver "j" rykket
            en til venstre fordi at de tal der er til venstre er mindst værdi
            det har vi valgt det til at gøre sådan.
            Så bliver "j" som f.eks var på plads 4 nu på plads 3, fordi den
            blev rykket en til venstre. Så trækker vi 1 fra "i", så den igen er
            en til venstre for "j". Og så bliver de to værdier igen tjekket om
            "j" er mindre en "i" til at tilsidst at "j" er større end "i",
            hvor så breaker den og går videre til den næste i listen eller
            at listen er ved slutningen nemlig plads 0.
            """
            if j < list[i]:
                list[i + 1] = list[i]
                list[i] = j
                i = i - 1
            else:
                break

def selectionSort(list):
    # Gør så den looper denne process igennem alle itemsne i listen.
    for i in range(len(list)):

        """
        Den starter med at sige at "i" er den mindste værdi og det item, som
        man er kommet til i listen. Så lopper den i gennem alle de itemsne efter "i"
        og tjekker om itemsne er mindre end i. Hvis der er et item, som er
        mindre end "i", så bliver det det nye med mindste værdi. Og så tjekker den
        videre igennem alle itemsne og så bliver den mindste værdi navngivet som
        den mindste værdi.
        """

        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j

        """
        Her bliver så den navngivet mindsteværdi rykket frem til den forreste
        plads i listen (altså, hvor "i" er i "for j in range")
        """
        list[i], list[min_idx] = list[min_idx], list[i]
