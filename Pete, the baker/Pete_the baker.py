'''
Solution of: https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
Author: Junaid
'''

def cakes(recipe, available):
    cnt = 0
    if len(recipe) <= len(available):
         ke = list(recipe.keys())[0]
         x = int(available[ke]/recipe[ke])
         if x is None:
                return cnt
         cnt = x
        
         for rec in recipe:
                x = int(available[rec]/recipe[rec])
                if x is None:
                    return 0
                else:
                    if cnt >= x:
                        cnt = x
                        
    return cnt
                    
        
        
                    
        
        