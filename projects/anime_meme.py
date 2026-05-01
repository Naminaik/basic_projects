import random 

subject = [
   "Naruto Uzumaki",
   "Goku",
   "Monkey D. Luffy",
   "Saitama",
   "Levi Ackerman",
   "Light Yagami",
   "Gojo Satoru",
   "Tanjiro Kamado"
]

action = ["says he will protect",
         "yells about becoming the king of",
         "casually one-punches",
         "dramatically declares war on",
         "whispers plans to control",
         "flexes while explaining",
         "promises to never abandon",
         "cries while defending"
         ]

place_object = [ 
                "his precious ramen",
                "the entire universe...",
                "the last slice of pizza...",
                "humanity’s strongest cleaning supplies...",
                "a mysterious notebook...",
                "the infinity of space...",
                "his nakama (friends)...",
                "a random demon..."
                ]

while True:
    subjects = random.choice(subject)
    actions = random.choice(action)
    place_objects = random.choice(place_object)
    headline = f"MEME OF THE DAY: {subjects} {actions} {place_objects}" 
    print("\n" + headline)
    asking = input("\n DO YOU WANT TO SEE ANOTHER MEME ?(y/n): ").upper().strip() 
   
    while True:#.strip() removes spaces from start to end of the string 
      if asking == "Y":
        break
      elif asking =="N":
        print("THANK YOU FOR USING THE ANIME MRME GENERATIOR, SEE YOU NEXT TIME!")
        exit()
      else:
         print("INVALID INPUT , PLEASE ENTER Y OR N")
         asking = input("\n DO YOU WANT TO SEE ANOTHER MEME ?(y/n): ").upper().strip()
         