def cakes(recipe, available):
    m=[]
    s=True
    for i in recipe.keys():
      if not i in available:
        return 0
      else:
        if recipe[i]>available[i]:
          return 0
        else:
          m.append(available[i]//recipe[i])
    return min(m)
