import random
import os
import time



def read():
       
    with open("archivos\DATA.txt", "r", encoding="utf-8") as f:
        words = [i.replace('\n', '') for i in f]
    return(words)

def run():
    AHORCADO = ['''



                    +---+

                    |   |

                        |

                        |

                        |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                        |

                        |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                    |   |

                        |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                   /|   |

                        |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                   /|\  |

                        |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                   /|\  |

                   /    |

                        |

                    =========''', '''



                    +---+

                    |   |

                    O   |

                   /|\  |

                   / \  |

                        |

                    =========''']

    os.system("cls")
    
    hangman = """
        __  _____    _   __________  ______    _   __
       / / / /   |  / | / / ____/  |/  /   |  / | / /
      / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ / 
     / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /  
    /_/ /_/_/  |_/_/ |_/\____/_/  /_/_/  |_/_/ |_/   
    
    """
    win = """
    __  ______  __  __   _       _______   __   __
    \ \/ / __ \/ / / /  | |     / /  _/ | / /  / /
     \  / / / / / / /   | | /| / // //  |/ /  / / 
     / / /_/ / /_/ /    | |/ |/ // // /|  /  /_/  
    /_/\____/\____/     |__/|__/___/_/ |_/  (_)   

    """
    game_over= """
       _________    __  _________   ____ _    ____________  
      / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \ 
     / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ / 
    / /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/  
    \____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|

    """                                                
                                                             
    print(hangman)
    
    word_random = random.choice(read())
    # print(word_random)
    character_replace = word_random.maketrans('áéíóú', 'aeiou')
    character_replaced = word_random.translate(character_replace)
    word_random = character_replaced
    secret_list = list(word_random)
    vocal = ''
    while vocal not in ["a", "e", "i", "o", "u"]:
        vocal=random.choice(secret_list)
    
    trys=0
    max_trys = 6
    print(AHORCADO[trys] + '\n' + '\n')
    word_ocult = len(word_random)*('_')
    word_ocult = list(word_ocult)
    word_ocult[word_random.index(vocal)]= vocal
    print('               ' + ' '.join(word_ocult) + '\n')
    answer= """         
                
                1 - Volver a jugar
                2 - Cerrar el juego

                Elige una opcion:
                """
  
    while trys<= max_trys and word_random != "".join(word_ocult):
      
        try:

            letra = input('               Ingrese una letra: ').lower()
            if len(letra) >= 2:
                raise ValueError
        
        except ValueError:
            print('               Debes ingresar una letra')
            time.sleep(1)
       
        finally:


            if letra in word_random: 
                # ind= word_random.index(letra)
                # word_ocult[ind]=letra
                for i in range(len(word_ocult)):
                    if word_random[i]==letra:
                        word_ocult[i]=letra
        
            else:
                trys += 1
                
                
            os.system("cls")
            print(hangman)
            print("          " + AHORCADO[trys] + '\n' + '\n')          
            print('               ' + ' '.join(word_ocult) + '\n')
            

            if trys == 6: 
                os.system("cls")
                print(hangman)
                print('     ★·.·´¯`·.·★' + ' La palabra era: ' + (word_random).capitalize
                () + ' ★·.·´¯`·.·★' + '\n' + '\n')
                print(game_over)
                
                opcion = int(input(answer))
                if opcion == 1:
                        run()
                else:
                    break
                
            
            if ''.join(word_ocult) == word_random:
                os.system("cls")
                print(hangman)
                print('     ★·.·´¯`·.·★' + 'La palabra era: ' + (word_random).capitalize
                () + ' ★·.·´¯`·.·★' + '\n' + '\n')
                print(win)
                
                opcion = int(input(answer))
                if opcion == 1:
                        run()
                else:
                    break 
                
if __name__ == '__main__':
    run()