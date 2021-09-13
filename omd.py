# Guido van Rossum <guido@python.org>

duck_with_umbrella = """ 
*****************************************--.*********:************+#*%=*******-**********************************
***********************************************=@###+@#####@%+***@+==@+******************************************
*****************************************%#%:-:+++++*++++++===%####%%#*******************************************
*****************************+-******@#*:+++++++++++=====@%*++++++++@##+*****************************************
**********************************@@:*+++**+:*+++=====@=*++++++++++++=#+%#+**************************************
***************************--:*+#:*+++****+++++=====@**+++***++++++:++=#++=@%************************************
*****************************+#:+++++++++++++=====%=*+++*****+++++++++==#+++=@@**********************************
****************************#:+++++++++++++======#:+++*****++++++*+++++=%=+++==#=**-*****************************
**************************=%*=@##@%%%%@##@%=====@:++++++++++++++-++++++==@++++==%#**-:***************************
************************%##@===============@#@%@-+====+++++++++++++++++==#++++++==#******************************
************************=#%#+============%@==@##==========@#%+++++++++===#+++++++==#*****************************
*****************************%#+========#=====================@#+++++====#+++**++===#****************************
********************************=#%+===#++++===+++++=============#%======@++***+++===#***************************
************************************@##-+++++++++**+++++++=========#====@+++**++++===%=**:***********************
*************************************+%*++++++++++**+++++++++=======#%==@++++++++=====#*:-+**********************
*************************************%*=++++++++++++++++++++++++=====@%#==============@+*************************
*************************************%#%*=++++++++###*++++:-+++++====@###@@%==========%%*************************
*************************************+###=++++++*#-%#%+++++++++++++===%#======%##======@*************************
**************************************#:*+**+++++%###++++++++++++++====@==========@#===@*************************
*******************************+#%#@+**##=:+%#*+++**++++++++++++++====##@=++========%#@%*************************
*******************************#:++++++=+++=%%=@#@@+++++++++++++++===#*******+=%@###@@##*************************
*******************************+@+++++++++++++++%==%%=++++++++++===##+****************+**************************
*********************************=#%==+++++====%%%%#===+++++**%#@%%@#%#******************************************
*************************************=@##@@@@@##@@@######@@%%%%%@%%%@##+***@#+***********************************
***************************************+#:+@##@%%%%========%%%%%@#@====%#@===#***********************************
**************************************==*+@%#%%%%%%=======%@#@+**+@%=*++++==#************************************
**************************************#:+==*+*:*+=#@%%%**+++*#:*++++++++====@%***********************************
**************************************@**#:++:::**@%%=#*++++@*+++++++++++===#+***********************************
***************************************@#@:*+*:::*#===%#+++%*++++++++++==@%%@************************************
**********************************+#@@+=@=#:++*::**@=#++++++@++++++++++===%#*************************************
**********************************#+=#+#=@=#:+++++*+++++++++*@+++=====%##@***************************************
**********************************+@====%@**@+*+++**++++++++++=========#+****************************************
***********************************+%##@******%#*++++++++++++=======%#*******************************************
**********************************************#++=##=++++=======@###@+*******************************************
*************************************+=======#+#+%@==%#+=+=++=%%=%@#@=======+************************************
************************************============%==@%@=#+=#=%%#%==============+*********:************************
***************************************+===============@%=%@==============+**************************************
"""

duck_without_umbrella = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
		⢀   .                 
			......-:**+++++*:-....                           
 ... ...           ....*+****************+:..                         
     ..    .      ..-+***********************..                       
                ...****************************.                      
   ....    .    ..*****************************+...                   
.... .         ..:*******+%-..-+%**%*+**********+..                   
-===-.       .-+====****%-.-.==-.+##%=**********+:.                   
%+++=-......:=++++++=+**=.=%###@+-%*************+*.                   
==++=======++++++==++=**%.=%%##%*++*************+*.                   
.==++++++++++++====+++=**+%:*+**%+**************+:.                   
..-%=+++============+++=%+*********************++..                   
  .-=%@%=+++++++++=%%==+**********************+*..                    
  .%+++==%%%%%=+++++=%************::*********+:..                     
  .-*:.............-+******::::::**********+*....                     
                  ...+++****************++*...                        
                    .-++++++**********+*...                           
                  ...-++++*********++-.                               
                .....+++*********+:...                                
                ...*++*********+-..                                   
             ...-++**********+*..                                     
         .....*++************+...                                     
        ...-++**************+*... .. .........     .                  
       ...++******************+*****++++*:-...                        
     ...:+***********************************+*-...                   
     ..*+******************+++++++++***************-.....  ...:**-..  
   ...*+**************++***************++**************-....:.-+++*...
  ...*+*************+*****::::::**********++*************+*-..:+++*.+-
  ..:+************++***::::::****************+++******************+*+-
  ..+*************+****::::*************************+++++*********++:.
   -+*************+****:::**************************+++*********+++++-
  .-+*************+**************************++++++++++++**********+-.
  ..+**************+*******************************++++**********++...
  ..:+**************++***********************+++++++************++..  
  ...*****************++*************************+++++*********++-.   
 ..  .:+****************++*********************+++++***********+*..   
     ...*+****************+++**************++++++*************+*.     
        ..*++****************++++************+++************++:..     
        .....*++++++***************++++++++******+*********+*...      
             .....-:+++++++++++******************+*****+++:...        
                  ...*+*******+++***************++++++*-....          
              ..     ..-*+++++++*-*+***********+:-..                  
           ..-::-.........%++==.....-++++++++++....                   
          ..+%%=+++==+-..+=++%-.. .....-=++=%:...                     
          ..%%=++++++==+++++==++*..   ..=++=%..                       
          ..=%%%%%==+++++++=%%%%%%=:...-=++=+......                   
           ....+%+++++==+*:+%%=++++++++++++=%%===+..                  
             ...:++*-........=%=++++++=++++++++++==.                  
                          ..:%%===%@@=++=%*....--..                   
                             ...:%@%+++=-..                           
                        ..      .:%%==-...            """



def step2_umbrella():
	print(duck_with_umbrella)

def step2_no_umbrella():
	print(duck_without_umbrella)

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()